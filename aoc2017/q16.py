from aocd import data

def parse_data(data, mod=16):
    S = 0
    ops = []
    for op in data.split(','):
        if op.startswith('s'):
            n = int(op[1:])
            S += n
        elif op.startswith('x'):
            a, b = op[1:].split('/')
            a = (int(a) - S) % mod
            b = (int(b) - S) % mod
            ops.append(('x', a, b))
        elif op.startswith('p'):
            a, b = op[1:].split('/')
            ops.append(('p', a, b))
    ops.append(('s', S % mod, S % mod))
    return ops

def run(data, d, n=1):
    mod = len(d)
    ops = parse_data(data, mod=mod)
    seen = {}
    while n:
        s = ''.join(d)
        if s in seen:
            r = seen[s] - n
            n %= r
            seen.clear()
            continue
        seen[s] = n
        for i, a, b in ops:
            if i == 'x':
                d[a], d[b] = d[b], d[a]
            elif i == 'p':
                ai = d.index(a)
                bi = d.index(b)
                d[ai], d[bi] = d[bi], d[ai]
            elif i == 's':
                d[:] = d[(mod-a):] + d[:(mod-a)]
        n -= 1
    return ''.join(d)

assert run(data='s1,x3/4,pe/b', d=list('abcde')) == 'baedc'
assert run(data='s1,x3/4,pe/b', d=list('abcde'), n=2) == 'ceadb'

d = list('abcdefghijklmnop')
print(run(data, d))  # part a: fgmobeaijhdpkcln
print(run(data, d, n=1000000000-1))  # part b: lgmkacfjbopednhi
