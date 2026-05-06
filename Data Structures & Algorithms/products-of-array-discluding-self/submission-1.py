class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #O(n^2)

        # res = []
        
        # for i in range(len(nums)):
        #     current = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             current *= nums[j]
        #     res.append(current)
        
        # return res


        #O(n) time and space?

        indexHash = {}

        #idea -> mutliply everything before with everything after

        #forward pass -> store every value multiplied together up to but not including current index
        forwardPass = 1
        for i in range(len(nums)):
            indexHash[i] = [forwardPass]
            forwardPass *= nums[i]

        #backward pass -> we know array is populated so just append 
        backwardPass = 1
        for j in range(len(nums)-1, -1, -1):
            indexHash[j].append(backwardPass)
            backwardPass *= nums[j]
        
        #results
        res = []
        pairs = [y for x,y in indexHash.items()]

        for elem in pairs:
            val = 1
            for num in elem:
                val *= num
            res.append(val)
        

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

#what if we made a new array for every index with the current num replaced with 1

#How can a hash map help?
#O(1) lookup

#Two O(n) loops
#Hash table key = index
#first pass add all the currents up to that point 
#second pass add all the pasts behind it 
#then iterate through keys and make a new list 