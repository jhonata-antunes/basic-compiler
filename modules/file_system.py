class FileSystem:
    def __init__(self, file_name):
        self.file = open(file_name, 'rb')

    def read_line(self):
        if not self.file:
            return 'EOF'
        line = self.file.readline()
        if not line:
            self.file.close()
            self.file = None
            return 'EOF'
        return line
