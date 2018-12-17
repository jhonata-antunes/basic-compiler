from tkn import Token

KEY_WORDS = [
    'END',
    'LET',
    'FN',
    'SIN',
    'COS',
    'TAN',
    'ATN',
    'EXP',
    'ABS',
    'LOG',
    'SQR',
    'INT',
    'RND',
    'READ',
    'DATA',
    'PRINT',
    'GO',  # TO
    'GOTO',
    'IF',
    'THEN',
    'FOR',
    'TO',
    'STEP',
    'NEXT',
    'DIM',
    'DEF',  # FN
    'GOSUB',
    'RETURN',
    'REM'
]


class LexicalReclassifier:
    def __init__(self, lexical_classifier):
        self.lexical_classifier = lexical_classifier
        self.token = None

    def get_token(self):
        if self.token:
            current_token = self.token
        else:
            current_token = self.lexical_classifier.get_token()
        if current_token.token_class == Token.ID:
            if current_token.value in KEY_WORDS:
                if current_token.value == 'GO':
                    next_token = self.lexical_classifier.get_token()
                    if next_token.value == 'TO':
                        self.token = None
                        current_token.value = 'GOTO'
                    else:
                        self.token = next_token
                elif current_token.value == 'DEF':
                    next_token = self.lexical_classifier.get_token()
                    if next_token.value == 'FN':
                        self.token = None
                        current_token.value = 'DEF FN'
                    else:
                        self.token = next_token
                current_token.token_class = Token.KEY_WORD
            else:
                if len(current_token.value) > 2:
                    # ID has one or two characters
                    current_token.token_class = Token.UNKNOWN
        return current_token
