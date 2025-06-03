class TimeMap:

    def __init__(self):
        self.store = {} # key = string and value is [list of [val,time]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" # default return is empty string
        
        values = self.store.get(key, []) # list of current values in dictionary

        #binary search
        
        l, r = 0, len(values) -1
        
        while l <= r:
            mid = (l+r) // 2 

            if values[mid][1] <= timestamp: # check if valid
                res = values[mid][0] # if valid update the result
                l = mid + 1

            else:
                r = mid - 1
        return res



