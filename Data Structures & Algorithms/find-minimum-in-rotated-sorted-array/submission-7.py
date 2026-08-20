class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = (2 * len(nums)) - 1
        m = ((l + r) // 2)
        msf = -math.inf #max so far

        if len(nums) == 1:
            return nums[0]
        

        while l <=r:

            nextm = (m + 1)
            
            if nums[nextm % len(nums)] < nums[m % len(nums)]:
                return nums[nextm % len(nums)]
            
            #if this is biggest num - update msf and go right
            elif nums[m % len(nums)] >= msf:
                l = m + 1
                msf = nums[m % len(nums)] 
                m = ((l + r) // 2)


            #if we've seen a bigger number - go left
            elif nums[m % len(nums)] < msf:
                r = m - 1 #l is offset so we know if we're at first 0-6 or 2nd
                m = ((l + r) // 2)

        #should never be hit
        return nums[m % len(nums)]


        
            
        
#[4,5,0,1,2,3,4,5,0,1,2,3]
#constraints
#not empty list
#nums between -1000 and 1000

#brute force
#O(n) linear search

#edge cases

#idea 
#target
#increase bounds to l, r=2*len - 1
#then, divide mid % len of array

        