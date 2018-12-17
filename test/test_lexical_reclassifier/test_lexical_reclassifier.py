import os
import sys


sys.path.insert(0, '{}/../../'.format(os.path.dirname(os.path.abspath(__file__))))

from modules.ascii_classifier import AsciiClassifier
from modules.ascii_filter import AsciiFilter
from modules.file_system import FileSystem
from modules.lexical_classifier import LexicalClassifier
from modules.lexical_reclassifier import LexicalReclassifier


def test_lexical_reclassifier():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    fn_in = path + 'test_lexical_reclassifier_in.txt'
    fn_out = path + 'test_lexical_reclassifier_out.txt'
    fs = FileSystem(file_name=fn_in)
    af = AsciiFilter(file_system=fs)
    ac = AsciiClassifier(ascii_filter=af)
    lc = LexicalClassifier(ascii_classifier=ac)
    lr = LexicalReclassifier(lexical_classifier=lc)
    fs = None
    af = None
    ac = None
    lc = None

    with open(fn_out, 'r') as f:
        while True:
            token = lr.get_token()
            if token.value == 'EOF':
                break
            token_class, value = f.readline().rstrip('\n').split(',')
            if value == 'GO':
                f.readline().rstrip('\n').split(',')
                value = 'GOTO'
            elif value == 'DEF':
                f.readline().rstrip('\n').split(',')
                value = 'DEF FN'
            assert token_class == token.token_class
            assert value == token.value

    assert lr.get_token().value == 'EOF'
    assert lr.get_token().value == 'EOF'
    assert lr.get_token().value == 'EOF'
    assert lr.get_token().value == 'EOF'
