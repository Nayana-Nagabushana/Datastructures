# adding edges to undirected graph

def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(f'node {v1} is not present in nodes')
    elif v2 not in nodes:
        print(f'node {v2} is not present in nodes')
    else:
        # we need to get index of two nodes first
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        adj_matrix[index1][index2] = cost
        adj_matrix[index2][index1] = cost
    return adj_matrix

# to print in matrix form
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(adj_matrix[i][j], end =' ')
        print()

nodes = ['A','B','C']
adj_matrix = [[0,0,0],[0,0,0],[0,0,0]]
node_count=3
print("node :",nodes)
print("adj matrix :",adj_matrix)
print_graph()
print()
print("after adding edge from A to B :")
add_edge("A","B",5)
print(adj_matrix)
print_graph()
print()
print("after adding edge from B to C :")
add_edge("B","C",2)
print(adj_matrix)
print_graph()