import sys
def preprocess(inputs):
    return [e.split(',') for e in inputs]

def compute(paths):
    grids = []
    for p in paths:
        g = []
        x = 0
        y = 0
        init = make_pt(x, y)
        g.append(init)
        for d in p:
            v = d[0]
            s = int(d[1:])
            if v == 'R':
                for ss in range(s):
                    x += 1
                    g.append(make_pt(x, y))
            elif v == 'L':
                for ss in range(s):
                    x -= 1
                    g.append(make_pt(x, y))
            elif v == 'U':
                for ss in range(s):
                    y += 1
                    g.append(make_pt(x, y))
            elif v == 'D':
                for ss in range(s):
                    y -= 1
                    g.append(make_pt(x, y))
        grids.append(g)
    return grids

def make_pt(x, y):
    return (x, y)

def man_dist(x, y):
    return abs(x) + abs(y)

if __name__ == '__main__':
    raw = sys.argv[1:]
    params = preprocess(raw)
    output = compute(params)  
    g1 = output[0]
    g2 = output[1]
    intx = set(g1).intersection(g2)
    origin = make_pt(0, 0)
    p1 = sorted(man_dist(p[0], p[1]) for p in intx)[1]
    print(p1)

    combined_dists = [ g1.index(i) + g2.index(i) for i in intx]
    p2 = sorted(combined_dists)[1]
    print(p2)
