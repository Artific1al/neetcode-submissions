class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0 

        i = 0
        j = len(heights)-1
        prevj = True

        while i<j:
            first = heights[i]
            second = heights[j]
            if min(first,second) * (j-i) > max:
                max = min(first,second) * (j-i)

            if heights[j] < heights[i]:
                j-=1

            else:
                i+=1


        return max
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         first = heights[i]
        #         second = heights[j]
        #         if min(first,second) * (j-i) > max:
        #             max = min(first, second) * (j-i)
        
        return max


        #repeated work - going over same bars again
        #idea - start at each end
        #calculate area
        #if 
        

#Constraints
# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000
# O(n) time | O(1) space

#Brute Force

#Edgecases

#Optimisation