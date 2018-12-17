from recognizers.lexical import Lexical
from tkn import Token


class LexicalClassifier:
    def __init__(self, ascii_classifier):
        self.ascii_classifier = ascii_classifier
        self.lexical = Lexical()
        self.current_token = None

    def get_token(self):
        token_value = ''
        try:
            while True:
                if not self.current_token:
                    self.current_token = self.ascii_classifier.get_categorized_char()
                    if self.current_token.value == 'EOF':
                        raise ValueError
                self.lexical.process_atom(self.current_token)
                token_value += self.current_token.value
                self.current_token = None
        except ValueError:
            token = Token(token_class=self.lexical.get_class(),
                          value=token_value.strip(' \n').rstrip(' \n'))
            self.lexical.reset()
            return token
