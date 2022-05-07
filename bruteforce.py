from itertools import combinations
from models.action import Wallet
from models.import_data import Data
from tools.timer import timer

MAX_INVEST = 500

path = r"datas/short-dataset1_Python+P7.csv"


class BruteForce:
    """
    Classe permettant de faire la somme de toutes les combinaisons
    possibles pour ensuite les trier et garder la meilleure
    """

    def __init__(self, wallet, max_invest):
        """
        :param wallet: Objet Wallet contenant toutes les actions du fichier source
        :param max_invest: Montant seuil à ne pas dépasser pour l'investissement
        """
        self.wallet = wallet
        self.max_invest = max_invest
        self.best_invest = []
        self.launch_bruteforce()

    @timer
    def launch_bruteforce(self):

        # On crée au fur et à mesure toutes les combinations possibles
        for i in range(1, len(self.wallet.actions) + 1):
            action_combinations = combinations(self.wallet.actions, i)

            for combination in action_combinations:
                # On stock chaque combinaison dans un Wallet pour calculer
                # automatiquement le cout total des actions
                combination_wallet = Wallet(combination)

                # Si le montant total est sous le seuil alors on garde la combinaison
                if combination_wallet.action_cost <= self.max_invest:
                    self.best_invest.append(combination_wallet)

        # On trie les combinaisons par montant de revenu
        self.best_invest.sort(key=lambda x: x.action_revenu, reverse=False)
        # On affiche le meilleur investissement
        print(self.best_invest[-1])


wallet_datas = Data(path).datas
test = BruteForce(wallet_datas, MAX_INVEST)
