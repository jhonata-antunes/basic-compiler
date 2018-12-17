from recognizers.automaton import Automaton


class Program(Automaton):

    def __init__(self):
        super().__init__([3])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            self.state = 1
            pass
            # return BStatement()

        elif self.state == 1:
            if token.is_int():
                self.state = 2
            else:
                pass
                # return BStatement()

        elif self.state == 2:
            if token.value == "END":
                self.state = 3
            else:
                ve = True

        elif self.state == 3:
                ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
