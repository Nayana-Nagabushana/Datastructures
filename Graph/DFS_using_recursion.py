def DFS(node,visited,graph): #node - starting node,graph -dictionary
    if node not in graph:
        print("node is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)

graph = {'A':['B','C','D'],'B':['A','E','D'],'C':['A','D'],'D':['A','B','C','E'],'E':['B','D']}
visited = set()      # we define outside bcs we are using recursion
DFS('A',visited,graph)



