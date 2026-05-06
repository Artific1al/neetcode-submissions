class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

# Array of ints in NON DECREASING ORDER e.g. 10 10 10 12 12 17 19 20
# 1 indexed array -> so when returning the indexes, add 1 to both indices
# index1 + index 2 = target & index1 < index2 
# index1 cannot = index 2
# ALWAYS EXACTLY ONE SOLUTION
# O(1) Aux Space
# 2 <= array length <= 1000
# -1000 <= numbers[i] <= 1000

# Naive Appraoch
# Iterate through and get the index of all unique nums
# for every unique num, if a sum of two of them = target and index 1 < index 2:
# return
# = O(n^2) if all nums are unique time comp + O(n) aux to store the unique indexes 
# -> Violates complexity


# Or alternatively Naive Appraoch
        for first in range(len(numbers)): # 0 , 1 ... n
            for second in range(first+1, len(numbers)): # first , first + 1, ... n
                if numbers[first] != numbers[second] and numbers[first] + numbers[second] == target:
                    return [first + 1, second +1] 
# if num + second = target
# return
# O(n^2) + O(1) aux