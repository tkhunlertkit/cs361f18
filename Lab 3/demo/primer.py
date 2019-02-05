class Primer(object):

    def __init__(self, prime_limit):
        self.prime_limit = prime_limit

    def generate(self, num_prime):
        num_prime_so_far = 1
        for i in range(2, self.prime_limit+1):
            if num_prime_so_far > num_prime:
                return
            if self.check_prime(i):
                num_prime_so_far += 1
                yield i

    @staticmethod
    def check_prime(val):
        for i in range(2, val):
            if val % i == 0:
                return False

        return True
