import json


class ReadFiles:
    """class for read txt file and return a array with the content"""
    def __init__(self, file):
        self.file = file

    def read_files(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                content = [line.rstrip() for line in file]
                if len(content) < 5 or len(content)-content.count('') < 5:
                    return json.dumps({'error': 'The file should with at least five sets of data'})
                return content
        except OSError as e:
            return e
