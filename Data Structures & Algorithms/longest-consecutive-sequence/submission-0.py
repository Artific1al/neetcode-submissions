class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Edge case - if 1 or 0 nums, return that lengtj
        if len(nums) <=1:
            return len(nums)

        triplesHash = {} #stores triples, [num-1, num, num+1]
        seenHash = {}
        bestCount = 0 #counter for longest sequence

        #First pass - add nums to triples hash
        for num in nums:
            if num not in triplesHash: #account for duplicates
                triplesHash[num] = [None, num, None]
            
        
        #Second pass - add all -1s and +1s
        for num in nums:
            if num-1 in triplesHash: #if current num is 1 greater than something
                triplesHash[num-1][2] = num
            
            elif num+1 in triplesHash: #if current num is 1 less than something
                triplesHash[num+1][0] = num



        #Third pass 
        #For every value in 
        for num in nums: #check every num
            if not num in seenHash: #O(1) do nothing if we've already checked it

                seenHash[num] = True #so we dont check this num again
                minValue = num
                maxValue = num

                while triplesHash[minValue][0] != None: #traverse to lowest num
                    minValue -=1
                    seenHash[minValue] = True #if already assigned - does not break

                while triplesHash[maxValue][2] != None:
                    maxValue +=1
                    seenHash[maxValue] = True

                
                #traversed all nums in order
                count = maxValue -minValue + 1
                if count > bestCount:
                    bestCount = count

        return bestCount

        
        #Idea -triple pass over array = O(3n)
#First pass - fill up hashes with just the number bigHash
#Second pass, - for every number, check if that number - 1 is in there, if so change that value to [num-1, num]

#Thirs pass, make a new hash (nums -1b to pos 1b) - smallHash
#Hold two counters, current and best
#for every num, if its length is 2 (means that it has a num that comes after it) O(1 check) then increase counter by 1 and go to that num in bigHash
#to prevent repeat work, have a smallHash that checks what nums we've seen, and if we've seen that num then skip in 3rd passover
#skip it

#if count ever = len(nums) return early

#To avoid N^2 potential work in the case where you have ascending nums but the last one is the smallest
#you must store before and after nums, then go to the earliest point, then the latest point


        
        


#Constraints
#betwen 0 and 1000 nums per input
#O(n) time and space
#individual nums between positive and negative 1,000,000,000
#Cant use a sorting algorithm as must run in O(n) time
#Dont have to return the sequence -> JUST the length


#Brute Force O(N^3) 
#For every num:
#If there is a num exactly 1 higher, then record that
#Recursively repeat until end

#EdgeCases
#if size 0 or 1, return that

#Optimisations
#Can I repeat less work?
#How can O(1) lookup be helpful?

#Idea -triple pass over array = O(3n)
#First pass - fill up hashes with just the number bigHash
#Second pass, - for every number, check if that number - 1 is in there, if so change that value to [num-1, num]

#Thirs pass, make a new hash (nums -1b to pos 1b) - smallHash
#Hold two counters, current and best
#for every num, if its length is 2 (means that it has a num that comes after it) O(1 check) then increase counter by 1 and go to that num in bigHash
#to prevent repeat work, have a smallHash that checks what nums we've seen, and if we've seen that num then skip in 3rd passover
#skip it

#if count ever = len(nums) return early

#To avoid N^2 potential work in the case where you have ascending nums but the last one is the smallest
#you must store before and after nums, then go to the earliest point, then the latest point


#[2,3,4,5]
#First pass [2,20,4,10,3,4,5]
#Second pass [[2,3], 20, [4,5], 10, [3,4], [4,5], 5] 

##[3,4,5,2]
#[[2,3], [3,4], [4,5], 5]
