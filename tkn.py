class Token:
    DIGIT = 'digit'
    LETTER = 'letter'
    SPECIAL = 'special'
    ID = 'id'
    INT = 'int'
    KEY_WORD = 'key_word'
    UNKNOWN = 'unknown'

    def __init__(self, token_class=None, value=None, extra=None):
        self.token_class = token_class
        self.value = value
        self.extra = extra

    def is_digit(self):
        return self.token_class == self.DIGIT or \
               (self.token_class == self.INT and len(self.value) == 1)

    def is_letter(self):
        return self.token_class == self.LETTER or \
               (self.token_class == self.ID and len(self.value) == 1)

    def is_special(self):
        return self.token_class == self.SPECIAL

    def is_id(self):
        return self.token_class == self.ID

    def is_int(self):
        return self.token_class == self.INT

    def is_key_word(self):
        return self.token_class == self.KEY_WORD
