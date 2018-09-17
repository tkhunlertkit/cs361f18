from primer import Primer

if __name__ == '__main__':
    prime = Primer(20)
    for p in prime.generate(9):
        print(p)