class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.length = len(sequence)
        self.count = 0
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.number:
            raise StopIteration

        self.idx += 1
        if self.idx == self.length:
            self.idx = 0

        self.count += 1

        return self.sequence[self.idx]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
