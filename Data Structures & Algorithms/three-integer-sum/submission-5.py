class Solution:
    
    def threeSum(self, nums: int):

        output = []
        sortedNums = sorted(nums)

        for index in range(len(sortedNums)-2):
            if index > 0 and sortedNums[index] == sortedNums[index - 1]:
                continue
  
            target = -1 * sortedNums[index]
            left = index + 1
            right = len(sortedNums) - 1

            #O(n), #O(1) space
            while right > left:

                current = sortedNums[index] + sortedNums[left] + sortedNums[right]
                if current < 0:
                    left += 1

                elif current > 0:
                    right -= 1
                
                else:
                    output.append([sortedNums[index], sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                
                       # Step 4: skip duplicates for left pointer
                    while left < right and sortedNums[left] == sortedNums[left - 1]:
                        left += 1
                    # Step 5: skip duplicates for right pointer
                    while left < right and sortedNums[right] == sortedNums[right + 1]:
                        right -= 1

           
        
        return output
