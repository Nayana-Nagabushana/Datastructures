def DFS(node,visited,graph): #node - starting node,graph -dictionary
    if node not in graph:
        print("node is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i[0],visited,graph)

graph = {'A':[['B',10],['C',5],['D',4]],'B':[['A',10],['E',7],['D',3]],'C':[['A',5],['D',1]],'D':[['A',10],['B',7],['C',1],['E',2]],'E':[['B',3],['D',2]]}
visited = set()      # we define outside bcs we are using recursion
DFS('A',visited,graph)



