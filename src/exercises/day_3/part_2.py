import re


def read_input(filename: str):
    data = {}

    with open(filename, 'r') as f_data:
        line_1 = f_data.readline().split(',')
        line_2 = f_data.readline().split(',')
        inputs_1 = []
        inputs_2 = []
        #data[0][0] = 0

        a = 0
        b = 0
        for x in line_1:
            el = re.split(r'(\d+)', x)
            inputs_1.append((el[0], int(el[1])))
            
            for _i in range(int(el[1])):
                a, b = move(el[0], a, b)
                data[a] = data.setdefault(a, {})
                data[a][b] = data[a].setdefault(b, 0)
                data[a][b] = data[a][b] | 1

        a = 0
        b = 0
        for x in line_2:
            el = re.split(r'(\d+)', x)
            inputs_2.append((el[0], int(el[1])))

            for _i in range(int(el[1])):
                a, b = move(el[0], a, b)
                data[a] = data.setdefault(a, {})
                data[a][b] = data[a].setdefault(b, 0)
                data[a][b] = data[a][b] | 2

    return data, inputs_1, inputs_2


def move(dir, x, y):
    if dir == 'R':
        y += 1
    
    if dir == 'L':
        y -= 1

    if dir == 'U':
        x -= 1

    if dir == 'D':
        x += 1

    return x, y


def get_steps(data, moves, i, j):
    count = 0
    a = 0
    b = 0

    for m in moves:
        for _i in range(m[1]):
            a, b = move(m[0], a, b)
            count += 1
            if a == i and b == j:
                return count


def get_min_steps(data, input_1, input_2):
    min_distance = 1000000

    for i in data.keys():
        for j in data[i].keys():
            if data[i][j] == 3:
                #print('yolo')
                min_distance = min(min_distance, 
                    get_steps(data, input_1, i, j) + 
                    get_steps(data, input_2, i, j))
                
    return min_distance

if __name__ == '__main__':
    data, inputs_1, inputs_2 = read_input('part_2.in')
    print(get_min_steps(data, inputs_1, inputs_2))
    #data[1] = 12
    #data[2] = 2
    #print(compute(data))
