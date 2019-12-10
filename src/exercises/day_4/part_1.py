def is_valid(pwd):
    digit = 0
    has_adjacent = False
    divisor = 100000

    for _i in range(6):
        next_digit = pwd // divisor
        pwd = pwd % divisor
        divisor = divisor // 10

        if next_digit < digit:
            return False

        if next_digit == digit:
            has_adjacent = True

        digit = next_digit

    return has_adjacent


def count_valid(start, end):
    count = 0
    for i in range(start, end + 1):
        if is_valid(i):
            count += 1

    return count


if __name__ == '__main__':
    print(is_valid(111111))
    print(is_valid(223450))
    print(is_valid(123789))
    print(count_valid(168630, 718098))