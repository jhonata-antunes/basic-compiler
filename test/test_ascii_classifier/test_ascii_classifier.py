import os
import sys

sys.path.insert(0, '{}/../../'.format(os.path.dirname(os.path.abspath(__file__))))

import pytest

from modules.ascii_classifier import AsciiClassifier
from modules.ascii_filter import AsciiFilter
from modules.file_system import FileSystem


def test_ascii_classifier():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    fn_in = path + 'test_ascii_classifier_in.txt'
    fn_out = path + 'test_ascii_classifier_out.txt'
    fs = FileSystem(fn_in)
    af = AsciiFilter(fs)
    ac = AsciiClassifier(af)
    fs = None
    af = None

    with open(fn_out, 'r') as f:
        while True:
            token = ac.get_categorized_char()
            if token.value == 'EOF':
                break
            assert token.token_class == f.readline().rstrip('\n')

    assert ac.get_categorized_char().value == 'EOF'
    assert ac.get_categorized_char().value == 'EOF'
    assert ac.get_categorized_char().value == 'EOF'
    assert ac.get_categorized_char().value == 'EOF'
