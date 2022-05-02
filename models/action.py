class StockAction:

    def __init__(self, name, profit, price):
        try:
            if '%' in profit:
                self.benefit = float(profit.replace('%', '')) / 100
            else:
                self.benefit = float(profit) / 100
            self.cost = float(price)
            self.revenu = round(self.benefit * self.cost, 2)
            self.name = name
        except BaseException as e:
            print("On action", name, "We have an error :", e)

    def __repr__(self):
        return self.name


class Wallet:

    def __init__(self, actions=[]):
        self.action_revenu = 0
        self.action_cost = 0
        self.actions = actions
        self.compute_actions_values()

    def add_actions(self, actions):
        self.actions.append(actions)
        self.compute_actions_values()

    def remove_actions(self, actions):
        self.actions.remove(actions)
        self.compute_actions_values()

    def compute_actions_values(self):
        self.action_cost = sum(action.cost for action in self.actions)
        self.action_revenu = sum(action.revenu for action in self.actions)

    def __repr__(self):
        result = f"-----------------------------------------\n" \
                 f"WALLET\nRevenus:{self.action_revenu}" \
                 f"\tCost:{self.action_cost}" \
                 f"\tNumber of actions:{len(self.actions)}" \
                 f"\nActions:\n"
        for action in self.actions:
            result += f"{action}; "
        result += "\n-----------------------------------------\n"
        return result
