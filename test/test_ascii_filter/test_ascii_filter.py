import os

from modules.ascii_filter import AsciiFilter
from modules.file_system import FileSystem


def test_ascii_filter():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    fn = path + 'test_ascii_filter_in.txt'
    fs = FileSystem(fn)
    af = AsciiFilter(fs)
    fs = None

    with open(fn, 'r') as f:
        for i in range(4):
            line = f.readline()
            for j in range(len(line)):
                assert line[j] == af.get_char()

    assert af.get_char() == 'EOF'
    assert af.get_char() == 'EOF'
    assert af.get_char() == 'EOF'
    assert af.get_char() == 'EOF'
