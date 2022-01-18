# # Breadth First Search algorithm implemented using recursion

# import collections

# def breath_first_search(graph, start):

#     visited, queue = set(), collections.deque([start])
#     visited.add(start)

#     while queue:

#         # Dequeue a vertex from queue
#         vertex = queue.popleft()
#         print(str(vertex) + " ", end="")

#         # If not visited, mark it as visited, and enqueue it
#         for neighbour in graph[vertex]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)


# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#     print("Breadth First Traversal: ")
#     breath_first_search(graph, 0)


# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')