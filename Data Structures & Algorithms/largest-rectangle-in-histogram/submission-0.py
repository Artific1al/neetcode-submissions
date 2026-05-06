class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
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