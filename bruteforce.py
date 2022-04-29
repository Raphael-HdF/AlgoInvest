from pprint import pprint
import csv
from itertools import combinations
from models.action import StockAction, Wallet

MAX_INVEST = 500

path = r"brute-datas.csv"


def import_datas(src):
    df = []
    with open(src, newline='', encoding='utf-8-sig') as csvfile:
        datas = csv.DictReader(csvfile, delimiter=';')
        return Wallet([StockAction(**row) for row in datas])


def brute_force():
    wallet = import_datas(path)
    best_invest = []
    for i in range(1, len(wallet.actions)+1):
        action_combinations = combinations(wallet.actions, i)
        for combination in action_combinations:
            # if combination.cost <= MAX_INVEST:
            best_invest.append(combination)
    pprint(best_invest)


brute_force()
