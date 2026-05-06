class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #globalHash = {}

        # for elem in nums:
            
        #     #O(1) check if key in hash
        #     if elem in globalHash:

        #         newVal = globalHash[elem] + 1
        #         globalHash[elem] = newVal #assumes values are always ints            
        #     #if key not in hash yet
        #     else:
        #         globalHash[elem] = 1 #there is one instance of this num

        # buckets = [[] for _ in range(len(nums) + 1)]


        # #sort the list by value, then return the key for the x highest values
        # #get all key value pairs sorted by values
        # sortedRes = sorted(globalHash.items(), key= lambda x: x[1], reverse=True)
        # res = [x for (x,y) in sortedRes[:k]]

        globalHash = {}

        for number in nums:
            #if key not in hash
            if number not in globalHash:
                globalHash[number] = 0 
            
            globalHash[number] +=1

        #O(10001) = constant
        buckets = [[] for _ in range(len(nums) + 1)]

        #O(n) run through of dictionary
        for key, value in globalHash.items():
            buckets[value].append(key)

        resultList = []
        for bucket in buckets[::-1]: #10001
            for num in bucket: #2001 = 20,000,000 = constant
                if len(resultList) == k:
                    break
                else:
                    resultList.append(num)
        
        return resultList
                

 
        

#Constraints
#Aim for O(n) time and O(n) space
#between 1 and 10000 numbers in list
#individual nums between -1000 and 1000
#There are no cases where 2 nums occur the same number of times unless k is not large enough to encapsulate that

#Brute Force
#make a 2001 len array, 0 = ind 1000, neg nums = 0-999, increment counters than iterate through and return
#the k top

#Optimisation | O(n log n) time and O(n) space
#Make a return list = [k length * 0]
#Make a hashmap
#For every element hash it to find index then increment by 1
#O(constant checks) -> if it is greater than return[0] then increment -> shift rest of list bla bla
#O(k * n) time and O(n) spacee

#Edge Case