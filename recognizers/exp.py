from recognizers.automaton import Automaton


class Exp(Automaton):

    def __init__(self):
        super().__init__([5, 6, 8, 11])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.value == "+" or token.value == "-":
                pass
            elif token.value == "(":
                self.state = 3
            elif token.value == ".":
                self.state = 7
            elif token.is_key_word():
                if token.value == "FN":
                    self.state = 1
                elif token.value == "SIN" or \
                        token.value == "COS" or \
                        token.value == "TAN" or \
                        token.value == "ATN" or \
                        token.value == "EXP" or \
                        token.value == "ABS" or \
                        token.value == "LOG" or \
                        token.value == "SQR" or \
                        token.value == "INT" or \
                        token.value == "RAND":
                    self.state = 2
                else:
                    ve = True
            elif token.is_int():
                self.state = 6
            elif token.is_id():
                self.state = 11
            else:
                ve = True

        elif self.state == 1:
            if token.is_id():
                self.state = 2
            else:
                ve = True

        elif self.state == 2:
            if token.value == "(":
                self.state = 3
            else:
                ve = True

        elif self.state == 3:
            self.state = 5
            return Exp()

        elif self.state == 4:
            if token.value == ")":
                self.state = 5
            else:
                ve = True

        elif self.state == 5:
            if token.value == "+" or token.value == "-" or \
                    token.value == "*" or token.value == "/":
                self.state = 15
            else:
                ve = True

        elif self.state == 6:
            if token.value == ".":
                self.state = 7
            elif token.value == "+" or token.value == "-" or \
                    token.value == "*" or token.value == "/":
                self.state = 15
            else:
                ve = True

        elif self.state == 7:
            if token.is_int():
                self.state = 8
            else:
                ve = True

        elif self.state == 8:
            if token.value == "+" or token.value == "-" or \
                    token.value == "*" or token.value == "/":
                self.state = 15
            elif token.value == "E":
                self.state = 9
            else:
                ve = True

        elif self.state == 9:
            if token.value == "+" or token.value == "-":
                self.state = 10
            else:
                ve = True

        elif self.state == 10:
            if token.is_int():
                self.state = 5
            else:
                ve = True

        elif self.state == 11:
            if token.value == "+" or token.value == "-" or \
                    token.value == "*" or token.value == "/":
                self.state = 15
            elif token.value == "(":
                self.state = 12
            else:
                ve = True

        elif self.state == 12:
            self.state = 13
            return Exp()

        elif self.state == 13:
            if token.value == ")":
                self.state = 5
            elif token.value == ",":
                self.state = 14
            else:
                ve = True

        elif self.state == 14:
            self.state = 13
            return Exp()

        elif self.state == 15:
            if token.value == "(":
                self.state = 3
            elif token.value == ".":
                self.state = 7
            elif token.is_key_word():
                if token.value == "FN":
                    self.state = 1
                elif token.value == "SIN" or \
                        token.value == "COS" or \
                        token.value == "TAN" or \
                        token.value == "ATN" or \
                        token.value == "EXP" or \
                        token.value == "ABS" or \
                        token.value == "LOG" or \
                        token.value == "SQR" or \
                        token.value == "INT" or \
                        token.value == "RAND":
                    self.state = 2
                else:
                    ve = True
            elif token.is_int():
                self.state = 6
            elif token.is_id():
                self.state = 11
            else:
                ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("{}: Invalid input '{}' to state '{}'"
                             .format(self.__class__.__name__, token.value, self.state))
