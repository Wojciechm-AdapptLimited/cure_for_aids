import random
import math


# generating an array with random elements
def rand(size):
    return [random.randint(-100, 100) for _ in range(size)]


# generating an array with increasing elements, starting with random number
def increasing(size):
    num = random.randint(-100, 100)
    return [i for i in range(num, num + size)]


# generating an array with decreasing elements, starting with random number
def decreasing(size):
    num = random.randint(-100, 100)
    return [i for i in range(num, num - size, -1)]


# generating an array filled with one random number
def fixed(size):
    num = random.randint(-100, 100)
    return [num] * size


# generating an array increasing to the middle, decreasing after it, starting with random number
def a_shaped(size):
    mid_index = math.ceil(size / 2)
    num = random.randint(-100, 100)
    arr = [i for i in range(num, num + mid_index)]
    mid = arr[-1]
    for i in range(mid_index, size):
        arr.append(mid - (i - mid_index + 1))
    return arr
