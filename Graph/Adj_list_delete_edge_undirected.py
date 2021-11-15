    # for deleting node in adj list first find the key (that is the vertex) and delete it later check all keys whether it
    # contains that particular node

def delete_edge(v1,v2):
        if v1 not in adj_list:
            print("node {} is not present in graph".format(v1))
        elif v2 not in adj_list:
            print("node {} is not present in graph".format(v1))
        else:
            if v2 in adj_list[v1]:
                adj_list[v1].remove(v2)
                adj_list[v2].remove(v1)
        return adj_list

adj_list = {"A":['B','C'],'B':['A','C'],'C':['A','B','D'],'D':['C']}
print("before deleting")
print(adj_list)
print()
print("after deleting edge between A and B")
delete_edge('A','B')
print(adj_list)
