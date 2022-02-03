import random


def rand(size):
    return [random.randint(0, 2 * size) for _ in range(size)]


def decreasing(size):
    num = random.randint(size, 2 * size)
    return [i for i in range(num, num - size, -1)]


def std_input():
    while True:
        data = input("Enter up to ten numbers: ").strip().split()
        if len(data) > 10:
            print("Too many elements! Try again")
            continue
        else:
            flag = True
            for item in data:
                try:
                    if int(item) < 0:
                        flag = False
                        break
                except ValueError:
                    flag = False
                    break
            if flag:
                break
            else:
                print("You can only enter positive integers!")
                continue
    return list(map(int, data))
