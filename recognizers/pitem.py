from recognizers.automaton import Automaton
from recognizers.character import Character


class PItem(Automaton):

    def __init__(self):
        super().__init__([3, 4])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.value == '"':
                self.state = 1
            else:
                self.state = 4
                return Exp()

        elif self.state == 1:
            self.state = 2
            return Character()

        elif self.state == 2:
            if token.value == '"':
                self.state = 3
            else:
                return Exp()

        elif self.state == 3:
                self.state = 4
                return Exp()

        elif self.state == 4:
                ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
