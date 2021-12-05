def more_than_two_points(data):
    w = 1000
    h = 1000

    grid = [[0 for x in range(w)] for y in range(h)]

    for d in data:
        start, end = d.split(' -> ')

        start_x, start_y = list(map(lambda a: int(a),start.split(',')))
        end_x, end_y = list(map(lambda a: int(a),end.split(',')))
        # is vertical
        if (start_x == end_x):
            print('{} vertical'.format(d))
            # increment the values in the grid
            if (start_y > end_y):
                start_y, end_y = end_y, start_y
            if (end_y > start_y):
                for i in range(start_y, end_y+1):
                    grid[i][start_x] += 1

        elif (start_y == end_y):
            print('{} horizontal'.format(d))
            if (start_x > end_x):
                start_x, end_x = end_x, start_x
            # increment the values in the grid
            for i in range(start_x, end_x+1):
                grid[start_y][i] += 1

    print()
    print_grid(grid)
    count = 0
    for r in range(0,w):
        for c in range(0,h):
            if grid[r][c] > 1:
                count += 1


        # is horizontal


    return count

def print_grid(grid):
    for g in grid:
        line = ''.join(list(map(lambda a: str(a), g)))
        line = line.replace('0','.')
        print(line)
        #print(''.join(g))

with open('day5.txt') as f:
    data = f.readlines()
    data = list(map(lambda d: d.strip(), data))
    print(more_than_two_points(data))
    #print(get_winning_board_score(data))
    #print(get_last_board(data))
