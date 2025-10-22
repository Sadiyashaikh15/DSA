class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        current = 1
        
        while current <= n * n:
            for i in range(left, right + 1):
                matrix[top][i] = current
                current += 1
            top += 1
            
            for i in range(top, bottom + 1):
                matrix[i][right] = current
                current += 1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = current
                    current += 1
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = current
                    current += 1
                left += 1
        
        return matrix