    # for deleting node in adj list first find the key (that is the vertex) and delete it later check all keys whether it
    # contains that particular node

def delete_edge(v1,v2,cost):
        if v1 not in adj_list:
            print("node {} is not present in graph".format(v1))
        elif v2 not in adj_list:
            print("node {} is not present in graph".format(v1))
        else:
            temp = [v1,cost]
            temp1 = [v2,cost]
            if temp1 in adj_list[v1]:
                adj_list[v1].remove(temp1)
                adj_list[v2].remove(temp)
        return adj_list

adj_list = {"A":[['B',10],['C',5]],'B':[['A',10],['C',2]],'C':[['A',5],['B',2],['D',4]],'D':[['C',4]]}
print("before deleting")
print(adj_list)
print()
print("after deleting edge between A and B")
delete_edge('A','B',10)
print(adj_list)
