class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        :note:
            从外到里一圈一圈的旋转，先将第一个值赋给tmp,后面相应的位置补上前面的空位
        """
        # matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
        
        m = len(matrix)
        for c in range(0, m/2): # cirlce
            n = m - 2*c         # sub matrix range = [c:c+n][c:c+n]
            for i in range(n-1):
                tmp = matrix[c][c+i]
                matrix[c][c+i] = matrix[c+n-1-i][c]
                matrix[c+n-1-i][c] = matrix[c+n-1][c+n-1-i]
                matrix[c+n-1][c+n-1-i] = matrix[c+i][c+n-1]
                matrix[c+i][c+n-1] = tmp
            # print matrix
