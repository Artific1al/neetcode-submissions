class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
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




        lens = []

        for i in range(len(heights)):

            #case 1 just itself
            minArea = heights[i] #hx1

            #case 2, check to left
            minHeight = heights[i]
            left = 0
            right = 0

            bestSoFar = [heights[i]]

            #if element is not 0 and is 
            for lInd in range (0, i):
                if heights[lInd] > 0:

                    if heights[lInd] < minHeight:
                        #update minHeight
                        minHeight = heights[lInd]
                    
                    #calculate current
                    current = (left + 1) * minHeight

                    if current > bestSoFar[-1]:
                        bestSoFar.append(current)

                    left +=1
                else:
                    break

            #case 3, check to right
            minHeight = heights[i]
            for rInd in range (i, len(heights)):
                if heights[rInd] > 0:

                    if heights[rInd] < minHeight:
                        #update minHeight
                        minHeight = heights[rInd]

                    #calculate left
                    
                    #calculate current
                    current = (right + 1) * minHeight

                    if current > bestSoFar[-1]:
                        bestSoFar.append(current)

                    right +=1
                else:
                    break
            
            if (len(lens) == 0) or bestSoFar[-1] > lens[-1]:
                lens.append(bestSoFar[-1])
        
        return lens[-1]

            
        
    
#Constraints
#O(n) time space
#heights between 1-1000 items
#individual heights ints between 0-1000
#width of ALL BARS = 1

#Brute Force
#for every element, check until cant on left and until cant on right
#append the largest rectangle you can

#Edge