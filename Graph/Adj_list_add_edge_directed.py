def add_edge(v1,v2):
    if v1 not in graph:
        print(f"node {v1} is not present in graph")
    elif v2 not in graph:
        print(f"node {v2} is not present in graph")
    else:
        graph[v1].append(v2)

def add_node(v):
    if v in graph:
        print(f"node {v} is already present in graph")
        return
    else:
        graph[v] = []

graph = {}
add_node("A")
add_node("B")
add_node("C")
print(graph)
print()
print("After adding edges")
add_edge("A","B")
add_edge("B","C")
print(graph)
