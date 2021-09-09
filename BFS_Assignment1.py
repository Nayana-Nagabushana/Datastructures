graph = {
    'A': ['D', 'S'],
    'B': ['D', 'S'],
    'C': ['D', 'S'],
    'D': ['A','B','C'],
    'S': ['A','B','C'],

}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, graph, 'A')
