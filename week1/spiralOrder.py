class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        res = []
        c,r = len(matrix[0]),len(matrix)
        x1,y1,x2,y2 = 0,0,r-1,c-1
        while x1<=x2 and y1<=y2:
            for i in range(y1,y2+1):
                res.append(matrix[x1][i])
            for j in range(x1+1,x2+1):
                res.append(matrix[j][y2])
            if x1 < x2 and y1 < y2:
                for i in range(y2-1,y1-1,-1):
                    res.append(matrix[x2][i])
                for j in range(x2-1,x1,-1):
                    res.append(matrix[j][y1])
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        return res