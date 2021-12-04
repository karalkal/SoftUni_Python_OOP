def possible_permutations(iterable):
    if len(iterable) == 0:
        return []

    if len(iterable) == 1:
        return [iterable]

    result = []

    for i in range(len(iterable)):
        current = iterable[i]
        remaining_elements = iterable[:i] + iterable[i + 1:]  # list of remaining elements

        # Generating all permutations where <current> is first
        for p in possible_permutations(remaining_elements):
            result.append([current] + p)
    return result


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
