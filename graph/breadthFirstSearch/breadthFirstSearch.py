from collections import deque


graph = {
    "a": ["b","c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def breadthFirstSearch(graph: dict,source: any) -> list:
    _result = []
    _queue = deque()
    _queue.append(source)

    while len(_queue) != 0:
        current = _queue.popleft()
        _result.append(current)
        for neighbour in graph[current]:
            _queue.append(neighbour)

    return _result


print(
    breadthFirstSearch(graph, "a")
)