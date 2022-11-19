class ReadFiles:
    """class for read txt file and return a array with the content"""
    def __init__(self, file):
        self.file = file

    def read_files(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                return [line.rstrip() for line in file]
        except OSError as e:
            return e

