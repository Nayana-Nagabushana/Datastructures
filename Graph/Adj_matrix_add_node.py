# we need two list - one for nodes and one for storing matrix in nested list

def add_node(v):
   global node_count
   # check if v is in graph
   if v in nodes:
        print("Node {v} already present in graph".format(v))
   else:
       node_count += 1
       # add column for adj matrix
       nodes.append(v)
       for column in adj_matrix:
           column.append(0)

       # for adding last row
       temp = []
       for row in range(node_count):
           temp.append(0)
       adj_matrix.append(temp)

# to print in matrix form
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(adj_matrix[i][j], end =' ')
        print()

nodes = []
adj_matrix = []
node_count = 0
print("before adding")
print("nodes :" ,nodes)
print("Adj matrix :", adj_matrix)
print()
add_node("A")
add_node("B")
print("after adding")
print("node : ",nodes)
print("Adj matrix :", adj_matrix)
print_graph()