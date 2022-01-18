
# Depth-First Search algorithm implementation using iteration and post-order traversal

from __future__ import annotations

def depth_first_search(graph: dict, start: str) -> set[str]:
    
    visited, stack = set(start), [start]

    while stack:
        last_visited = stack.pop()
        visited.add(last_visited)
    
        for neighbor in reversed(graph[last_visited]):
            if neighbor not in visited:
                stack.append(neighbor)
    return visited


graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

print(depth_first_search(graph, "A"))