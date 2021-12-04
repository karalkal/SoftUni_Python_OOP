def read_next(*args):
    for each_entry in args:
        for chars in each_entry:
            yield chars


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')
print()
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
