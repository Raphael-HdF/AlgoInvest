class StockAction:

    def __init__(self, action, benefice, cout):
        try:
            if '%' in benefice:
                self.benefit = float(benefice.replace('%', '')) / 100
            else:
                self.benefit = float(benefice)
            self.cost = float(cout)
            self.revenu = self.benefit * self.cost
            self.name = action
        except BaseException as e:
            print("On action", action, "We have an error :", e)


class Wallet:

    def __init__(self, actions=[]):
        self.action_value = 0
        self.actions = actions
        self.compute_actions_value()

    def add_actions(self, actions):
        self.actions.append(actions)
        self.compute_actions_value()

    def remove_actions(self, actions):
        self.actions.remove(actions)
        self.compute_actions_value()

    def compute_actions_value(self):
        self.action_value = sum(action.cost for action in self.actions)

