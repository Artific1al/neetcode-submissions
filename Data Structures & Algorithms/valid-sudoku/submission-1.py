class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

                
        #First Passover -> Check Rows
        for row in board: 

            seen = [False] * len(board[0]) #number seen already AT POSITION index of array + 1
            
            for element in row:
                
                #edge case is .
                if element != ".":
                    
                    index = int(element) - 1
                    if seen[index] is True:
                        return False
                    else:
                        seen[index] = True

            
        #Second Passover - columns
        for columnInd in range(0, len(board)):

            column = [row[columnInd] for row in board]
            seen = [False] * len(board[0])  #number seen already AT POSITION index of array + 1
            for element in column:

                 #edge case is .
                if element != ".":
                    
                    index = int(element) - 1
                    if seen[index] is True:
                        return False
                    else:
                        seen[index] = True


        #Final Passover - 3x3 grids
    
        #For every mini row
        #offset = 3 because the squared are 3x3
        offset = 3
        for miniRow in range(0, len(board), 3):

            #And every mini column
            for miniColumn in range(0, len(board), 3):

                square = [row[miniColumn: miniColumn+offset] for row in board[miniRow: miniRow+offset]]
                
                seen = [False] * len(board[0])  #number seen already AT POSITION index of array + 1
                for section in square:
                    for element in section:
                            
                        #edge case is .
                        if element != ".":
                            
                            index = int(element) - 1
                            if seen[index] == True:
                                return False
                            else:
                                seen[index] = True

        #didnt fail before now -> valid sudoku board
        return True
                
               

            

        

#Constraints
#9x9 = 81 tile board
#Rows are valid if contains digits 1-9 without duplicates
#Columns are valid if 1-9 no dup
#3x3 squares are valid if 1-3 no dup
#Input is in rows from top to bottom
#all inputs are nums 1-9 or .
#O(n^2) time and space (or better) WHERE N IS THE NUMBER OF ROWSSSS ? - wait so n = 9 in a square grid?
#We are NOT SOLVING. WE just want to know if the current state of the board is valid aka
#does not violate any existing rules

#Brute Force
#For every single row check no duplicate nums via 9 local vars (constant time)
#For every single column check the same
#For every single 3x3 sub box check the same 
#If ever invalid -> return early
#O(3n? time and 3n space?) (total input)


#Edge Cases
#

#Optimisations
#Draw it -> how can I visualise it?
#How can hashmaps / O(1) lookup be useful in this context?