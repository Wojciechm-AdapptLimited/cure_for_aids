from src import dag_alg as alg, rep
import os
import sys
import time


def exec_alg():
    size = int(input("Enter the number of vertices in the graph: "))
    graph = alg.Graph(size)
    while True:
        rep.screen_clear()
        input_option = input("1) RANDOM\n2) FROM STANDARD INPUT\n")
        if input_option == '1':
            graph.gen_adj_matrix()
            break
        elif input_option == '2':
            graph.input_adj_matrix()
            break
        else:
            continue
    graph.gen_adj_list()
    graph.gen_edge_list()
    while True:
        print("\n")
        alg_option = input("1) PRINT ADJACENCY MATRIX\n"
                           "2) PRINT ADJACENCY LIST\n"
                           "3) PRINT EDGE LIST\n"
                           "4) EXECUTE DEEP FIRST SEARCH\n"
                           "5) EXECUTE BREADTH FIRST SEARCH\n"
                           "6) SORT TOPOLOGICALLY VIA DFS - ADJACENCY MATRIX\n"
                           "7) SORT TOPOLOGICALLY VIA DFS - ADJACENCY LIST\n"
                           "8) SORT TOPOLOGICALLY VIA DFS - EDGE LIST\n"
                           "9) SORT TOPOLOGICALLY VIA BFS - ADJACENCY MATRIX\n"
                           "10) SORT TOPOLOGICALLY VIA BFS - ADJACENCY LIST\n"
                           "11) SORT TOPOLOGICALLY VIA BFS - EDGE LIST\n"
                           "12) EXIT\n")
        rep.screen_clear()
        if alg_option == '1':
            graph.print_adj_matrix()
        elif alg_option == '2':
            graph.print_adj_list()
        elif alg_option == '3':
            graph.print_edge_list()
        elif alg_option == '4':
            graph.dfs()
        elif alg_option == '5':
            graph.bfs()
        elif alg_option == '6':
            start = time.time_ns()
            graph.topological_dfs('1')
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_dag.write("{}, 1, 1, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '7':
            start = time.time_ns()
            graph.topological_dfs('2')
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_dag.write("{}, 1, 2, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '8':
            start = time.time_ns()
            graph.topological_dfs('3')
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_dag.write("{}, 1, 3, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '9':
            start = time.time_ns()
            graph.topological_bfs('1')
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_dag.write("{}, 2, 1, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '10':
            start = time.time_ns()
            graph.topological_bfs('2')
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_dag.write("{}, 2, 2, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '11':
            start = time.time_ns()
            graph.topological_bfs('3')
            stop = time.time_ns()
            exec_duration = (stop - start) / pow(10, 6)
            file_dag.write("{}, 2, 3, {:.10f}ms\n".format(size, exec_duration))
        elif alg_option == '12':
            sys.exit()
        else:
            continue


def menu_welcome():
    while True:
        rep.screen_clear()
        print("Welcome to the directed acyclic graphs testing platform!")
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
    file_dag = None
    try:
        file_dag = open("data/dag.txt", 'a', encoding='utf8')
        menu_welcome()
        while True:
            rep.screen_clear()
            exec_alg()
    finally:
        file_dag.close()
