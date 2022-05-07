import csv
from models.action import StockAction, Wallet


class Data:
    """
    Classe servant à Importer les données et Instancier uns classe Wallet avec les StockAction dedans
    """
    def __init__(self, path):
        self.path = path
        if '.csv' in path:
            self.datas = self.import_csv()

    def import_csv(self):
        with open(self.path, newline='', encoding='utf-8-sig') as csvfile:
            datas = csv.DictReader(csvfile, delimiter=',')
            return Wallet([StockAction(**row) for row in datas if float(row['price']) > 0])
