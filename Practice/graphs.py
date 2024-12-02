# References
# A good medium article for reference: https://augustinejoseph.medium.com/graph-data-structure-in-python-38dd58752836
#
# Graph Algorithms
# 1. Breadth-First Search (BFS): Explores all neighbors of a vertex level by level.
# 2. Depth-First Search (DFS): Explores as far as possible along a branch before backtracking.
#
# * [Breadth-First Search (BFS)]
# - Traversal using BFS algorithm

from collections import deque  # Import deque for efficient queue operations

# Define the BFS function
def bfs(graph, start):
    visited = set()  # List to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:  # While there are still nodes to process
        node = queue.popleft()  # Dequeue a node from the front of the queue

        if node not in visited:  # Check if the node has been visited
            visited.add(node)  # Mark the node as visited
            print(node, end=" ")  # Output the visited node

            # Enqueue all unvisited neighbors (children) of the current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue

#     A
#    / \
#   B   C
#  / \   \
# D   E   F
#      \ /
#       F

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("Traversal using BFS: ")
# Execute BFS starting from node 'A'
bfs(graph, "A")

# Output: A B C D E F
# Notes:
# The order in which neighbors are listed in the adjacency list doesn't affect the
# correctness of BFS.
# The order of traversal of nodes depends on the queue and the level of exploration
# rather than the order in the adjacency list.

# - Search for an item using BFS algorithm
# Task is to check whether an item exist

def bfs_item(graph_i, start, search_item):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node == search_item:
            return True

        if node not in visited:
            visited.add(node)

            # check the neighbours
            for neighbour in graph_i[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return False

print("\n\nSearch using BFS: ")

bfs_item_res_01 = bfs_item(graph, "A", "B")
print(f"Result for case 01: {bfs_item_res_01}")

bfs_item_res_02 = bfs_item(graph, "A", "L")
print(f"Result for case 02: {bfs_item_res_02}")
