class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        length = rows*cols
        # index k -> row = (k // cols), col = k % cols
        low = 0
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            row_mid, col_mid = mid // cols, mid % cols
            if matrix[row_mid][col_mid] < target:
                low = mid + 1
            elif matrix[row_mid][col_mid] > target:
                high = mid - 1
            elif matrix[row_mid][col_mid] == target:
                return True

        return False