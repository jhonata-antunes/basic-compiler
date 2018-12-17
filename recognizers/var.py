from recognizers.automaton import Automaton
from recognizers.exp import Exp


class Var(Automaton):

    def __init__(self):
        super().__init__([1, 4])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.is_letter():
                self.state = 1
            else:
                ve = True

        elif self.state == 1:
            if token.value == "(":
                self.state = 2
            elif token.is_digit():
                self.state = 4
            else:
                ve = True

        elif self.state == 2:
            self.state = 3
            return Exp()

        elif self.state == 3:
            if token.value == ",":
                self.state = 2
            elif token.value == ")":
                self.state = 4
            else:
                ve = True

        elif self.state == 4:
            ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
