


if __name__ == '__main__':
    with open('input', mode='r') as h:
        inp = h.readlines()
    inp = [int(x) for x in inp]
    # Part One
    mem = inp[0]
    c = 0
    for i in inp:
        if i > mem:
            c+=1
        mem = i
    print(f'Part One: {str(c)}')


    # Part Two
    mem = None
    c = 0
    i = 2
    while i < len(inp):
        cur = sum([inp[i-2], inp[i-1], inp[i]])
        
        if mem is not None and cur > mem:
            c+=1
        mem = cur
        
        
        i+=1
    print(f'Part Two: {str(c)}')


