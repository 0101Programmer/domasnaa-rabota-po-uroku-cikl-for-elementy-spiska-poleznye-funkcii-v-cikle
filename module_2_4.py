numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.pop(0)
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(int(i))
    else:
        not_primes.append(int(i))
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
