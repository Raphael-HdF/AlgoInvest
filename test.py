import itertools
from itertools import combinations

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

condition = 10

test = combinations(liste, 4)

for t in test:
    print(t)

def check_condition(liste, condition):
    element = liste.pop()
    # for li in liste:


# check_condition(liste, condition)
