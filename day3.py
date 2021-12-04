def get_power(data):
    return get_most_common_digits(data)

def get_most_common_digits(data):
    binary_answer = ''
    width = len(data[0].strip())
    for offset in range(0, width):
        digits_sum = 0
        for d in data:
            digits_sum += int(d[offset])

        if digits_sum > len(data)/2:
            binary_answer += '1'
        else:
            binary_answer += '0'

    gama = binary_answer

    epsilon = ''.join(list(map(lambda a: '1' if a=='0' else '0', gama)))

    return int(gama, 2)*int(epsilon, 2)


def get_most_common_at_position(data, position):
    digits_sum = 0
    for d in data:
        digits_sum += int(d[position])

    if digits_sum >= len(data)/2:
        return '1'

    return '0'

def get_least_common_at_position(data, position):
    return '1' if get_most_common_at_position(data, position) == '0' else '0'

def find_number(data, get_common):
    position = 0
    while True:
        for position in range(0, len(data[0])):

            most_common = get_common(data,position)
            # filter to only include the data with this value
            # at this position
            data = list(filter(lambda x: x[position]==most_common, data))
            if len(data) == 1:
                return int(''.join(data), 2)

def find_oxygen(data):
    return find_number(data, get_most_common_at_position)

def find_co2(data):
    return find_number(data, get_least_common_at_position)

with open('day3.txt') as f:
    data = f.readlines()
    print(get_power(data))
    print(find_oxygen(data)*find_co2(data))
