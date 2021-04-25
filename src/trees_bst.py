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
            elif parent.value < val:
                if parent.right_child is None:
                    parent.right_child = new
                    break
                else:
                    parent = parent.right_child
            else:
                break
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
        if node.right_child is None and node.left_child is None:
            node = None
            return node
        if node.right_child is None:
            temp = node.left_child
            temp.up = node.up
            node = None
            return temp
        if node.left_child is None:
            temp = node.right_child
            temp.up = node.up
            node = None
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


def log_2(x):
    y = 1
    x >>= 1
    while x > 0:
        y <<= 1
        x >>= 1
    return y


def balance_tree(node: TreeNode):
    n = 0
    p = node
    while p is not None:
        if p.left_child is not None:
            node = rotate_right(node, p)
            p = p.up
        else:
            n += 1
            p = p.right_child
    s = n + 1 - log_2(n + 1)
    p = node
    for i in range(s):
        node = rotate_left(node, p)
        p = p.up.right_child
    n -= s
    while n > 1:
        n //= 2
        p = node
        for i in range(int(n)):
            node = rotate_left(node, p)
            p = p.up.right_child
    return node


def rotate_left(node: TreeNode, a: TreeNode):
    b = a.right_child
    parent = a.up
    if b is not None:
        a.right_child = b.left_child
        if a.right_child is not None:
            a.right_child.up = a
        b.left_child = a
        b.up = parent
        a.up = b
        if parent is not None:
            if parent.left_child == a:
                parent.left_child = b
            else:
                parent.right_child = b
        else:
            node = b
    return node


def rotate_right(node: TreeNode, a: TreeNode):
    b = a.left_child
    parent = a.up
    if b is not None:
        a.left_child = b.right_child
        if a.left_child is not None:
            a.left_child.up = a
        b.right_child = a
        b.up = parent
        a.up = b
        if parent is not None:
            if parent.left_child == a:
                parent.left_child = b
            else:
                parent.right_child = b
        else:
            node = b
    return node


def get_height(node):
    if node is None:
        return 0
    return node.height


def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left_child) - get_height(node.right_child)
