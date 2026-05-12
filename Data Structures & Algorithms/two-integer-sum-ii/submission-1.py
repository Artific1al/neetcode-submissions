class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[j] + numbers[i] == target:
                    return [i+1, j+1]
        

#Constraints
#O(n) time and O(1) space
#assume its a one indexed array
#sorted in non decreasing order
#exactly one valid sol

#Brute Force
#O(n^2) iterate in two loops
#How to decrease repeated work

#Edge Cases
#two nums that are the same next to each other

#Optimisation