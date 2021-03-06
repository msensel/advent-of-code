from aocd import data

test_data = '''\
..#
#..
...'''

def parse_data(data):
    lines = data.splitlines()
    s = len(lines)//2
    grid = {}
    for row, line in enumerate(lines, -s):
        for col, char in enumerate(line, -s):
            grid[col-row*1j] = char
    return grid

def run(data, n_iterations, mutation=1):
    mutation = {
        1: {'#': '.', '.': '#'},
        2: {'#': 'F', 'F': '.', '.': 'W', 'W': '#'},
    }[mutation]
    grid = parse_data(data)
    p, v = 0, 1j
    n_infected = 0
    for i in range(n_iterations):
        s = grid.get(p, '.')
        if s == '.':
            v *= 1j
        elif s == 'W':
            pass
        elif s == 'F':
            v *= -1
        else:
            v *= -1j
        grid[p] = mutation[s]
        if grid[p] == '#':
            n_infected += 1
        p += v
    return n_infected

assert run(test_data, n_iterations=7) == 5
assert run(test_data, n_iterations=70) == 41
assert run(test_data, n_iterations=10000) == 5587
assert run(test_data, n_iterations=100, mutation=2) == 26
assert run(test_data, n_iterations=10000000, mutation=2) == 2511944

print(run(data, n_iterations=10000))  # part a: 5259
print(run(data, n_iterations=10000000, mutation=2))  # part b: 2511722
