from recognizers.automaton import Automaton


class Eb(Automaton):

    def __init__(self):
        super().__init__([1, 2, 3, 5])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.is_int():
                self.state = 1
            elif token.is_special():
                if token.value == ".":
                    self.state = 2
                elif token.value == "(":
                    self.state = 7
                else:
                    ve = True
            elif token.is_id():
                if token.value == "FN":
                    self.state = 9
                elif token.value == "SIN" or \
                        token.value == "COS" or\
                        token.value == "TAN" or \
                        token.value == "ATN" or \
                        token.value == "EXP" or \
                        token.value == "ABS" or \
                        token.value == "LOG" or \
                        token.value == "SQR" or \
                        token.value == "INT" or \
                        token.value == "RAND":
                    self.state = 10
                else:
                    ve = True
            else:
                ve = True
        elif self.state == 1:
            if token.value == ".":
                self.state = 2
            else:
                ve = True

        elif self.state == 2:
            if token.is_int():
                self.state = 3
            else:
                ve = True

        elif self.state == 3:
            if token.value == "E":
                self.state = 4
            else:
                ve = True

        elif self.state == 4:
            if token.is_int():
                self.state = 5
            elif token.is_special():
                if token.value == "+" or token.value == "-":
                    self.state = 6
                else:
                    ve = True
            else:
                ve = True

        elif self.state == 5:
            ve = True

        elif self.state == 6:
            if token.is_int():
                self.state = 5
            else:
                ve = True

        elif self.state == 7:
            self.state = 8
            return Exp()

        elif self.state == 8:
            if token.value == ")":
                self.state = 5
            else:
                ve = True

        elif self.state == 9:
            if token.is_letter():
                self.state = 10
            else:
                ve = True

        elif self.state == 10:
            if token.value == ")":
                self.state = 7
            else:
                ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
