from models.action import Wallet
from models.import_data import Data
from tools.timer import timer

MAX_INVEST = 500.0

path = r"datas/short-dataset1_Python+P7.csv"
path = r"datas/dataset1_Python+P7.csv"
# path = r"datas/dataset2_Python+P7.csv"


class Optimized:

    def __init__(self, wallet, max_invest):
        """
        :param wallet: Objet Wallet contenant toutes les actions du fichier source
        :param max_invest: Montant seuil à ne pas dépasser pour l'investissement
        """
        self.wallet = wallet
        self.max_invest = max_invest
        self.launch_optimisation()

    @timer
    def launch_optimisation(self):

        # On instancie une liste avec des Wallets vides
        # Dans le but d'optimiser la vitesse, je crée une liste ne
        # descendant que jusqu'aux dizaines de centimes
        actual = [Wallet() for x in range(int(self.max_invest * 10) + 1)]

        # Je passe sur chacune des actions
        for action in self.wallet.actions:
            # Je mets en mémoire la précédente liste
            memory = list(actual)
            # On calcule le cout de l'action à la dizaine de centimes prêt
            cost = int(round(action.cost * 10))

            # On ne boucle que sur les élements du tableau ayant un montant supérieur au cout de l'action
            for key, value in enumerate(actual[cost:], start=cost):
                # On calcule ce que donnerait le nouveau revenu avec l'ation en cours
                check_revenu = action.revenu + memory[key - cost].action_revenu
                # On calcule ce que donnerait le nouveau cout avec l'ation en cours
                check_cost = action.cost + memory[key - cost].action_cost

                # On vérifie que le nouveau revenu est supérieur à l'ancien revenu
                if self.max_invest >= check_cost and check_revenu > value.action_revenu:
                    # On met la nouvelle combinaison d'action dans la liste
                    actual[key] = Wallet([action] + memory[key - cost].actions)

        # On récupère et on affiche le meilleur investissement
        best = actual[-1]
        print(str(best))


wallet_datas = Data(path).datas
test = Optimized(wallet_datas, MAX_INVEST)
