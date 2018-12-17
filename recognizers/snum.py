from recognizers.automaton import Automaton
from recognizers.num import Num


class SNum(Automaton):

    def __init__(self):
        super().__init__([1])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.value == "+" or token.value == "-":
                self.state = 2
            else:
                self.state = 1
                return Num()

        elif self.state == 1:
            ve = True

        elif self.state == 2:
            self.state = 1
            return Num()

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
