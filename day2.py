def get_distance(data):
    l = 0
    d = 0
    for line in data:

        direction = line.split(' ')[0]
        magnitude = int(line.split(' ')[1])

        if (direction == 'forward'):
            l += magnitude
        elif (direction == 'down'):
            d += magnitude
        else:
            d -= magnitude

    return (l*d)

def get_aim(data):
    aim = 0
    l = 0
    d = 0
    for line in data:
        direction = line.split(' ')[0]
        magnitude = int(line.split(' ')[1])

        if (direction == 'forward'):
            l += magnitude
            d += (aim*magnitude)
        elif (direction == 'down'):
            aim += magnitude
        else:
            aim -= magnitude

    return (l*d)

with open('day2.txt') as f:
    data = f.readlines()
    print(get_distance(data))
    print(get_aim(data))
