class Solution:
    def search(self, nums: List[int], target: int) -> int:

    #l = 0, r = len(nums)-1, mid = l+r//2
    #0,1 = 3,5, target = 4, mid initialised to index 1 = 5

        l = 0
        r = len(nums) - 1
        mid = (l+r) // 2

        #check if in array
        while l <= r:
            #cond 1
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                l = mid + 1
                mid = (l+r)//2
            elif target < nums[mid]:
                r = mid - 1
                mid = (l+r) // 2
            #target == mid
            #should not ever get hit
            else:
                return -1
                

        #failed 
        #return mid if nums[mid] == target else -1
        return -1

#constraints
#list sorted in asc order
#log n time
#all numbers are unique (no dupes)

#edge cases
#list size even? list size odd?

#


        #how does binary search work
        #low, high, mid
        #get middle index
        # -> if result, return
        #if not result, if that num > target, high = that num -1
        
#[1,2,3]
# l = 0, h = 2, m = 1, t = "3"
#l = 2, h = 2, t = "3"
#high = 3, low = 1, mid = 2, target = 3, low = mid+1, high = high, mid = 3
#low = 2, high = 3, target = 3, mid = 
#[1,2,3,4]
#[2,3,4,5,6]