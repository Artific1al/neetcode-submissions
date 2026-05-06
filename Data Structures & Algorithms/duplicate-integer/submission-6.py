class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):

            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

        
        
        # maxNum = 0 
        # #O(n) time 
        # for num in nums: 
        #     if num > maxNum: 
        #         maxNum = num 
        #     #O(n) space 

        # simpleHash = [None] * ((maxNum)*2+1)
        # mid = simpleHash // 2 
        # #hash function = num value 
        # #O(n) time 
        # for num in nums:
        #     if simpleHash[num] == None:
        #         if num < 0:
        #             simpleHash[num] = num 
        #     else: 
        #         return True 
        
        # return False 
        
        #Constraints 
        #Aim for O(n) time and O(n) space 
        
        #Brute Force 
        
        #Sort, then check if next num is equal - O(n) space and O(sort) + O(n) time 
        #sorted = nums.sort() #timsort is O(n log n worst case) 
        #Solution: Can put in a hash table with O(n) space and O(n) time, and if I ever c 
        #Edgecases #Cant identify any