import sys

def invert_bits(inp):
    return ''.join([str(abs(int(x)-1)) for x in list(inp)])

def get_most_common_bit(inp):
    data = [0 for x in range(len(list(inp[0])))]
    for l in inp:
        l = list(l)
        i = 0
        while i < len(l):
            data[i] = data[i] + int(l[i])
            i+=1
    gamma = ''
    for d in data:
        g = 1 if (d + d)>len(inp) else 0
        #e = 0 if g == 1 else 1
        gamma = gamma + str(g)
        #epsilon = epsilon + str(e)
    return gamma

def filter_on_index(arr, index, bit):
    retval = []
    for r in arr:
        if list(r)[index] == bit:
            retval.append(r)
    return retval



if __name__ == '__main__':
    with open(sys.argv[1], mode='r') as h:
        inp = h.read().splitlines()
    # Part One
    data = [0 for x in range(len(list(inp[0])))]
    for l in inp:
        l = list(l)
        i = 0
        while i < len(l):
            data[i] = data[i] + int(l[i])
            i+=1
    gamma, epsilon = '', ''
    for d in data:
        g = 1 if (d + d)>len(inp) else 0
        e = 0 if g == 1 else 1
        gamma = gamma + str(g)
        epsilon = epsilon + str(e)

    gamma_dec, epsilon_dec = int(gamma, 2), int(epsilon, 2)

    print(f'Part One: {gamma_dec*epsilon_dec}')
    # Part Two
    print(f'{gamma}, {invert_bits(gamma)}')
    
    exit()
    oxygen_matches, co2_matches = inp.copy(), inp.copy()
    
        
        
        
    
    exit()
