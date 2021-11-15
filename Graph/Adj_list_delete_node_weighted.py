    # for deleting node in adj list first find the key (that is the vertex) and delete it later check all keys whether it
    # contains that particular node

def delete_node(v):
        if v not in adj_list:
            print("node {} is not present in graph".format(v))
        else:
            adj_list.pop(v) # for removing that particular key
            for i in adj_list:   # here i represent tha key - to remove values in other keys containing node v
                list1 = adj_list[i]
                for j in list1:
                    if v == j[0]:
                        list1.remove(j)
                        break


adj_list = {"A":[['B',10],['C',5]],'B':[['A',10],['C',2]],'C':[['A',5],['B',2],['D',4]],'D':[['C',4]]}
print("before deleting")
print(adj_list)
print()
print("after deleting node C")
delete_node("C")
print(adj_list)
