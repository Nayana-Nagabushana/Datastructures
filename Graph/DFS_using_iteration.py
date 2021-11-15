def DFS(node,graph):
    visited = set()
    if node not in graph:
        print("node is not present in graph")
        return
    stack =[]
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            print(current)
            for i in graph[current]:
                stack.append(i)
    return visited


graph = {'A':['B','C','D'],'B':['A','E','D'],'C':['A','D'],'D':['A','B','C','E'],'E':['B','D']}
DFS('A',graph)





