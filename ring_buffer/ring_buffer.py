class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.buffer = [None] * capacity
        self.length = 0

    def append(self, item):
        self.buffer[self.current] = item
        self.current += 1
        self.current = self.current % self.capacity
        if self.length < self.capacity:
            self.length += 1

    def get(self):
        return self.buffer[:self.length]
