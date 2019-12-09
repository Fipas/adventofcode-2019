import math

def read_input(filename: str, data: list):
    with open(filename, 'r') as f_data:
        line = f_data.readline()
        while line:
            data.append(int(line))
            line = f_data.readline()

def get_required_fuel(mass: int):
    fuel = math.floor(mass / 3) - 2
    if fuel < 0:
        return 0
    else:
        return fuel + get_required_fuel(fuel)

def get_fuel_content_upper(data: list):
    return sum([get_required_fuel(x) for x in data])

if __name__ == '__main__':
    data = []
    read_input('part_2.in', data)
    print(get_fuel_content_upper(data))
