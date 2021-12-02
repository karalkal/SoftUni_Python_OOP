class countdown_iterator:
    def __init__(self, start):
        self.start = start
        self.result = self.start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.result -= 1

        if self.result < 0:
            raise StopIteration
        return self.result


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
