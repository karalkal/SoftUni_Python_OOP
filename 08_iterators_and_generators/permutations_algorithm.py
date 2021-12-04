def permutation(iterable):
    if len(iterable) == 0:
        return []

    if len(iterable) == 1:
        return [iterable]

    result = []

    for i in range(len(iterable)):
        current = iterable[i]
        remaining_elements = iterable[:i] + iterable[i + 1:]  # list of remaining elements

        # Generating all permutations where <current> is first
        for p in permutation(remaining_elements):
            result.append([current] + p)
    return result


# Test code
data = list('123')
for p in permutation(data):
    print(p)
