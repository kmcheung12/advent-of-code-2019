import sys
def preprocess(inputs):
    return list(map(int, inputs.split(',')))

def compute(orig, i):
    p = intc(params, i, 0)
    return p

def intc(pgm, i=0, ptr=0):
    inst = pgm[ptr]
    oc = inst % 100
    m1 = int(inst / 100) % 10
    m2 = int(inst / 1000) % 100
    m3 = int(inst / 10000)
    if oc == 1:
        o1 = pgm[pgm[ptr + 1]] if m1 == 0 else pgm[ptr + 1]
        o2 = pgm[pgm[ptr + 2]] if m2 == 0 else pgm[ptr + 2]
        if m3 == 0:
            pgm[pgm[ptr + 3]] = o1 + o2
        else:
            pgm[ptr + 3] = o1 + o2
        return intc(pgm, i, ptr + 4)
    elif oc == 2:
        o1 = pgm[pgm[ptr + 1]] if m1 == 0 else pgm[ptr + 1]
        o2 = pgm[pgm[ptr + 2]] if m2 == 0 else pgm[ptr + 2]
        if m3 == 0:
            pgm[pgm[ptr + 3]] = o1 * o2
        else:
            pgm[ptr + 3] = o1 * o2
        return intc(pgm, i, ptr + 4)
    elif oc == 3:
        if m1 == 0:
            pgm[pgm[ptr + 1]] = i
        else:
            pgm[ptr + 1] = i
        return intc(pgm, i, ptr + 2)
    elif oc == 4:
        if m1 == 0:
            o = pgm[pgm[ptr + 1]]
        else:
            o = pgm[ptr + 1]
        print(o)
        return intc(pgm, i, ptr + 2)
    elif oc == 5:
        o1 = pgm[pgm[ptr + 1]] if m1 == 0 else pgm[ptr + 1]
        if m2 == 0:
            if o1 != 0:
                ptr = pgm[pgm[ptr + 2]] 
                return intc(pgm, i, ptr)
            else:
                return intc(pgm, i, ptr + 3)
        else:
            if o1 != 0:
                ptr = pgm[ptr + 2] 
                return intc(pgm, i, ptr)
            else:
                return intc(pgm, i, ptr + 3)
    elif oc == 6:
        o1 = pgm[pgm[ptr + 1]] if m1 == 0 else pgm[ptr + 1]
        if m2 == 0:
            if o1 == 0:
                ptr = pgm[pgm[ptr + 2]] 
                return intc(pgm, i, ptr)
            else:
                return intc(pgm, i, ptr + 3)
        else:
            if o1 == 0:
                ptr = pgm[ptr + 2] 
                return intc(pgm, i, ptr)
            else:
                return intc(pgm, i, ptr + 3)
    elif oc == 7:
        o1 = pgm[pgm[ptr + 1]] if m1 == 0 else pgm[ptr + 1]
        o2 = pgm[pgm[ptr + 2]] if m2 == 0 else pgm[ptr + 2]
        if m3 == 0:
            pgm[pgm[ptr + 3]] = 1 if o1 < o2 else 0
        else:
            pgm[ptr + 3] = 1 if o1 < o2 else 0
        return intc(pgm, i, ptr + 4)
    elif oc == 8:
        o1 = pgm[pgm[ptr + 1]] if m1 == 0 else pgm[ptr + 1]
        o2 = pgm[pgm[ptr + 2]] if m2 == 0 else pgm[ptr + 2]
        if m3 == 0:
            pgm[pgm[ptr + 3]] = 1 if o1 == o2 else 0
        else:
            pgm[ptr + 3] = 1 if o1 < o2 else 0
        return intc(pgm, i, ptr + 4)
    elif oc == 99:
        return pgm
    else:
        return 0

if __name__ == '__main__':
    raw = sys.argv[1]
    params = preprocess(raw)
    output = compute(params, 5)
    print(output)
