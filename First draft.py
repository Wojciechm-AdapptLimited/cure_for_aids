import random
from collections import defaultdict
size = int(input("Enter the number of the vertices: "))
wsp = 0.5 *(((size)*(size-1))/2)

def adjMat(size):            #adding 1 in upper triangle of the matrix
    mat = [[0 for x in range(size)] for y in range(size)]
    edges = 0
    for y in range(size-2):             #choosing random place for 1 in every row
        x=random.randint(y+1,size-1)
        mat[y][x] = 1
        edges+=1

    while edges < wsp:                  #choosing random place for 1 in matrix
        y= random.randint(0,size-2)
        x= random.randint(y+1,size-1)
        if mat[y][x] == 1:
            continue
        else:
            mat[y][x] = 1
            edges +=1
    return mat

adjacencyMatrix = adjMat(size)

def printingMat(mat):
    print("Adjacency Matrix:")
    for i in range(size):
        print(mat[i])

def adjList(mat):
    lst = defaultdict(list)
    for y in range(size):
        for x in range(size):
            if mat[y][x]==1:
                lst[y].append(x)
    return lst
adjacencyList = adjList(adjacencyMatrix)

def printingAdjList(mat):
    print("Adjacency List:")
    for y in mat:
        print(y,end="")
        for x in mat[y]:
            print(" -> {}".format(x),end="")
        print()


def edgList(mat):
    edgesL = []
    for y in range(size):
        for x in range(size):
            if mat[y][x]==1:
                edgesL.append([y,x])
    return edgesL

edgeList = edgList(adjacencyMatrix)

def printingEdgList(mat):
    print("Edge List: ")
    for y in range(len(mat)):
        print(mat[y])

printingMat(adjacencyMatrix)
print()
printingAdjList(adjacencyList)
print()
printingEdgList(edgeList)
