# for deleting a node in  adj matrix just delete the row and column representing that node in graph
# in this example C is present in third row and third column so we delete it
def delete_node(v1):
    global node_count
    if v1 not in nodes:
        print("node {} is not present in graph".format(v1))
    else:
        index1 = nodes.index(v1)
        nodes.remove(v1)
        node_count = node_count - 1
        adj_matrix.pop(index1)    # to remove the row
        for i in adj_matrix:      # to remove the column
            i.pop(index1)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(adj_matrix[i][j],end = " ")
        print()

nodes = ['A','B','C','D']
adj_matrix = [[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,0,1]]
node_count = 4
print(nodes)
print_graph()
print()
print("after deleting node C")
delete_node('C')
print(nodes)
print_graph()
delete_node('F')