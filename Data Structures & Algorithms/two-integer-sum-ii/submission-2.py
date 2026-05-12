class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        #O(n), #O(1) space
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -=1
            else:
                left +=1

        return[left+1, right+1]

        # Brute force
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if numbers[j] + numbers[i] == target:
        #             return [i+1, j+1]

        
        

#Constraints
#O(n) time and O(1) space
#assume its a one indexed array
#sorted in non decreasing order
#exactly one valid sol
#numbs between -1000 and 1000, same for target

#Brute Force
#O(n^2) iterate in two loops
#How to decrease repeated work

#Edge Cases
#two nums that are the same next to each other

#Optimisation