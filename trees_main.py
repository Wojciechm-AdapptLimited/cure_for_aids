from src import trees_bst as bst, trees_avl as avl, trees_gen as gen, rep
import sys
import os
import time


def exec_gen(gen_type, size):
    if gen_type == '1':
        return gen.rand(size)
    elif gen_type == '2':
        return gen.std_input()
    else:
        return gen.decreasing(size)


def exec_bst(gen_type):
    size_gen = None
    if gen_type in ['1', '3']:
        while True:
            size_gen = int(input("Enter the length of the array (10 - 999): "))
            if size_gen not in range(10, 1000):
                print("Length of the array should not exceed 999 or be lower than 10")
                continue
            else:
                break
    arr = exec_gen(gen_type, size_gen)
    size_write = len(arr)
    root = bst.TreeNode(arr[0])
    start = time.time_ns()
    for item in arr:
        root = bst.insert_node(root, item)
    end = time.time_ns()
    exec_duration = (end - start) / pow(10, 6)
    file_bst.write("{}; 1; {:.10f}ms\n".format(size_write, exec_duration))
    while True:
        rep.screen_clear()
        print("Select operation type: ")
        op_type = input("1) FIND LARGEST\n"
                        "2) FIND SMALLEST\n"
                        "3) DELETE ELEMENT\n"
                        "4) PRINT PREORDER\n"
                        "5) PRINT INORDER\n"
                        "6) BALANCE TREE\n"
                        "7) DELETE TREE\n"
                        "8) EXIT TO MENU\n"
                        "9) EXIT\n")
        if op_type == '1':
            print(bst.search_max(root))
            time.sleep(5)
        elif op_type == '2':
            start = time.time_ns()
            print(bst.search_min(root))
            end = time.time_ns()
            exec_duration = (end - start) / pow(10, 6)
            file_bst.write("{}; 2; {:.10f}ms\n".format(size_write, exec_duration))
            time.sleep(5)
        elif op_type == '3':
            del_num = int(input("How many would you like to delete: "))
            for i in range(del_num):
                del_val = int(input("Enter value of node you want to delete: "))
                root = bst.delete_node(root, del_val)
        elif op_type == '4':
            print(bst.pre_order(root))
            time.sleep(5)
        elif op_type == '5':
            start = time.time_ns()
            print(bst.in_order(root))
            end = time.time_ns()
            exec_duration = (end - start) / pow(10, 6)
            file_bst.write("{}; 3; {:.10f}ms\n".format(size_write, exec_duration))
            time.sleep(5)
        elif op_type == '6':
            start = time.time_ns()
            root = bst.balance_tree(root)
            end = time.time_ns()
            exec_duration = (end - start) / pow(10, 6)
            file_bst.write("{}; 4; {:.10f}ms\n".format(size_write, exec_duration))
        elif op_type == '7':
            bst.delete_tree(root)
        elif op_type == '8':
            break
        elif op_type == '9':
            sys.exit()
        else:
            continue


def exec_avl(gen_type):
    size_gen = None
    if gen_type in ['1', '3']:
        while True:
            size_gen = int(input("Enter the length of the array (10 - 999): "))
            if size_gen not in range(10, 1000):
                print("Length of the array should not exceed 999 or be lower than 10")
                continue
            else:
                break
    arr = exec_gen(gen_type, size_gen)
    size_write = len(arr)
    tree = avl.AVLTree()
    start = time.time_ns()
    root = tree.insert_node(arr)
    end = time.time_ns()
    exec_duration = (end - start) / pow(10, 6)
    file_avl.write("{}; 1; {:.10f}ms\n".format(size_write, exec_duration))
    while True:
        rep.screen_clear()
        print("Select operation type: ")
        op_type = input("1) FIND LARGEST\n"
                        "2) FIND SMALLEST\n"
                        "3) DELETE ELEMENT\n"
                        "4) PRINT PREORDER\n"
                        "5) PRINT INORDER\n"
                        "6) DELETE TREE\n"
                        "7) EXIT TO MENU\n"
                        "8) EXIT\n")
        if op_type == '1':
            print(bst.search_max(root))
            time.sleep(5)
        elif op_type == '2':
            start = time.time_ns()
            print(bst.search_min(root))
            end = time.time_ns()
            exec_duration = (end - start) / pow(10, 6)
            file_avl.write("{}; 2; {:.10f}ms\n".format(size_write, exec_duration))
            time.sleep(5)
        elif op_type == '3':
            del_num = int(input("How many would you like to delete: "))
            for i in range(del_num):
                del_val = int(input("Enter value of node you want to delete: "))
                root = tree.delete_node(root, del_val)
        elif op_type == '4':
            print(tree.pre_order(root))
            time.sleep(5)
        elif op_type == '5':
            start = time.time_ns()
            print(tree.in_order(root))
            end = time.time_ns()
            exec_duration = (end - start) / pow(10, 6)
            file_avl.write("{}; 3; {:.10f}ms\n".format(size_write, exec_duration))
            time.sleep(5)
        elif op_type == '6':
            bst.delete_tree(root)
        elif op_type == '7':
            break
        elif op_type:
            sys.exit()
        else:
            continue


def menu_gen():
    while True:
        rep.screen_clear()
        print("Select an array type: ")
        array_option = input("1) RANDOM\n2) FROM STANDARD INPUT\n3) DECREASING\n")
        if array_option in ['1', '2', '3']:
            return array_option
        else:
            continue


def menu_tree():
    while True:
        rep.screen_clear()
        print("Select a tree type: ")
        tree_option = input("1) BST\n2) AVL\n")
        if tree_option in ['1', '2']:
            return tree_option
        else:
            continue


def menu_welcome():
    while True:
        rep.screen_clear()
        print("Welcome to the data structures testing platform!")
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
    file_bst, file_avl = None, None
    try:
        file_bst = open("data/bst.txt", 'a', encoding='utf8')
        file_avl = open("data/avl.txt", 'a', encoding='utf8')
        menu_welcome()
        while True:
            rep.screen_clear()
            gen_choice = menu_gen()
            tree_choice = menu_tree()
            if tree_choice == '1':
                exec_bst(gen_choice)
            elif tree_choice == '2':
                exec_avl(gen_choice)
    finally:
        file_bst.close()
        file_avl.close()
