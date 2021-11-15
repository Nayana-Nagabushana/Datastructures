# for deleting edge no need to delete anything in nodes list

def delete_edge(v1,v2):
    if v1 not in nodes:
        print("node {} is not present in nodes".format(v1))
    elif v2 not in nodes:
        print("node {} is not present in nodes".format(v1))
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        adj_matrix[index1][index2] = 0
        adj_matrix[index2][index1] = 0

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(adj_matrix[i][j],end = " ")
        print()

nodes = ['A','B','C','D']
adj_matrix = [[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
node_count = 4
print(nodes)
print_graph()
print()
print("after deleting edge from C to D")
delete_edge("C","D")
print(nodes)
print_graph()
