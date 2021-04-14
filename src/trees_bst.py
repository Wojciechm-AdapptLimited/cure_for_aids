class TreeNode(object):
    def __init__(self, val):
        self.up = None
        self.left_child = None
        self.right_child = None
        self.value = val
        self.height = 0


def insert_node(node: TreeNode, val):
    new = TreeNode(val)
    parent = node
    if parent is None:
        return new
    else:
        while True:
            if parent.value > val:
                if parent.left_child is None:
                    parent.left_child = new
                    break
                else:
                    parent = parent.left_child
            else:
                if parent.right_child is None:
                    parent.right_child = new
                    break
                else:
                    parent = parent.right_child
    new.up = parent
    return node


def delete_node(node: TreeNode, val):
    if node is None:
        return node
    if node.value > val:
        node.left_child = delete_node(node.left_child, val)
    elif node.value < val:
        node.right_child = delete_node(node.right_child, val)
    else:
        if node.right_child is None:
            temp = node.left_child
            temp.up = node.up
            return temp
        if node.left_child is None:
            temp = node.right_child
            temp.up = node.up
            return temp
        temp = successor(node.right_child)
        node.value = temp.value
        node.right_child = delete_node(node.right_child, temp.value)
    return node


def successor(node):
    cur = node
    while cur.left_child is not None:
        cur = cur.left_child
    return cur


def in_order(node):
    values = []
    if node.left_child is not None:
        values += in_order(node.left_child)
    if node.value is not None:
        values.append(node.value)
    if node.right_child is not None:
        values += in_order(node.right_child)
    return values


def pre_order(node):
    values = []
    if node.value is not None:
        values.append(node.value)
    if node.left_child is not None:
        values += pre_order(node.left_child)
    if node.right_child is not None:
        values += pre_order(node.right_child)
    return values


def search_min(node):
    cur = node
    path = []
    while cur.left_child is not None:
        path.append(cur.value)
        cur = cur.left_child
    path.append(cur.value)
    return path


def search_max(node):
    cur = node
    path = []
    while cur.right_child is not None:
        path.append(cur.value)
        cur = cur.right_child
    path.append(cur.value)
    return path


def delete_tree(node):
    if node is None:
        return node
    if node.left_child:
        delete_tree(node.left_child)
    if node.right_child:
        delete_tree(node.right_child)
    node.value = None


def balance_tree(node):
    if node.left_child:
        rotate_left(node, node.left_child)
    if node.right_child:
        rotate_right(node, node.right_child)


def rotate_left(node_root, node_temp):
    vine = node_temp.right_child
    tail = node_temp.up
    if vine:
        node_temp.right_child = vine.left_child
        if node_temp.right_child:
            node_temp.right_child.up = node_temp
        vine.left_child = node_temp
        vine.up = tail
        node_temp.up = vine
        if tail:
            if tail.left_child == node_temp:
                tail.left_child = vine
            else:
                tail.right_child = vine
        else:
            node_root = vine
    return node_root


def rotate_right(node_root, node_temp):
    vine = node_temp.left_child
    tail = node_temp.up
    if vine:
        node_temp.left_child = vine.right_child
        if node_temp.left_child:
            node_temp.left_child.up = node_temp
        vine.right_child = node_temp
        vine.up = tail
        node_temp.up = vine
        if tail:
            if tail.left_child == node_temp:
                tail.left_child = vine
            else:
                tail.right_child = vine
        else:
            node_root = vine
    return node_root


def get_height(node):
    if node is None:
        return 0
    return node.height


def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left_child) - get_height(node.right_child)
