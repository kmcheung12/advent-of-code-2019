import sys
def node(f, t):
    return {f: t}

def preprocess(inputs):
    return list(map(lambda x: x.split(')'), inputs))

def compute(params):
    graph = {}
    for pair in params:
        a = pair[0]
        b = pair[1]
        graph.update(node(b, a))
    orbit = 0
    you = graph.get('YOU')
    yl = []
    san = graph.get('SAN')
    sl = []
    while you:
        yl.append(you)
        you = graph.get(you)

    while san:
        sl.append(san)
        san = graph.get(san)

    print(len(yl))
    print(len(sl))
    print(len(set(yl).intersection(set(sl))))
    #for k in graph:
    #    centre = graph.get(k)
    #    print('%s)%s: ' % (centre, k))
    #    while centre:
    #        orbit += 1
    #        centre = graph.get(centre)
    return orbit

if __name__ == '__main__':
    raw = sys.argv[1:]
    params = preprocess(raw)
    output = compute(params)
    print(output)
