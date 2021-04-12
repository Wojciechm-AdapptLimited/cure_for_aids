
import random
#generating an array with random elements
def rand(size):
    return [random.randint(-size, size) for _ in range(size)]


#asking for input from user and checking if it only contains positive integers
while True:
    data = input("Enter the numbers: ").strip().split()
    if len(data) > 10:
        print("Too many elements! Try again")
        continue
    else:
        for item in data:
            if item.isdigit():
                item = int(item)
            else:
                print("You can only enter positive integers!")
                continue
        break
arr = list(map(int,data))


# Klasa reprezentujaca pojedynczy wezel drzewa
class Node:
    def __init__(self, value = None):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None


    def insert(self, value):
        if not self.value:  # there is no value in node yet
            self.value = value
            return
        if self.value == value:  # there already exists the same value
            return
        if value < self.value:  #building left subtree
            if self.left:
                self.left.insert(value)
                return
            self.left = Node(value)     #giving class node inserted value
            return
        if value > self.value:
            if self.right:
                self.right.insert(value)
                return
            self.right = Node(value)
            return

    def delete(self, value):
        if self == None:    #if the node is empty
            return self
        if value < self.value:     #going to the left of the tree if element is smaller
            if self.left:
                self.left = self.left.delete(value)
            return self
        if value > self.value: #going to the right
            if self.right:
                self.right = self.right.delete(value)
            return self

        #if the value to delete is the same as node
        if self.right == None: #cases when there is only one son
            return self.left
        if self.left == None:
            return self.right
                                        #case where there are 2 sons
        min_larger_node = self.right    #bigger elem than the deleted one
        while min_larger_node.left:
            min_larger_node = min_larger_node.left      #finding the smallest but bigger number than the node
        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)    #moving all the left elem on good position
        return self

    def delTree(self):
        if self == None: #if the tree is empty
            return self
        if self.left:   # going down to the left of the tree
            self.left.delTree()
        if self.right:  # going down to the right of the tree
            self.right.delTree()
        print("Deleting the node: ", self.value) #if there is no son(right or left) delete the node
        self.value = None

def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    tree = Node()
    for num in nums:
        tree.insert(num)
    delNodes = int(input("Enter a number of nodes to delete: "))
    for i in range(delNodes):
        delVal = int(input("Enter the number to delete: "))
        tree.delete(delVal)
main()
