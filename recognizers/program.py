from recognizers.automaton import Automaton
from recognizers.exp import Exp


class Program(Automaton):

    def __init__(self):
        super().__init__([56])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.is_int():
                self.state = 1
            else:
                ve = True

        elif self.state == 1:
            if token.is_key_word():
                if token.value == "LET":
                    self.state = 2
                elif token.value == "RETURN":
                    self.state = 9
                elif token.value == "READ":
                    self.state = 10
                elif token.value == "DATA":
                    self.state = 16
                elif token.value == "PRINT":
                    self.state = 24
                elif token.value == "GOTO" or token.value == "GOSUB":
                    self.state = 34
                elif token.value == "GO":
                    self.state = 29
                elif token.value == "IF":
                    self.state = 30
                elif token.value == "FOR":
                    self.state = 35
                elif token.value == "NEXT":
                    self.state = 42
                elif token.value == "DIM":
                    self.state = 43
                elif token.value == "DEF FN":
                    self.state = 49
                elif token.value == "":
                    self.state = 0
                else:
                    ve = True
            else:
                ve = True

        elif self.state == 2:
            if token.is_id():
                self.state = 3
            else:
                ve = True

        elif self.state == 3:
            if token.value == "(":
                self.state = 4
            elif token.value == "=":
                self.state = 8
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 4:
            self.state = 5
            return Exp()

        elif self.state == 5:
            if token.value == ",":
                self.state = 6
            elif token.value == ")":
                self.state = 7
            else:
                ve = True

        elif self.state == 6:
            self.state = 5
            return Exp()

        elif self.state == 7:
            if token.value == "=":
                self.state = 8
            else:
                ve = True

        elif self.state == 8:
            self.state = 9
            return Exp()

        elif self.state == 9:
            if token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 10:
            if token.is_id():
                self.state = 11
            else:
                ve = True

        elif self.state == 11:
            if token.value == ",":
                self.state = 10
            elif token.value == "(":
                self.state = 12
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 12:
            self.state = 13
            return Exp()

        elif self.state == 13:
            if token.value == ",":
                self.state = 14
            elif token.value == ")":
                self.state = 15
            else:
                ve = True

        elif self.state == 14:
            self.state = 13
            return Exp()

        elif self.state == 15:
            if token.value == ",":
                self.state = 10
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 16:
            if token.value == "+" or token.value == "-":
                self.state = 17
            elif token.is_int():
                self.state = 18
            elif token.value == ".":
                self.state = 19
            else:
                ve = True

        elif self.state == 17:
            if token.is_int():
                self.state = 18
            elif token.value == ".":
                self.state = 19
            else:
                ve = True

        elif self.state == 18:
            if token.value == ",":
                self.state = 16
            elif token.value == ".":
                self.state = 19
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 19:
            if token.is_int():
                self.state = 18
            else:
                ve = True

        elif self.state == 20:
            if token.value == ",":
                self.state = 16
            elif token.value == "E":
                self.state = 21
            else:
                ve = True

        elif self.state == 21:
            if token.value == "+" or token.value == "-":
                self.state = 22
            elif token.is_int():
                self.state = 23
            else:
                ve = True

        elif self.state == 22:
            if token.is_int():
                self.state = 23
            else:
                ve = True

        elif self.state == 23:
            if token.value == ",":
                self.state = 16
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 24:
            if token.value == '"':
                self.state = 25
            elif token.is_int():
                self.state = 55
            else:
                self.state = 28
                return Exp()

        elif self.state == 25:
            if token.value != '"':
                self.state = 26
            else:
                ve = True

        elif self.state == 26:
            if token.value == '"':
                self.state = 27
            else:
                pass

        elif self.state == 27:
            if token.value == ",":
                self.state = 24
            elif token.is_int():
                self.state = 55
            else:
                self.state = 28
                return Exp()

        elif self.state == 28:
            if token.value == ",":
                self.state = 24
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 29:
            if token.value == "TO":
                self.state = 34
            else:
                ve = True

        elif self.state == 30:
            self.state = 31
            return Exp()

        elif self.state == 31:
            if token.value == ">=" or token.value == ">" or token.value == "<>" or \
                    token.value == "<" or token.value == "<=" or token.value == "=":
                self.state = 32
            else:
                ve = True

        elif self.state == 32:
            self.state = 33
            return Exp()

        elif self.state == 33:
            if token.value == "THEN":
                self.state = 34
            else:
                ve = True

        elif self.state == 34:
            if token.is_int():
                self.state = 9
            else:
                ve = True

        elif self.state == 35:
            if token.is_id():
                self.state = 36
            else:
                ve = True

        elif self.state == 36:
            if token.value == "=":
                self.state = 37
            else:
                ve = True

        elif self.state == 37:
            self.state = 38
            return Exp()

        elif self.state == 38:
            if token.value == "TO":
                self.state = 39
            else:
                ve = True

        elif self.state == 39:
            self.state = 40
            return Exp()

        elif self.state == 40:
            if token.value == "STEP":
                self.state = 41
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 41:
            self.state = 9
            return Exp()

        elif self.state == 42:
            if token.is_id():
                self.state = 9
            else:
                ve = True

        elif self.state == 43:
            if token.is_id():
                self.state = 44
            else:
                ve = True

        elif self.state == 44:
            if token.value == "(":
                self.state = 45
            else:
                ve = True

        elif self.state == 45:
            if token.is_int():
                self.state = 46
            else:
                ve = True

        elif self.state == 46:
            if token.value == ",":
                self.state = 47
            elif token.value == ")":
                self.state = 48
            else:
                ve = True

        elif self.state == 47:
            if token.is_int():
                self.state = 46
            else:
                ve = True

        elif self.state == 48:
            if token.value == ",":
                self.state = 43
            elif token.is_int():
                self.state = 55
            else:
                ve = True

        elif self.state == 49:
            if token.is_id():
                self.state = 50
            else:
                ve = True

        elif self.state == 50:
            if token.value == "(":
                self.state = 51
            else:
                ve = True

        elif self.state == 51:
            if token.is_id():
                self.state = 52
            else:
                ve = True

        elif self.state == 52:
            if token.value == ")":
                self.state = 53
            else:
                ve = True

        elif self.state == 53:
            if token.value == "=":
                self.state = 54
            else:
                ve = True

        elif self.state == 54:
            self.state = 9
            return Exp()

        elif self.state == 55:
            if token.value == "END":
                self.state = 56
            elif token.is_key_word():
                if token.value == "LET":
                    self.state = 2
                elif token.value == "RETURN":
                    self.state = 9
                elif token.value == "READ":
                    self.state = 10
                elif token.value == "DATA":
                    self.state = 16
                elif token.value == "PRINT":
                    self.state = 24
                elif token.value == "GOTO" or token.value == "GOSUB":
                    self.state = 34
                elif token.value == "GO":
                    self.state = 29
                elif token.value == "IF":
                    self.state = 30
                elif token.value == "FOR":
                    self.state = 35
                elif token.value == "NEXT":
                    self.state = 42
                elif token.value == "DIM":
                    self.state = 43
                elif token.value == "DEF FN":
                    self.state = 49
                elif token.value == "":
                    self.state = 0
                else:
                    ve = True
            else:
                ve = True

        elif self.state == 56:
            ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("{}: Invalid input '{}' to state '{}'"
                             .format(self.__class__.__name__, token.value, self.state))
