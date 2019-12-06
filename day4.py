def compute(param):
    count = 0
    for i in range(param[0], param[1] + 1):
        s = str(i)
        if has_n_adj(s, 2) and \
            ever_increasing(s):
            count += 1
    return count

inputs = [367479,893698]


def group_by(s):
    l = []
    prev = ''
    can = ''
    for i in range(len(s)):
        c = s[i]
        if c != prev:
            if can:
                l.append(can)
            prev = c
            can = c
        else:
            can += c
    l.append(can)
    return l


def has_n_adj(s, n=2):
    l = group_by(s)
    return any(len(e) == n for e in l)


def ever_increasing(s):
    for i in range(len(s) - 1):
        c = s[i]
        if int(c) > int(s[i + 1]):
            return False
    return True

if __name__ == '__main__':
    print(compute(inputs))
