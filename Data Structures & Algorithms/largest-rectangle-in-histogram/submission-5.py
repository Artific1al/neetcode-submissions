class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        
        lefts = [-1] * len(heights) #left indicies where first rect smaller occurs
        rights = [len(heights)] * len(heights) #right indicies where first rect smaller occurs

        leftStack = [] #stack of decreasing order (index, height) going from left to right
        rightStack = [] #going from right to left

        for ind in range(len(heights)):
            
            #bigger than = found end of rectangle
            while leftStack and heights[ind] < leftStack[-1][1]:
                index, height = leftStack.pop()
                rights[index] = ind
            
            #add to stack (monotonically decreasing order)
            leftStack.append((ind, heights[ind]))

       
        for ind in range(len(heights)-1, -1, -1):

            
            #bigger than = found end of rectangle
            while rightStack and heights[ind] < rightStack[-1][1]:
                index, height = rightStack.pop()
                lefts[index] = ind
            
            #add to stack (monotonically decreasing order)
            rightStack.append((ind, heights[ind]))


        #offsets to keep uniform representation right-left
        #lefts[0] -=1
        #rights[len(heights)-1] +=1

        #print(f"Lefts: {lefts}")
        #print(f"Rights {rights}")

        best = 0
        for i in range(len(heights)):
            area = (rights[i] - lefts[i] - 1) * heights[i]
            if area > best:
                best = area

        print(best)        
        return best


        # lefts = [0] * len(heights) #left indicies where first rect smaller occurs
        # rights = [len(heights)-1] * len(heights) #right indicies where first rect smaller occurs

        # leftStack = [] #stack of decreasing order (index, height) going from left to right
        # rightStack = [] #going from right to left

        # for ind in range(len(heights)):
            
        #     #bigger than = found end of rectangle
        #     while leftStack and heights[ind] > leftStack[-1][1]:
        #         _, height = leftStack.pop()
        #         rights[ind - 1] = ind
            
        #     #add to stack (monotonically decreasing order)
        #     leftStack.append((ind, heights[ind]))

       
        # for ind in range(len(heights)-1, -1, -1):

            
        #     #bigger than = found end of rectangle
        #     while rightStack and heights[ind] > rightStack[-1][1]:
        #         index, height = rightStack.pop()
        #         lefts[index] = ind
            
        #     #add to stack (monotonically decreasing order)
        #     rightStack.append((ind, heights[ind]))


        # #print(f"Lefts: {lefts}")
        # #print(f"Rights {rights}")

        # best = 0
        # for i in range(len(heights)):
        #     area = (rights[i] - lefts[i]) * heights[i]
        #     if area > best:
        #         best = area
        
        # return best

        # lefts = [None] * len(heights) #left indicies where first rect smaller occurs
        # rights = [len(heights)-1] * len(heights) #right indicies where first rect smaller occurs

        # leftStack = [] #stack of decreasing order (index, height)
        # rightStack = []

        # for ind in range(len(heights)):
        #     #edge case first num
        #     if not leftStack:
        #         leftStack.append((ind, heights[ind]))
            
        #     #bigger than = found end of rectangle
        #     while heights[ind] > leftStack[-1]:
        #         _, height = leftStack.pop()
        #         rights[ind] = heights[ind]
            
        #     #add to stack (monotonically decreasing order)
        #     leftStack.append(ind, heights[ind])

       
        # for ind in range(len(heights)-1, -1, -1):
        #     #edge case first num
        #     if not rightStack:
        #         rightStack.append((ind, heights[ind]))
            
        #     #bigger than = found end of rectangle
        #     while heights[ind] > rightStack[-1]:
        #         _, height = rightStack.pop()
        #         rights[ind] = heights[ind]
            
        #     #add to stack (monotonically decreasing order)
        #     rightStack.append(ind, heights[ind])


       
        #O(n) idea
        #for every index,
        #check ONLY to the left of it
        #first, pull off the (minHeight, len, bestSoFar) from the stack
        #then, using your new minHeight, calculate bestSoFar, len
        
        #left to right stack
        # ltrStack = []
        # #values = (minHeight to the left of it for best, len, bestSoFar)

        # for i in range(len(heights)):
            
        #     #base case 
        #     if len(ltrStack) == 0:
        #         ltrStack.append((heights[i], 1, heights[i]))
        #         continue

        #     #pull top element off stack
        #     minHeight, left, bestSoFar = ltrStack[-1]

        #     #if current is higher or equal to existing minHeight
        #     if heights[i] >= minHeight:
        #         left +=1 #because we meet the minHeight
        #         bestSoFar = max(heights[i], left * minHeight)
        #         ltrStack.append((minHeight, left, bestSoFar))
            
        #     #if current is lower than existing minHeight
        #     else:
        #         left +=1
        #         minHeight = heights[i]
        #         ltrStack.append((minHeight, left, bestSoFar))
        
        # return ltrStack[-1][2]




        # lens = []

        # for i in range(len(heights)):

        #     #case 1 just itself
        #     minArea = heights[i] #hx1

        #     #variables
        #     minHeight = heights[i]
        #     left = 0
        #     right = 0
        #     bestSoFar = [heights[i]]


        #     #case 2, check to right
        #     minHeight = heights[i]
        #     for rInd in range (i, len(heights)):
        #         if heights[rInd] > 0:

        #             if heights[rInd] < minHeight:
        #                 #update minHeight
        #                 minHeight = heights[rInd]
                    
        #             #calculate current
        #             current = (right + 1) * minHeight

        #             if current > bestSoFar[-1]:
        #                 bestSoFar.append(current)

        #             right +=1
        #         else:
        #             break
            
        #     if (len(lens) == 0) or bestSoFar[-1] > lens[-1]:
        #         lens.append(bestSoFar[-1])
        
        # return lens[-1]

            
        
    
#Constraints
#O(n) time space
#heights between 1-1000 items
#individual heights ints between 0-1000
#width of ALL BARS = 1

#Brute Force
#for every element, check until cant on left and until cant on right
#append the largest rectangle you can

#Edge