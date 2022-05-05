from models.action import Wallet
from models.import_data import Data
from tools.timer import timer
from math import ceil
from sortedcontainers import SortedDict

MAX_INVEST = 500

path = r"datas/short-dataset1_Python+P7.csv"
path = r"datas/dataset1_Python+P7.csv"
path = r"datas/dataset2_Python+P7.csv"

class Optimized:

    @timer
    def __init__(self, path, max_invest):
        self.path = path
        data = Data(path)
        self.wallet = data.datas
        self.max_invest = max_invest

        actual = SortedDict({x: Wallet() for x in range(max_invest + 1)})

        for action in self.wallet.actions:
            memory = SortedDict(actual)
            cost = ceil(action.cost)
            for key, value in actual.items():
                if key >= cost:
                    new = Wallet([action] + memory[key - cost].actions)
                    if self.max_invest >= new.action_cost and new.action_revenu > value.action_revenu:
                        actual[key] = new
        best = actual.popitem()
        print(str(best[1]))


test = Optimized(path, MAX_INVEST)
