class Solution:

    def encode(self, strs: List[str]) -> str:

  

        resString = ""
        charDivider = 'x'
        stringDivider = 'd'

        #O(m) total for these loops
        for string in strs:

            currentString = ""
            for char in string:
                currentChar = str(ord(char))
                currentString += currentChar + charDivider
            

            resString += currentString + stringDivider

        return resString        


    def decode(self, s: str) -> List[str]:
        charDivider = 'x'
        stringDivider = 'd'

        #O(m) space?
        resStrings = []
        strings = s.split(stringDivider)[:-1]

        #O(m) total
        for string in strings:
            asciiWord = string.split(charDivider)[:-1]
            word = "" 
            for char in asciiWord:
                word += chr(int(char))
            resStrings.append(word)

        return resStrings


#Constraints
#there is no "divider" because the strings can contain any of the 256 valid ascii chars
#individual string length is less than 200
#max 100 strings
#O(m) time for both, O(m+n) space 

#Brute Force
#Make one really long string seperated by some char that is not present 
#Then decode by splitting up along that
#cheat by using a non-ascii char

#O(m is sum of len of all strings)
#idea, for each string: for each char: encode the ascii number then a seperation value like x
#then, at the end of every string make a seperation char like y 
#then, decode that at other end
# Encode = O(2-3m) time complexity, and O(2-3m) space
# Decode = same?

#Edge case