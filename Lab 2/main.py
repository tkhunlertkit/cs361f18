import lib

if __name__=='__main__':
    print('Question 1:')
    print(lib.get_stars(8))
    for _ in range(3):
        print(lib.get_star_space(8))
        print(lib.get_star_space(8))
        print(lib.get_stars(8))

    print()

    print('Question 2')
    num = int(input('enter a number: '))
    print(lib.get_ox(num))

    print()

    print('Question 3')
    print(lib.get_median())

    print()

    print('Question 4')
    print(lib.question4())