class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        lettersFirst = [0] * 26
        lettersSecond = [0] * 26
        offset = 97 #97 is ascii value for 'a' and there are 26 letters in lowercase alphabet

        for char in s:
            lettersFirst[ord(char) - offset] +=1

        for char in t:
            lettersSecond[ord(char) - offset] +=1
        
        return lettersFirst == lettersSecond

        
#Constraints
#All lowercase letters

#Brute Force
#create two hashes, which is O(n+m) space, fill by iterating
#through strings and compare if equal which is o(n+m) time

#Edge Cases