prime = int(input('Enter a number: '))

for i in range(2, prime):
    if prime % i == 0:
        print('this not is prime, it is divisible by: ', i)

print('this is prime')