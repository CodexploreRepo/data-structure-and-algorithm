class Solution(object):
    def totalNQueens(self, n, row=0, diag=set(), off_diag=set(), cols=set()):
        """
        :diag, off_diag, cols: sets => to keep track on attacked zones
        """
        #Base Case: row = n, i.e. we find a solution since row start from 0 to (n-1)!
        if row == n: return 1
        
        count = 0
        
        for col in range(n):
            # At each curent row, iterate through columns
            if row-col in diag or row+col in off_diag or col in cols:
                #if current cell in the attacked zones, we will skip that cell
                continue
            else:
                #if current cell NOT in the attacked zones, we will place the new queen at that cell
                diag.add(row-col)
                off_diag.add(row+col)
                cols.add(col)

                #Move to the next row
                count += self.totalNQueens(n, row + 1, diag, off_diag, cols)
                
                # backtrack, i.e. remove the queen and remove the attacking zone.
                diag.remove(row-col)
                off_diag.remove(row+col)
                cols.remove(col)
        
        return count
