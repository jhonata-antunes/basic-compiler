from tkn import Token


class AsciiClassifier:
    def __init__(self, ascii_filter):
        self.ascii_filter = ascii_filter

    def get_categorized_char(self):
        char = self.ascii_filter.get_char()
        token = Token(value=char)
        if is_digit(char):
            token.token_class = Token.DIGIT
        elif is_letter(char):
            token.token_class = Token.LETTER
        else:
            token.token_class = Token.SPECIAL
        return token


def is_digit(char):
    return '0' <= char <= '9'


def is_letter(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'
