import os

from modules.file_system import FileSystem


def test_file_system():
    path = os.path.dirname(os.path.abspath(__file__)) + '/'
    fn = path + 'test_file_system_in.txt'
    fs = FileSystem(fn)

    with open(fn, 'rb') as f:
        for i in range(3):
            line = fs.read_line()
            assert line == f.readline()

    assert fs.read_line() == 'EOF'
    assert fs.read_line() == 'EOF'
    assert fs.read_line() == 'EOF'
    assert fs.read_line() == 'EOF'
