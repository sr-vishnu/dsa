
graph = {
    "a": ["b","c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["f"],
    "f": []
}


def depthFirstSearch(graph : dict,source: any ) -> list:
    result = []
    stack = [source]

    while stack:
        current = stack.pop()
        result.append(current)
        for neighbour in graph[current]:
            stack.append(neighbour)

    return result

print(depthFirstSearch(graph, "a"))