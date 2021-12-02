def fibonacci():
    x = 0
    y = 1
    yield x
    while True:
        x, y = y, x + y
        yield x


generator = fibonacci()
for i in range(5):
    print(next(generator))
generator = fibonacci()
for i in range(1):
    print(next(generator))
