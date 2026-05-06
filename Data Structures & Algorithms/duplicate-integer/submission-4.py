class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
# brute force sol is for every elem in array
# to check if in duplicate array, and if not add, if so return false
# = O(n^2) time & O(n) space 
# since you have to do n linear searches in the duplicate array of size 1..2..n-1

# Upgrade to this could be sorted array + binary search or hashmaps

# Sorted array + binary search
# duplicate is a sorted array, and when checking if a duplicate exists you use binary search
# for a time comp of n * log(n) when the length of the duplicate array is 1...2...n
# O(n log n), space = O(n) since linear array

# Hash maps -> Promise O(1) sorting and retrieval provided a good enough hash function
# Implementation -> could be done in a normal array (not sure if python
# has other built in hash maps)
# Create hash function that should be unique (e.g. current index is array len)
# Then hash every num into an array
# If you O(n) search to find the largest num, make an array of that size, then use
# the hash H(n) = n e.g. index is the num itself then if you ever run into a collision
# return false, if not return true (/ the allocation)

# This would be O(n) time for largest num + O(n) for hashing into array = O(n) time & space comp
# Is it necessary to search through and get the largest number in this context?
# I think so because otherwise you have no idea what the size of the hash table needs to be
# to maintain the invariant that there should be no collisions?

        largest = 0

        #acquire largest num in O(n)
        for num in nums:
            if abs(num) > largest:
                largest = abs(num)

        # setup duplicate array
        duplicate = (largest+1) * [-1]
        negative = (largest+1) * [1]

        # hash values in O(n)
        for num in nums:
            if num >= 0:
                # if this is the first instance of the value -> hash
                if duplicate[num] == -1:
                    duplicate[num] = num
                # otherwise we've violated the invariant that nums[0.. num] has only unique nums
                # -> return false
                else:
                    return True
            else:
                if negative[abs(num)] == 1:
                    negative[abs(num)] = num
                else:
                    return True
        return False

        # invariant -> nums[0.. num] has only unique nums if the program is still running?         
        # initialisation

        # mistakes 
        # -> misread question and returned T/F in opposite order of what was asked
        # -> did not make note of edge cases to begin with and got caught by negative numbers