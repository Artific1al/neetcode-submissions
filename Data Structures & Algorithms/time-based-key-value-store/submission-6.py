class TimeMap:
    #key and value only include lowercase English letters and digits.
    #use a finite hash map and make each letter and digit have an array, the arrays sorted by timestamp w
    #binary search

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #case 1 this key has not been seen before
        #stored as key, value, timestamp
        if self.hash.get(key, None) == None:
            self.hash[key] = [[key, value, timestamp]]
        #case 2 there is already an array w at least one element here
        else:
            self.hash[key].append([key, value, timestamp])

        #bin search so O(log n) time
    def get(self, key: str, timestamp: int) -> str:

        r = len(self.hash.get(key, [])) - 1
        #if empty hash
        if r == -1:
            return ""
        
        l = 0
        r = len(self.hash.get(key, 0)) - 1
        m = (l+r) // 2
        arr = self.hash.get(key)
        largest = m #so that single element arrays can return correctly

        
        while l <=r:

            #return val
            if arr[m][2] == timestamp:
                return arr[m][1]

            #too large
            elif arr[m][2] > timestamp:
                r = m - 1
                m = (l + r) //2
            
            else:
                largest = m #useful for returning the largest value smaller than m
                l = m + 1
                m = (l+r) // 2
                

        #if there is a value smaller than the timestamp, return the largest one of those
        return arr[largest][1] if arr[largest][2] < timestamp else ""
        
        
#constraints

#edge cases

#brute force
#make a hash in init
#when setting check if it exists, if it does not add the element to an array then append the array,
#else just append the element to the internal array at that spot, and because timestamps are
#strictly increasing this is a sorted list of the order in which they were added
#get - binary search through that portion of the array