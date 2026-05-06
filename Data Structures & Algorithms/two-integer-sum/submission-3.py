class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #python dictionary key value pairs hashmap
        hashMap = {}
        
        #iterate through the indexes
        for i in range(len(nums)):
            #i = 7, nums[i] = 4, target = 9, diff = 5
            #this is the value we want to find in nums
            difference = target - nums[i]
            #O(1) expected lookup because hash function
            if difference in hashMap:
                return[hashMap[difference],i]
            
            #populate the current part of hashmap 
            hashMap[nums[i]] = i
        

            
            
        
#Constraints
#Two different nums
#Sum to a desired num
#There is exactly one pair that satisfies the condition
#Aim for O(n) time and O(n) space
#nums between -10m and +10m
#list of array between 2 and 1000

#Brute Force
#iterate through every num in array
#for each num after it, check if they sum to desired target

#Non brute force - make another list O(n) time and space of target - every num
#then, for every 

#Edge Cases


#create a hash map in O(n) space that has all the target - nums
#for every value in nums, if that value 