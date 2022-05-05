from models.action import Wallet
from models.import_data import Data
from tools.timer import timer
from math import ceil
from sortedcontainers import SortedDict

MAX_INVEST = 500.0

path = r"datas/short-dataset1_Python+P7.csv"
path = r"datas/dataset1_Python+P7.csv"
path = r"datas/dataset2_Python+P7.csv"


class Optimized:

    @timer
    def __init__(self, path, max_invest):
        data = Data(path)
        self.wallet = data.datas
        self.max_invest = max_invest

        actual = [Wallet() for x in range(int(max_invest * 100) + 1)]
        for action in self.wallet.actions:
            memory = list(actual)
            cost = int(action.cost * 100)
            for key, value in enumerate(actual[cost:], start=cost):
                check_revenu = action.revenu + memory[key - cost].action_revenu
                check_cost = action.cost + memory[key - cost].action_cost
                if self.max_invest >= check_cost and check_revenu > value.action_revenu:
                    actual[key] = Wallet([action] + memory[key - cost].actions)
        best = actual[-1]
        print(str(best))


test = Optimized(path, MAX_INVEST)
