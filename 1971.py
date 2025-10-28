from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # check if the edges list is empty
        if not edges:
            return True

        edges_copy = edges.copy()

        def is_destination_in_next_level(source):
            """
            Helper function to recursively explore paths from a given source.
            """
            current_edges = []

            # get the edges with source at any position
            for edge in edges_copy:
                if source in edge:
                    if destination in edge:
                        return True

                    current_edges.append(edge)

            for edge in current_edges:
                if edge in edges_copy:
                    edges_copy.remove(edge)

                new_source = sum(edge) - source
                if is_destination_in_next_level(new_source):
                    return True

            return False

        return is_destination_in_next_level(source)


print(
    Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
)
print("Expected: true")

print(
    Solution().validPath(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
)
print("Expected: false")

print(Solution().validPath(n=5, edges=[[0, 4]], source=0, destination=4))
print("Expected: true")

print(
    Solution().validPath(
        n=10,
        edges=[
            [4, 3],
            [1, 4],
            [4, 8],
            [1, 7],
            [6, 4],
            [4, 2],
            [7, 4],
            [4, 0],
            [0, 9],
            [5, 4],
        ],
        source=5,
        destination=9,
    )
)
print("Expected: true")

print(Solution().validPath(n=1, edges=[], source=0, destination=0))
print("Expected: true")

print(
    Solution().validPath(
        n=10,
        edges=[
            [0, 7],
            [0, 8],
            [6, 1],
            [2, 0],
            [0, 4],
            [5, 8],
            [4, 7],
            [1, 3],
            [3, 5],
            [6, 5],
        ],
        source=7,
        destination=5,
    )
)
print("Expected: true")


print(
    Solution().validPath(
        n=50,
        edges=[
            [31, 5],
            [10, 46],
            [19, 31],
            [5, 1],
            [31, 28],
            [28, 29],
            [8, 26],
            [13, 23],
            [16, 34],
            [30, 1],
            [16, 18],
            [33, 46],
            [27, 35],
            [2, 25],
            [49, 33],
            [44, 19],
            [22, 26],
            [30, 13],
            [27, 12],
            [8, 16],
            [42, 13],
            [18, 3],
            [21, 20],
            [2, 17],
            [5, 48],
            [41, 37],
            [39, 37],
            [2, 11],
            [20, 26],
            [19, 43],
            [45, 7],
            [0, 21],
            [44, 23],
            [2, 39],
            [27, 36],
            [41, 48],
            [17, 42],
            [40, 32],
            [2, 28],
            [35, 38],
            [3, 9],
            [41, 30],
            [5, 11],
            [24, 22],
            [39, 5],
            [40, 31],
            [18, 35],
            [23, 39],
            [20, 24],
            [45, 12],
        ],
        source=29,
        destination=46,
    )
)
print("Expected: false")
