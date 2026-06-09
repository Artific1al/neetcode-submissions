class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


            #idea brute force -> hash map for both long and short with # of each char
            #for char in long, l,r = 0 
            #if l -r = len(shorter string) return true
            #if r not in short hashMap or exeed quantity - empty out long hashmap and move l and r to be r
            #else r in short hashMap & not exceed quantity r+=1
            

            #vars
            l = 0
            r = 0
            shorter = [0] * 26
            longer = [0] * 26
            
            longest, shortest = s2, s1
            

            if len(shortest) > len(longest):
                return False

            #shortest hash initialisation
            for elem in shortest:
                shorter[ord(elem)-97] +=1

            while r <= (len(longest)-1):

                #check if we succeed
                if r-l == len(shortest):
                    return True

                required = shorter[(ord(longest[r]))-97]
                current = longer[(ord(longest[r]))-97]

                #if this is a necessary char and we dont have too many
                if((current + 1 <= required) and (required > 0)):
                    longer[ord(longest[r])-97] +=1 #increment counter
                    r+=1

                #reset value
                else:

                    if required > 0 and longest[l] == longest[r]:
                        l+=1
                        r+=1

                    else:
                        for ind in range(len(longer)):
                            longer[ind] = 0
                
                        r+=1
                        l = r
                    
            

            #outcome
            return r-l == len(shortest)




#wrong understanding of permutations -> "bac" is a permutation of "abc" but "bsdclkja" is not a permutation
#of "abc"
#longest string time and o1 space

#brute force
#two hash maps, check if longer string has all of shorter string -> then true else false
#both strings only contain lowercase letters

        # #O(1) hmap since only lowercase letters
        # hMap = [None] * 26
        
        # #get short / long
        # longest, shortest = s1, s2
        # if len(s2) > len(s1):
        #     longest = s2
        #     shortest = s1

        # for char in longest:
        #     hMap[ord(char)-97] = True
        
        # for char in shortest:
        #     if hMap[ord(char)-97] != True:
        #         return False

        # return True



