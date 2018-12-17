from recognizers.automaton import Automaton


class Character(Automaton):

    def __init__(self):
        super().__init__([1])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.is_letter() or \
                    token.is_digit() or \
                    token.is_special():
                self.state = 1
            else:
                ve = True

        elif self.state == 1:
            ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
