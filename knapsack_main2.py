from src import knapsack_alg as alg, rep
import os
import sys
import time


def exec_alg():
    file_elements = None
    elements = []
    try:
        file_elements = open("data/elements.txt", 'r')
        lines = file_elements.readlines()
        capacity = int(lines[0])
        number = int(lines[1])
        for line in range(2,number+2):
            line = lines[line].strip().split()
            elements.append((int(line[1]), int(line[0])))
    finally:
        file_elements.close()
    while True:
        print("\n")
        alg_option = input("1) BRUTE FORCE ALGORITHM\n"
                           "2) DYNAMIC PROGRAMMING BASED ALGORITHM\n"
                           "3) EXIT\n")
        rep.screen_clear()
        if alg_option == '1':
            start = time.time_ns()
            print(alg.brute_force(number, capacity, elements))
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 9)
            file_knapsack.write("{}, {}, 1, {:.10f}s\n".format(number, capacity, exec_duration))
        elif alg_option == '2':
            start = time.time_ns()
            print(alg.dynamic(number, capacity, elements))
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 9)
            file_knapsack.write("{}, {}, 2, {:.10f}s\n".format(number, capacity, exec_duration))
        elif alg_option == '3':
            sys.exit()
        else:
            continue


def menu_welcome():
    while True:
        rep.screen_clear()
        print("Welcome to the knapsack problem solving algorithms testing platform!")
        welcome_option = input("1) CONTINUE\n2) EXIT\n")
        if welcome_option == '1':
            break
        elif welcome_option == '2':
            sys.exit()
        else:
            continue


if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    file_knapsack = None
    try:
        file_knapsack = open("data/knapsack.txt", 'a', encoding='utf8')
        menu_welcome()
        while True:
            rep.screen_clear()
            exec_alg()
    finally:
        file_knapsack.close()
