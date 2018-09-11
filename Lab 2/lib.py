def get_stars(num):
    return '*' * num

def get_star_space(num):
    return '*' + ' ' * (num - 2) + '*'

def get_ox(num):
    ret = ''
    for i in range(1, num + 1):
        ret += 'O' * i + 'X' * (num-i) + '\n'

    return ret

def get_median():
    continue = True

    while continue