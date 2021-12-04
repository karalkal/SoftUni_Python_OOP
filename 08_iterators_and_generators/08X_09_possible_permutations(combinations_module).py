from itertools import permutations

def possible_permutations(iterable):
    for each_p in permutations(iterable):
        yield list(each_p)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]

result = possible_permutations([1, 2, 3])
print(next(result))
