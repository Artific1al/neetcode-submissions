class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix[0]) * len(matrix) - 1
        mid = r-l // 2 
        
        while l <=r:
            column = mid // len(matrix[0]) #what bracket in the matrix
            #row = r-l % len(matrix[0]) #what section of the bracket
            row = mid % len(matrix[0])

            #target found
            if matrix[column][row] == target:
                return True

            #
            elif matrix[column][row] > target:
                r = mid - 1
                mid = r - l // 2

            #bigger than
            else:
                l = mid + 1
                mid = r - l // 2
        
        return False

#constraints

#edge

#brute force
#O(m * n) = linear search

#idea
#-> binary search but mid has both a column and row
#O(log n) is cause you keep halving the n sized array
#O(log (m*n)) is imagine you stack all the columns side by side in one big long array as long as you
#keep cutting it up and discarding one half you get m*n


