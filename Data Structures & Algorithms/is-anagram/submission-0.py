class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

#ord(letter) - ord('a')
# ord(letter) = values 91-122 - ord('a') = values 0-26
        
# only contains lowercase english letters e.g. a-z

# naive approach
# check string length is equal
# for every letter check if it is in the other string
# remove letter from both strings
# continue = O(n^2 comp) O(n) space

# hash approach?
# therefore, we can hash with values 1-26 with a counter for how many times
# a letter occurs in string s, then check if the same hash array occurs for string t
# when both are hashed, return early if the value at a given hash is not the same for a letter
# O(2n to hash + O(n) to check if same = O(n) time & space via hashing)

        # hash function = ord(letter) - ord('a')
        first = [0] * 26
        second = [0] * 26

        for letter in s:
            index = ord(letter) - ord('a')
            first[index] +=1

        for letter in t:
            index = ord(letter) - ord('a')
            second[index] +=1
        # now both strings have been hashed and each index contains the number of occurances of the char in s/t

        for i in range(len(first)): # 26 times 0 ... 25
            if first[i] != second[i]:
                return False
        return True
