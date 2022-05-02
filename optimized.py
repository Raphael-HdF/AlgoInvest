from models.action import Wallet
from models.import_data import Data
from tools.timer import timer
from math import ceil
from sortedcontainers import SortedDict

MAX_INVEST = 500

path = r"datas/short-dataset1_Python+P7.csv"


class Optimized:

    @timer
    def __init__(self, path, max_invest):
        self.path = path
        data = Data(path)
        self.wallet = data.datas
        self.max_invest = max_invest

        actual = SortedDict({x: Wallet() for x in range(max_invest + 1)})

        for action in self.wallet.actions:
            cost = ceil(action.cost)
            for key, value in actual.items():
                if key >= cost:
                    new = Wallet([action] + actual[key - cost].actions)
                    actual[key] = new if new.action_revenu > value.action_revenu else value
        best = actual.popitem()
        print(best)


test = Optimized(path, MAX_INVEST)
