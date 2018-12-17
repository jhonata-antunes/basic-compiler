from recognizers.automaton import Automaton
from tkn import Token


class Lexical(Automaton):

    def __init__(self):
        super().__init__([1, 2, 3, 4, 5, 6, 7, 8])

    def get_class(self):
        class_map = {
            Token.INT: [1],
            Token.ID: [2],
            Token.SPECIAL: [3, 4, 5, 6, 7, 8]
        }
        if self.get_state() in class_map[Token.INT]:
            return Token.INT
        elif self.get_state() in class_map[Token.ID]:
            return Token.ID
        elif self.get_state() in class_map[Token.SPECIAL]:
            return Token.SPECIAL

    def process_atom(self, token):
        ve = False

        if self.state == 0:
            if token.is_digit():
                self.state = 1
            elif token.is_letter():
                self.state = 2
            elif token.is_special():
                if token.value == '>':
                    self.state = 3
                elif token.value == '<':
                    self.state = 5
                elif token.value == ' ' or token.value == '\n':
                    pass
                else:
                    self.state = 8
            else:
                ve = True

        elif self.state == 1:
            if token.is_digit():
                pass
            else:
                ve = True

        elif self.state == 2:
            if token.is_letter() or token.is_digit():
                pass
            else:
                ve = True

        elif self.state == 3:
            if token.value == '=':
                self.state = 4
            else:
                ve = True

        elif self.state == 4:
            ve = True

        elif self.state == 5:
            if token.value == '=':
                self.state = 6
            elif token.value == '>':
                self.state = 7
            else:
                ve = True

        elif self.state == 6:
            ve = True

        elif self.state == 7:
            ve = True

        elif self.state == 8:
            ve = True

        else:
            raise AttributeError("Current state '{}' does not exist".format(self.state))

        if ve:
            raise ValueError("Invalid input '{}' to state '{}'".format(token.value, self.state))
