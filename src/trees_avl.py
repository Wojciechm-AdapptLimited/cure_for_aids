from src import trees_bst as bst


class TreeNode(object):
    def __init__(self, val):
        self.up = None
        self.left_child = None
        self.right_child = None
        self.value = val
        self.height = 1


class AVLTree(object):
    def insert_node(self, arr, parent):
        arr = sorted(list(dict.fromkeys(arr)))
        median = (len(arr) - 1) // 2
        node = TreeNode(arr[median])
        node.up = parent
        if len(arr[:median]) > 0:
            node.left_child = self.insert_node(arr[:median], node)
        if len(arr[median + 1:]) > 0:
            node.right_child = self.insert_node(arr[median + 1:], node)
        node.height = 1 + max(bst.get_height(node.left_child), bst.get_height(node.right_child))
        return node

    def in_order(self, node):
        values = []
        if node.left_child is not None:
            values += self.in_order(node.left_child)
        if node.value is not None:
            values.append(node.value)
        if node.right_child is not None:
            values += self.in_order(node.right_child)
        return values

    def pre_order(self, node):
        values = []
        if node.value is not None:
            values.append(node.value)
        if node.left_child is not None:
            values += self.pre_order(node.left_child)
        if node.right_child is not None:
            values += self.pre_order(node.right_child)
        return values

    def delete_node(self, node: TreeNode, val):
        if node is None:
            return node
        elif node.value > val:
            node.left_child = self.delete_node(node.left_child, val)
        elif node.value < val:
            node.right_child = self.delete_node(node.right_child, val)
        else:
            if node.right_child is None:
                temp = node.left_child
                return temp
            if node.left_child is None:
                temp = node.right_child
                return temp
            temp = bst.successor(node.right_child)
            node.value = temp.value
            node.right_child = self.delete_node(node.right_child, temp.value)
        if node is None:
            return node
        node.height = 1 + max(bst.get_height(node.left_child), bst.get_height(node.right_child))
        balance = bst.get_balance(node)
        if balance > 1 and bst.get_balance(node.left_child) >= 0:
            return self.rotate_right(node)
        if balance < -1 and bst.get_balance(node.right_child) <= 0:
            return self.rotate_left(node)
        if balance > 1 and bst.get_balance(node.left_child) < 0:
            node.left_child = self.rotate_right(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and bst.get_balance(node.right_child) > 0:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)
        return node

    @staticmethod
    def rotate_left(node):
        new_root = node.right_child
        temp = new_root.left_child
        new_root.left_child = node
        node.right_child = temp
        node.height = 1 + max(bst.get_height(node.left_child), bst.get_height(node.right_child))
        new_root.height = 1 + max(bst.get_height(new_root.left_child), bst.get_height(new_root.right_child))
        return new_root

    @staticmethod
    def rotate_right(node):
        new_root = node.left_child
        temp = new_root.right_child
        new_root.right_child = node
        node.left_child = temp
        node.height = 1 + max(bst.get_height(node.left_child), bst.get_height(node.right_child))
        new_root.height = 1 + max(bst.get_height(new_root.left_child), bst.get_height(new_root.right_child))
        return new_root
