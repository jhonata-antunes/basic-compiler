import os
import sys

sys.path.insert(0, '{}/../../'.format(os.path.dirname(os.path.abspath(__file__))))

from modules.ascii_classifier import AsciiClassifier
from modules.ascii_filter import AsciiFilter
from modules.file_system import FileSystem
from modules.lexical_classifier import LexicalClassifier


def test_lexical_classifier():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    fn_in = path + 'test_lexical_classifier_in.txt'
    fn_out = path + 'test_lexical_classifier_out.txt'
    fs = FileSystem(file_name=fn_in)
    af = AsciiFilter(file_system=fs)
    ac = AsciiClassifier(ascii_filter=af)
    lc = LexicalClassifier(ascii_classifier=ac)
    fs = None
    af = None
    ac = None

    with open(fn_out, 'r') as f:
        while True:
            token = lc.get_token()
            if token.value == 'EOF':
                break
            token_class, value = f.readline().rstrip('\n').split(',')
            assert token_class == token.token_class
            assert value == token.value

    assert lc.get_token().value == 'EOF'
    assert lc.get_token().value == 'EOF'
    assert lc.get_token().value == 'EOF'
    assert lc.get_token().value == 'EOF'
