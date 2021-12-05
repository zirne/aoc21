import sys


if __name__ == '__main__':
    with open(sys.argv[1], mode='r') as h:
        inp = h.readlines()
#    inp = [int(x) for x in inp]
    # Part One
    h,d = 0,0
    for i in inp:
        dire, dist = i.split(' ')
        dist = int(dist)
        if dire == 'forward':
            h = h + dist
        elif dire in ['up', 'down']:
            if dire == 'up':
                d = d - dist
            else:
                d = d + dist
        else:
            print(f'WTF? {i}')

    res = h*d
    print(f'Part One: {res}')

    # Part Two
    h,d,aim = 0,0,0
    for i in inp:
        dire, dist = i.split(' ')
        dist = int(dist)
        if dire == 'forward':
            h = h + dist
            d = d + (aim*dist)
        elif dire in ['up', 'down']:
            if dire == 'up':
#                d = d - dist
                aim = aim - dist
            else:
#                d = d + dist
                aim = aim + dist
        else:
            print(f'WTF? {i}')
#        print(f'h,d,aim: {h},{d},{aim}')
    res = h*d
    print(f'Part Two: {res}')


    exit()

