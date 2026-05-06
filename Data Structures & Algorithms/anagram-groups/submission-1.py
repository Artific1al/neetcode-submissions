class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        bigHash = {}
        offset = 97

        for current in strs: #O(m)

            smallHash = [0] * 26 
            
            #populate per string array
            for char in current:#O(n)
                smallHash[ord(char)-97] +=1

            #python keys in hashes must be immutable, so convert the list into a tuple
            #python does some super smart bs in the background and creates a hash function
            #to represent this tuple
            smallTuple = tuple(smallHash)
            
            #if that arrangement of chars exists already, add the next string
            if smallTuple in bigHash:
                bigHash[smallTuple] = bigHash[smallTuple] + [current]

            #if not make a list of just [current]
            else:
                bigHash[smallTuple] = [current]
        
        
        resList = []
        for arrangements in bigHash:
            resList.append(bigHash[arrangements])
        
        return resList



#Constraints
#Lowercase english letters
#strs.length between 1 and 1000
#m * n complexity, m space, n is longest string

#Brute Force
#Make a hashmap of len 26 for each string, then iterate through all of them
#and group the ones that are identical

#Idea O(m*n) time and O(m*constant) space
#For each list, create a len 26 hashmap (O(m*n))
#Then, create an overall hashmap
#Then, everytime a hashmap already has a value, make it a list
#Then, return the lists

#Edge Cases