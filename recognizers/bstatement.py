from recognizers.automaton import Automaton
from recognizers.character import Character
from recognizers.exp import Exp
from recognizers.pitem import PItem
from recognizers.snum import SNum
from recognizers.var import Var


class BStatement(Automaton):

    def __init__(self):
        super().__init__([5, 7, 10, 12, 13, 14, 28,31,37,43])

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.is_int():
                self.state = 1
            else:
                ve = True

        elif self.state == 1:
            if token.is_key_word():
                if token.value == "RETURN":
                    self.state = 5
                elif token.value == "LET":
                    self.state = 2
                elif token.value == "READ":
                    self.state = 6
                elif token.value == "DATA":
                    self.state = 9
                elif token.value == "PRINT":
                    self.state = 12
                elif token.value == "GOTO" or token.value == "GOSUB":
                    self.state = 15
                elif token.value == "GO":
                    self.state = 16
                elif token.value == "IF":
                    self.state = 17
                elif token.value == "FOR":
                    self.state = 22
                elif token.value == "NEXT":
                    self.state = 30
                elif token.value == "DIM":
                    self.state = 32
                elif token.value == "DEF":
                    self.state = 38
                elif token.value == "REM":
                    self.state = 43
                else:
                    ve = True
            else:
                ve = True

        elif self.state == 2:
            self.state = 3
            return Var()

        elif self.state == 3:
            if token.value == "=":
                self.state = 4
            else:
                ve = True

        elif self.state == 4:
            self.state = 5
            return Exp()

        elif self.state == 5:
            ve = True

        elif self.state == 6:
            self.state = 7
            return Var()

        elif self.state == 7:
            if token.value == ",":
                self.state = 8
            else:
                ve = True

        elif self.state == 8:
            self.state = 7
            return Var()

        elif self.state == 9:
            self.state = 10
            return SNum()

        elif self.state == 10:
            if token.value == ",":
                self.state = 11
            else:
                ve = True

        elif self.state == 11:
            self.state = 10
            return SNum()

        elif self.state == 12:
            self.state = 13
            return PItem()

        elif self.state == 13:
            if token.value == ",":
                self.state = 14
            else:
                ve = True

        elif self.state == 14:
            self.state = 13
            return PItem()

        elif self.state == 15:
            if token.is_int():
                self.state = 5
            else:
                ve = True

        elif self.state == 16:
            if token.value == "TO":
                self.state = 15
            else:
                ve = True

        elif self.state == 17:
            self.state = 18
            return Exp()

        elif self.state == 18:
            if token.value == ">=" or \
                    token.value == ">" or \
                    token.value == "<>" or \
                    token.value == "<" or \
                    token.value == "<=" or \
                    token.value == "=":
                self.state = 19
            else:
                ve = True

        elif self.state == 19:
            self.state = 20
            return Exp()

        elif self.state == 20:
            if token.value == "THEN":
                self.state = 21
            else:
                ve = True

        elif self.state == 21:
            if token.is_int():
                self.state = 5
            else:
                ve = True

        elif self.state == 22:
            if token.is_letter():
                self.state = 23
            else:
                ve = True

        elif self.state == 23:
            if token.is_digit():
                self.state = 24
            elif token.value == "=":
                self.state = 25
            else:
                ve = True

        elif self.state == 24:
            if token.value == "=":
                self.state = 25
            else:
                ve = True

        elif self.state == 25:
            self.state = 26
            return Exp()

        elif self.state == 26:
            if token.value == "TO":
                self.state = 27
            else:
                ve = True

        elif self.state == 27:
            self.state = 28
            return Exp()

        elif self.state == 28:
            if token.value == "STEP":
                self.state = 29
            else:
                ve = True

        elif self.state == 29:
            self.state = 5
            return Exp()

        elif self.state == 30:
            if token.is_letter():
                self.state = 31
            else:
                ve = True

        elif self.state == 31:
            if token.is_digit():
                self.state = 5
            else:
                ve = True

        elif self.state == 32:
            if token.is_letter():
                self.state = 33
            else:
                ve = True

        elif self.state == 33:
            if token.value == "(":
                self.state = 34
            else:
                ve = True

        elif self.state == 34:
            if token.is_int():
                self.state = 35
            else:
                ve = True

        elif self.state == 35:
            if token.value == ",":
                self.state = 36
            elif token.value == ")":
                self.state = 37
            else:
                ve = True

        elif self.state == 36:
            self.state = 35
            return Var()

        elif self.state == 37:
            if token.value == ",":
                self.state = 32
            else:
                ve = True

        elif self.state == 38:
            if token.value == "FN":
                self.state = 39
            else:
                ve = True

        elif self.state == 39:
            if token.value == "(":
                self.state = 40
            else:
                ve = True

        elif self.state == 40:
            if token.is_letter():
                self.state = 41
            else:
                ve = True

        elif self.state == 41:
            if token.value == "=":
                self.state = 42
            elif token.is_digit():
                self.state = 44
            else:
                ve = True

        elif self.state == 42:
            self.state = 5
            return Exp()

        elif self.state == 43:
            return Character()

        elif self.state == 44:
            if token.value == "=":
                self.state = 42
            elif token.is_digit():
                pass
            else:
                ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
