import os
import sys


sys.path.insert(0, '{}/../../'.format(os.path.dirname(os.path.abspath(__file__))))

from modules.ascii_classifier import AsciiClassifier
from modules.ascii_filter import AsciiFilter
from modules.file_system import FileSystem
from modules.lexical_classifier import LexicalClassifier
from modules.lexical_reclassifier import LexicalReclassifier
from modules.parser import Parser


def test_parser():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    fn_in = path + 'bubble_sort.txt'
    fs = FileSystem(file_name=fn_in)
    af = AsciiFilter(file_system=fs)
    ac = AsciiClassifier(ascii_filter=af)
    lc = LexicalClassifier(ascii_classifier=ac)
    lr = LexicalReclassifier(lexical_classifier=lc)
    pr = Parser(lexical_reclassifier=lr)
    fs = None
    af = None
    ac = None
    lc = None
    lr = None

    assert pr.parse()
