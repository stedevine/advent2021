def get_input(data):
    numbers = data[0].strip().split(',')
    numbers = list(map(lambda x: int(x.strip()), numbers))

    grids = []
    i = 1
    while (i < len(data)):
        if (data[i] != ''):

            grids.append(data[i:i+5])
            i += 4
        i += 1

    for g in grids:
        for i in range(0,5):
            g[i] = g[i].replace('  ',' ')
            g[i] = g[i].split(' ')
            g[i] = list(map(lambda x: int(x.strip()), g[i]))


    return numbers, grids


def apply_number(number, grids):
    for g in grids:
        for r in range(0,5):
            for c in range(0,5):
                if g[r][c] == number:
                    g[r][c] = -1

def check_grids(grids):

    for g in grids:
        # check rows
        for r in range(0,5):
            if (sum(g[r]) == -5):
                return g

        for c in range(0,5):
            total = 0
            for r in range(0,5):
                total += g[r][c]
            if total == -5:
                return g

def score(grid, number):
    total = 0
    for r in range(0,5):
        for c in range(0,5):
            if grid[r][c] > 0:
                total += grid[r][c]

    return total*number


def get_winning_board_score(data):
    numbers, grids = get_input(data)
    for n in numbers:
        apply_number(n, grids)
        g = check_grids(grids)
        if g != None:
            return score(g,n)

with open('day4-test.txt') as f:
    data = f.readlines()
    data = list(map(lambda d: d.strip(), data))
    print(get_winning_board_score(data))
