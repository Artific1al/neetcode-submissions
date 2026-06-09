class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
    
#O(n) time O(m) space where m is # of unique chars

#brute force -> for every spot in the string, add all chars seen to a list. if char ever in list already
#move on to next string - n^2 time and n^2 space

#using hash map -> for every spot in string add all chars seen to hash - n^2 time and n^2 space


#edge case -> if len of longest is > remaining characters then return - you've found it
#use L R pointer, increment R and add to hash until repeat char, 
#on repeat char - first calculate max 
#then, remove all left pointer chars until you get to current char
#then continue till end (O(n) time and o(m) space?)

        cSet = set()
        l = 0
        r = 0
        maxVal = 0


        #r loop
        while r <= len(s)-1:
            idx = s[r]
           
            #check if it exists
            if idx in cSet:
                maxVal = max(maxVal, r-l) #update maxVal if needed

                #until we find same char remove all chars
                while s[l] != idx:
                    cSet.remove(s[l])
                    l+=1
                l+=1 #increment l one more time to get next

            cSet.add(s[r])

            #check if r
            #increment r
            r +=1
            
        maxVal = max(maxVal, r-l) #edge case incase whole string


        return maxVal 