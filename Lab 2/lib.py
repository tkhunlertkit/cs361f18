import statistics

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
    num = []

    while True:
        curr_num = int(input('enter a number: '))
        if curr_num < 0:
            break
        
        num.append(curr_num)
    
    return statistics.median(num)


def question4():
    return freq(input('enter a phrase: '))

def freq(phrase):
    stat = {}
    for s in phrase:
        if s not in stat:
            stat[s] = 0
        stat[s] += 1
    
    return stat