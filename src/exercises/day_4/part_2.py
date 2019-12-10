def is_valid(pwd):
    has_adjacent = False
    pwd_list = [int(x) for x in str(pwd)]

    for i in range(len(pwd_list)):
        if i == 0:
            if pwd_list[i] == pwd_list[i + 1] and \
                pwd_list[i] != pwd_list[i + 2]:
                has_adjacent = True           
        elif i == len(pwd_list) - 1:
            if pwd_list[i] == pwd_list[i - 1] and \
                pwd_list[i] != pwd_list[i - 2]:
                has_adjacent = True
            
            if pwd_list[i] < pwd_list[i - 1]:
                return False
        else:
            if pwd_list[i] == pwd_list[i - 1] and \
                pwd_list[i] != pwd_list[i + 1]:
                if i == 1:
                    has_adjacent = True
                elif pwd_list[i] != pwd_list[i - 2]:
                    has_adjacent = True

            if pwd_list[i] == pwd_list[i + 1] and \
                pwd_list[i] != pwd_list[i - 1]:
                if i == 4:
                    has_adjacent = True
                elif pwd_list[i] != pwd_list[i + 2]:
                    has_adjacent = True
            
            if pwd_list[i] < pwd_list[i - 1]:
                return False

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