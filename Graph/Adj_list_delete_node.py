# for deleting node in adj list first find the key (that is the vertex) and delete it later check all keys whether it
# contains that particular node

def delete_node(v):
    if v not in adj_list:
        print("node {} is not present in graph".format(v))
    else:
        adj_list.pop(v) # for removing that particular key
        for i in adj_list:   # here i represent tha key - to remove values in other keys containing node v
            list1 = adj_list[i]
            if v in list1:
                list1.remove(v)


adj_list = {"A":['B','C'],'B':['A','C'],'C':['A','B','D'],'D':['C']}
print("before deleting")
print(adj_list)
print()
print("after deleting node C")
delete_node("E")
print(adj_list)
