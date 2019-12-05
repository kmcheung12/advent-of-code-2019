import sys
dayN = """import sys
def preprocess(inputs):
    return inputs

def compute(params):
    return params

if __name__ == '__main__':
    raw = sys.argv[1:]
    params = preprocess(raw)
    output = compute(params)  
    print(output)
"""

if __name__ == '__main__':
    day = sys.argv[1]
    print("Making file day%s.py" % day)
    fn = 'day%s.py' % day
    with open(fn, 'w') as f:
       f.write(dayN)
