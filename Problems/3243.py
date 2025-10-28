from typing import List, Dict
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph: Dict[int, List[int]] = {}
        lengths = []
        lowest_length = n - 1

        # pre processing the input
        # normal path
        for num in range(0, n):
            if num == 0:
                graph[num] = [num + 1]
            elif num < n - 1:
                graph[num] = [num - 1, num + 1]
            else:
                graph[num] = []

        def getShortestPath(start: int, end: int, direction: int):
            if start == end:
                return 0

            # store the paths
            queue = deque([[start]])
            visited = []

            while queue:
                path = queue.popleft()
                edge = path[-1]

                if edge == end:
                    return len(path) - 1

                if edge in visited:
                    continue
                visited.append(edge)

                # build the path by adding the next edge
                next_edges = graph[edge]

                for next_edge in next_edges:
                    if (direction < 0 and next_edge < edge) or (
                        direction > 0 and next_edge > edge
                    ):
                        queue.append(path + [next_edge])

        # process queries
        for start, end in queries:
            # update the graph
            graph[start].append(end)
            graph[end].append(start)
            # call the function to get the shortest path
            length_from_start_to_start = getShortestPath(start, 0, -1)
            length_from_end_to_end = getShortestPath(start, n - 1, 1)
            lowest_length = min(lowest_length,
                                (length_from_start_to_start + length_from_end_to_end)
                              )
            lengths.append(lowest_length)

        return lengths


print("RESULTS")
# Test case 01:
# Input: n = 5, queries = [[2,4],[0,2],[0,4]]
# Output: [3,2,1]
test_case_01_res = Solution().shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]])
print(f"- Test Case 01: {test_case_01_res}")

# Test case 02:
# Input: n = 4, queries = [[0,3],[0,2]]
# Output: [1, 1]
test_case_02_res = Solution().shortestDistanceAfterQueries(4, [[0, 3], [0, 2]])
print(f"- Test Case 02: {test_case_02_res}")

# Test case 03:
# Input: n = 6, queries = [[1,3],[3,5]]
# Output: [4,3]
test_case_03_res = Solution().shortestDistanceAfterQueries(6, [[1, 3], [3, 5]])
print(f"- Test Case 03: {test_case_03_res}")

# Test case 04:
# Input: n = 6, queries = [[1,4],[2,4]]
# Output: [3,3]
test_case_04_res = Solution().shortestDistanceAfterQueries(6, [[1, 4], [2, 4]])
print(f"- Test Case 03: {test_case_04_res}")

# Plan
# Preprocess the inputs to create a adjacent nodes dictionary. use A list to store the targets.
# Use the BFS to get shortest path to start (0) from the query[0] and shortest path to end (n-1)
# from the query[1].
# Concat the paths and remove duplicate nodes and then calculate the length.
