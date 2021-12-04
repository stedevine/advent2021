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

def updated_grids(grids, number, winning_grids):

    for i in range(0, len(grids)):
        # winning_grids holds a tuple, index of the winning board
        # and its score.
        # Once the grid has won - don't recalculate the score (it will change - as the game goes on the grids are updated and their final score will change)
        if len(list(filter(lambda a:a[0] == i,winning_grids))) == 0:
            g = grids[i]
            row_match = False
            col_match = False

            # check rows
            for r in range(0,5):
                if (sum(g[r]) == -5):
                    row_match = True
                    continue
            # check columns
            for c in range(0,5):
                total = 0
                for r in range(0,5):
                    total += g[r][c]
                if total == -5:
                    col_match = True
                    continue

            # This is the first time this grid has won
            # put it on the list with its score.
            if (row_match or col_match):
                winning_grids.append((i,score(grids[i],number)))

    return winning_grids



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

def get_last_board(data):
    numbers, grids = get_input(data)
    # Track every grid that wins and the score
    # it has when it wins
    winning_grids = []
    for n in numbers:
        #print(n)
        apply_number(n, grids)
        updated_grids(grids, n, winning_grids)

    # Game is over, what was the score on the last board that won?
    return winning_grids[-1][1]


with open('day4.txt') as f:
    data = f.readlines()
    data = list(map(lambda d: d.strip(), data))
    print(get_winning_board_score(data))
    print(get_last_board(data))
