class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #O(n)

        res = []
        
        for i in range(len(nums)):
            current = 1
            for j in range(len(nums)):
                if i != j:
                    current *= nums[j]
            res.append(current)
        
        return res
        
#Constraints
#Int is a suffient data type to hold it
#nums length between 2 and 1000
#nums between -20 and 20
#O(n) time and space

#Brute Force
#Multiply all nums once then divide by current num
#nums = [2,4,5,10]
#answer = [200, 100, 80, 40]
#current = [2, 8, 40, 400]
#before&after = [[0, 100], [2, 50], [8, 10], [40, 0]]


#Edge Cases
#1 0 will make everything go to 0 except itself
#2 0s will make everything go 0