import sorting_alg as algorithm
import sorting_gen as generate
import os
import sys
import time


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def exec_array(arr_type, size):
    if arr_type == '1':
        return generate.increasing(size)
    elif arr_type == '2':
        return generate.decreasing(size)
    elif arr_type == '3':
        return generate.fixed(size)
    elif arr_type == '4':
        return generate.rand(size)
    else:
        return generate.a_shaped(size)


def exec_sort(alg, gen):
    size = int(input("Enter the length of the array: "))
    arr = exec_array(gen, size)
    print(*arr, sep=", ")
    print("\n\n")
    if alg == '1':
        start = time.time_ns()
        algorithm.insertion(arr)
        end = time.time_ns()
        exec_duration = (end - start) / pow(10, 6)
        file_insert.write("{}; {}; {:.10f}ms\n".format(size, int(gen), exec_duration))
    elif alg == '2':
        start = time.time_ns()
        algorithm.shell(arr)
        end = time.time_ns()
        exec_duration = (end - start) / pow(10, 6)
        file_shell.write("{}; {}; {:.10f}ms\n".format(size, int(gen), exec_duration))
    elif alg == '3':
        start = time.time_ns()
        algorithm.selection(arr)
        end = time.time_ns()
        exec_duration = (end - start) / pow(10, 6)
        file_selection.write("{}; {}; {:.10f}ms\n".format(size, int(gen), exec_duration))
    elif alg == '4':
        start = time.time_ns()
        algorithm.heap(arr)
        end = time.time_ns()
        exec_duration = (end - start) / pow(10, 6)
        file_heap.write("{}; {}; {:.10f}ms\n".format(size, int(gen), exec_duration))
    elif alg == '5':
        start = time.time_ns()
        algorithm.quick(arr, 0, len(arr) - 1, 0)
        end = time.time_ns()
        exec_duration = (end - start) / pow(10, 6)
        file_q_right.write("{}; {}; {:.10f}ms\n".format(size, int(gen), exec_duration))
    else:
        start = time.time_ns()
        algorithm.quick(arr, 0, len(arr) - 1, 1)
        end = time.time_ns()
        exec_duration = (end - start) / pow(10, 6)
        file_q_rand.write("{}; {}; {:.10f}ms\n".format(size, int(gen), exec_duration))
    print(*arr, sep=", ")
    time.sleep(10)
    while True:
        screen_clear()
        exec_option = input("1) TRY AGAIN\n2) CHANGE SETTINGS\n3) EXIT\n")
        if exec_option == '1':
            exec_sort(alg, gen)
        elif exec_option == '2':
            break
        elif exec_option == '3':
            sys.exit()
        else:
            continue


def menu_array():
    while True:
        screen_clear()
        print("Select an array type: ")
        array_option = input("1) INCREASING\n2) DECREASING\n3) FIXED\n"
                             "4) RANDOM\n5) A-SHAPED\n6) EXIT\n")
        if array_option in ['1', '2', '3', '4', '5']:
            return array_option
        elif array_option == '6':
            sys.exit()
        else:
            continue


def menu_sort():
    while True:
        screen_clear()
        print("Select the algorithm you would like to test: ")
        sorting_option = input("1) INSERTION SORT\n2) SHELL SORT\n3) SELECTION SORT\n"
                               "4) HEAP SORT\n5) QUICK SORT WITH RIGHT PIVOT\n"
                               "6) QUICK SORT WITH RANDOM PIVOT \n7) EXIT\n")
        if sorting_option in ['1', '2', '3', '4', '5', '6']:
            return sorting_option
        elif sorting_option == '7':
            sys.exit()
        else:
            continue


def menu_welcome():
    while True:
        screen_clear()
        print("Welcome to the sort algorithm testing platform!")
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
    file_insert, file_selection, file_shell, file_heap, file_q_rand, file_q_right = None, None, None, None, None, None
    try:
        file_insert = open("data/insertion.txt", 'a', encoding='utf8')
        file_selection = open("data/selection.txt", 'a', encoding='utf8')
        file_shell = open("data/shell.txt", 'a', encoding='utf8')
        file_heap = open("data/heap.txt", 'a', encoding='utf8')
        file_q_rand = open("data/quick_random.txt", 'a', encoding='utf8')
        file_q_right = open("data/quick_right.txt", 'a', encoding='utf8')
        menu_welcome()
        while True:
            screen_clear()
            alg_option = menu_sort()
            gen_option = menu_array()
            exec_sort(alg_option, gen_option)
    finally:
        file_insert.close()
        file_selection.close()
        file_shell.close()
        file_heap.close()
        file_q_rand.close()
        file_q_right.close()
