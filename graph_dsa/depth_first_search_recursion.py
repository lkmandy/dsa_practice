# Depth-First Search algorithm implementation using recursion and post-order traversal

def depth_first_search(graph, start, visited = None):
    # Check if any nodes have been visited
    if visited is None:
        visited = set()

    # Mark the starting node as visited
    visited.add(start)

    # Remove the currently visited node and traverse through it's neigbors
    for neighbor in graph[start] - visited:

        # Call the depth first search algorithm for each neighbor
        depth_first_search(graph, neighbor, visited)

    # return the set of visited nodes in the order of traversal
    return visited



if __name__ == '__main__':
    
    graph = { '0': set(['2', '3']),
          '1': set(['0', '3']),
          '2': set(['3']),
          '3': set(['1']),
          }
    
    print(depth_first_search(graph, '0'))