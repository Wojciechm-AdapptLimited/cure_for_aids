from src import cycles_alg as cycles, rep
import os
import sys
import time
import copy


def exec_alg():
    size = int(input("Enter the number of vertices in the graph: "))
    saturation = float(input("Enter the saturation of edges of the graph: "))
    graph = cycles.Graph(size, saturation)
    while True:
        rep.screen_clear()
        input_option = input("1) HAMILTONIAN\n2) NOT HAMILTONIAN\n3) FROM STANDARD INPUT\n")
        if input_option == '1':
            graph.gen_hamiltonian()
            break
        elif input_option == '2':
            graph.gen_hamiltonian()
            graph.gen_not_hamiltonian()
            break
        elif input_option == '3':
            edges = int(input("Enter the number of edges: "))
            graph.input_graph(edges)
            break
        else:
            continue
    rep.screen_clear()
    while True:
        print("\n")
        alg_option = input("1) PRINT GRAPH\n"
                           "2) PRINT EULER PATH\n"
                           "3) PRINT HAMILTONIAN PATH\n"
                           "4) EXIT\n")
        rep.screen_clear()
        if alg_option == '1':
            graph.print_graph()
        elif alg_option == '2':
            g_copy = copy.deepcopy(graph)
            start = time.time_ns()
            g_copy.print_euler_tour()
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_cycles.write("{}, 1, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '3':
            start = time.time_ns()
            graph.print_hamiltonian_cycle()
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_cycles.write("{}, 2, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '4':
            sys.exit()
        else:
            continue


def menu_welcome():
    while True:
        rep.screen_clear()
        print("Welcome to the cycle algorithms testing platform!")
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
    file_cycles = None
    try:
        file_cycles = open("data/cycles.txt", 'a', encoding='utf8')
        menu_welcome()
        while True:
            rep.screen_clear()
            exec_alg()
    finally:
        file_cycles.close()
