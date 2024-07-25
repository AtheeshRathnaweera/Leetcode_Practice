class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version_01 = list(map(int, version1.split(".")))
        version_02 = list(map(int, version2.split(".")))

        # make the parts equal
        revision_count_diff = len(version_01) - len(version_02)
        if revision_count_diff > 0:
            version_02.extend([0] * revision_count_diff)
        elif revision_count_diff < 0:
            version_01.extend([0] * abs(revision_count_diff))

        for v_01_index, value in enumerate(version_01):
            if value > version_02[v_01_index]:
                return 1

            if value < version_02[v_01_index]:
                return -1

        return 0

print(Solution().compareVersion(version1 = "1.01", version2 = "1.001"))
print("Expected: 0\n")

print(Solution().compareVersion(version1 = "1.0", version2 = "1.0.0"))
print("Expected: 0\n")

print(Solution().compareVersion(version1 = "0.1", version2 = "1.1"))
print("Expected: -1\n")

print(Solution().compareVersion(version1="1.2.67", version2="1.1.66"))
print("Expected: -1\n")

print(Solution().compareVersion(version1="1.0", version2="1.0.66"))
print("Expected: -1\n")
