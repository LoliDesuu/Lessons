numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
numbers.remove(1)

for elem in numbers:
    is_prime = True
    for divinity in range(2, elem):
        if elem % divinity == 0:
            is_prime = False
            not_primes.append(elem)
            break

    if (is_prime != False):
        primes.append(elem)

print(primes)
print(not_primes)

