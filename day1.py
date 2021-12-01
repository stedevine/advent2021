import sys

def get_depth(values):
    count = 0
    current = int(values[0])

    for i in range(1, len(values)):
            next = int(values[i])
            if next > current:
                count += 1

            current = next

    return count


def get_windowed_depth(values):
    window_size = 3
    current = sys.maxsize
    count = 0
    for i in range(len(values) - window_size + 1):
        w = values[i: i + window_size]
        next = sum(list(map(lambda x: int(x), w)))

        if next > current:
            count += 1

        #print("{} {} {} {}".format(current, w, next, count))
        current = next

    return count
        #print(values[i: i + window_size])


with open('day1.txt') as f:
    values = f.readlines()
    increases = get_depth(values)
    print("Number of increases " + str(increases))

    increases = get_windowed_depth(values)
    print("Number of increases " + str(increases))

    #print()
    #print(get_depth(f.readlines())
