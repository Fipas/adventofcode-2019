import math

def read_input(filename: str):
    data = []
    with open(filename, 'r') as f_data:
        data = f_data.read().split(',')

    return [int(x) for x in data]
        
def compute(data: list):
    i = 0
    while data[i] != 99:
        intcode = data[i]
        x = data[data[i+1]]
        y = data[data[i+2]]
        r_i = data[i+3]

        if intcode == 1:
            data[r_i] = x + y

        if intcode == 2:
            data[r_i] = x * y

        i += 4

    return data[0]

if __name__ == '__main__':
    input_size = len(read_input('part_1.in'))
    for i in range(input_size):
        for j in range(input_size):
            data = read_input('part_1.in')
            data[1] = i
            data[2] = j
            if compute(data) == 19690720:
                print('{} {}'.format(i, j))
                exit()
