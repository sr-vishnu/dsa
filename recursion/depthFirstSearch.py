
graph = {
    "a": ["b","c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def depthFirstSearchWrapper(graph: dict,source: any) -> list:
    
    result = []

    def depthFirstSearch(graph: dict,source: any) -> None:
        result.append(source)
        for neighbour in graph[source]:
            depthFirstSearch(graph, neighbour)
        return
            
    depthFirstSearch(graph, source)
    return result

print(
    depthFirstSearchWrapper(graph, "a")
)