# References
# https://augustinejoseph.medium.com/graph-data-structure-in-python-38dd58752836
# https://www.datacamp.com/tutorial/breadth-first-search-in-python
#
# Graph Traversal Algorithms
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

# Shortest Path Problems
# - BFS can be used to solve shortest path problems only when the graph is unweighted.

# Question 01:
# You are given an unweighted graph represented as an adjacency list.
# Write a function to find the shortest path (in terms of the number of edges) between two nodes
# in the graph using Breadth-First Search (BFS).

# Find the shortest path from A to F

from typing import List

def shortest_path_q_01(graph: dict, start: str, end: str):
    if start not in graph:
        return []

    # queue to store paths. all the possible paths will be generated.
    queue = deque([[start]])
    visited: set[str] = set()

    while queue:
        # get the left most path from the queue
        left_most_path = queue.popleft()
        last_node = left_most_path[-1]

        # if the end node is found, return the path
        if last_node == end:
            return left_most_path

        if last_node in visited:
            continue
        visited.add(last_node)

        # get the neighbours of the last node
        for neighbour in graph.get(last_node, []):
            queue.append(left_most_path + [neighbour])
    return []


print("\n-- Question 01")
# Test case 01
q1_graph_01 = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
q1_result_01 = shortest_path_q_01(q1_graph_01, "A", "F")
print(f"Q1 Test Case 01 Result: {q1_result_01} | Expected: ['A', 'C', 'F']")

# Test case 02
q1_graph_02 = {"A": ["B"], "B": ["C"], "C": []}
q1_result_02 = shortest_path_q_01(q1_graph_02, "A", "C")
print(f"Q1 Test Case 02 Result: {q1_result_02} | Expected: ['A', 'B', 'C']")

# Test case 03
q1_graph_03 = {"A": ["B"], "B": ["C", "A"], "C": ["D"], "D": []}
q1_result_03 = shortest_path_q_01(q1_graph_03, "A", "D")
print(f"Q1 Test Case 03 Result: {q1_result_03} | Expected: ['A', 'B', 'C', 'D']")

# Test case 04
q1_graph_04: dict = {}
q1_result_04 = shortest_path_q_01(q1_graph_04, "A", "B")
print(f"Q1 Test Case 04 Result: {q1_result_04}")