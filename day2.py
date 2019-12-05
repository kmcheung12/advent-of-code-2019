import sys
def preprocess(inputs):
    return list(map(int, inputs.split(',')))

def compute(orig):
    for n in range(100):
        for v in range(100):
            params = orig.copy()
            params[1] = n
            params[2] = v
            p = intc(params, 0)
            if p[0] == 19690720:
                print(n, v)
                return 100 * n + v

def intc(pgm, ptr=0):
    oc = pgm[ptr]
    if oc == 1:
        o1 = pgm[pgm[ptr + 1]]
        o2 = pgm[pgm[ptr + 2]]
        pgm[pgm[ptr + 3]] = o1 + o2
        return intc(pgm, ptr + 4)
    elif oc == 2:
        o1 = pgm[pgm[ptr + 1]]
        o2 = pgm[pgm[ptr + 2]]
        pgm[pgm[ptr + 3]] = o1 * o2
        return intc(pgm, ptr + 4)
    elif oc == 99:
        return pgm
    else:
        return 0

if __name__ == '__main__':
    raw = sys.argv[1]
    params = preprocess(raw)
    output = compute(params)  
    print(output)
