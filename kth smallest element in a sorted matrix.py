class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        list1 = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                list1.append(matrix[i][j])
        list1.sort()
        return list1[k-1]
