import sys
def preprocess(inputs):
    return inputs[-1]

def compute(params, w, h):
    pixels = len(params)
    p = w*h
    l = pixels // p
    layers = []
    counts = []
    for i in range(l):
        layer = params[i*p: i*p + p]
        layers.append(layer)
        counts.append((layer.count('0'), layer.count('1'), layer.count('2')))
    final_img = ''
    for i in range(p):
        for layer in layers:
            tmp_pix = layer[i]
            if tmp_pix is not '2':
                break
        final_img += tmp_pix
    for i in range(h):
        print(''.join(list(map(lambda x: 'XX' if x == '1' else '  ' ,final_img[i*w: i*w+w]))))
    return final_img

if __name__ == '__main__':
    raw = sys.argv[1:]
    params = preprocess(raw)
    w = 25
    h = 6
    output = compute(params, w, h)
