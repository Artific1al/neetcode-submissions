class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0 
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                first = heights[i]
                second = heights[j]
                if min(first,second) * (j-i) > max:
                    max = min(first, second) * (j-i)
        
        return max
        

#Constraints
# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000
# O(n) time | O(1) space

#Brute Force

#Edgecases

#Optimisation