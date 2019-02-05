prime = int(input("Enter a prime number: "))
is_prime = True
for i in range(2, prime):
    if prime % i == 0:
        is_prime = False
        break
print("The number is prime: ", is_prime)   