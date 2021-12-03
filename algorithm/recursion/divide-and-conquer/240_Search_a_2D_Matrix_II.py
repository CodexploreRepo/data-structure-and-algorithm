class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #Base Case: 
        if not matrix or not matrix[0]: return False
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
        #Recursion Case: Divide the search into 4 regions by cal the center of matrix
        center_x, center_y = len(matrix[0])//2, len(matrix)//2
        
        if matrix[center_y][center_x] > target:
            tl = self.searchMatrix([matrix[row][:center_x] for row in range(0, center_y)], target)
            tr = self.searchMatrix([matrix[row][center_x:] for row in range(0, center_y)], target)
            bl = self.searchMatrix([matrix[row][:center_x] for row in range(center_y, len(matrix))], target)      
            return tl or tr or bl #Conquer
        elif matrix[center_y][center_x] < target:
            tr = self.searchMatrix([matrix[row][center_x:] for row in range(0, center_y)], target)
            bl = self.searchMatrix([matrix[row][:center_x] for row in range(center_y, len(matrix))], target)
            br = self.searchMatrix([matrix[row][center_x:] for row in range(center_y, len(matrix))], target)
            return tr or bl or br
        else:
            return True
