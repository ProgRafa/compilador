class Reader:
    def __init__(self, buffer_size, archive_name):
        self.col = 0
        self.size = buffer_size
        self.archive = open(archive_name, 'r').read()
        self.load_buffer()

    def load_buffer(self):
        start = self.col
        end = self.col + self.size
        self.col = end
        self.buffer = list(self.archive[start:end])

    def pull_buffer(self):
        if not self.buffer:
            self.load_buffer()
            return self.pull_buffer()
        else:
            return self.buffer.pop(0)
    
    def push_buffer(self, char):
        self.buffer.insert(0, char)

    def end_of_archive(self):
        if self.col < len(self.archive) or self.buffer:
            return True
        else:
            return False
            