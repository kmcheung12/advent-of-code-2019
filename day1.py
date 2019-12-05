import sys
def fuel(mass, acc=0):
    s = int(mass/3) - 2
    if s < 9:
        return s + acc
    else:
        return fuel(s, s + acc)

def compute(params):
    return sum(fuel(p) for p in params)

def preprocess(inputs):
    return map(int, inputs)

if __name__ == '__main__':
    raw = sys.argv[1:]
    params = preprocess(raw)
    output = compute(params)  
    print(output)
