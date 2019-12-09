import math

def read_input(filename: str, data: list):
    with open(filename, 'r') as f_data:
        line = f_data.readline()
        while line:
            data.append(int(line))
            line = f_data.readline()

def get_required_fuel(mass: int):
    return math.floor(mass / 3) - 2

def get_fuel_content_upper(data: list):
    return sum([get_required_fuel(x) for x in data])

if __name__ == '__main__':
    data = []
    read_input('part_1.in', data)
    print(get_fuel_content_upper(data))
