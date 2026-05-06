class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

# Contraints 
# -> Target >= -10M & <= +10M
# -> So is the value of a given index in nums
# -> Exactly ONE pair of inputs will always be the answer
# return in form [lowest, highest]
# cannot reutrn the same num twice


# Brute Force
# for every number, check if every other number + that num = the target
# when it does, return the lowest then the highest
# O(n^2) time & O(1) space

# sort idea 
# would have to sort somehow -> probably n log n  / n^2 comp
# then start from middle and work outwards?
# seems complex & not helpful for this problem

# Hashing idea
# For every sum, add the indexes first + second
# Since there is only one case where target will occur, then we can override 
# the value every time that element is called
# array size of 20 M? -> No better than brute force because brute force to setup 

# What makes this challenging?
# The numbers are not sorted so there is no way to know if you're "getting close"
# sorting the nums should take n log n min - but then you still have to find them
# a <n^2 sol is not obvious atm

        for i in range(len(nums)): # assume nums is 10 -> 0 .... 9
            for j in range(i+1, len(nums)): # assume nums is 10 & i = 3, 3 ... 9
                if nums[i] + nums[j] == target:
                    lowest = i
                    highest = j
                    if j < i:
                        lowest = j
                        highest = i
                    
                    return [lowest, highest]


