def get_primes(numbers):
    for number in numbers:
        is_prime = True
        for smaller in range(2, number):
            if number % smaller == 0:
                is_prime = False
                break
        if is_prime and number > 1:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
