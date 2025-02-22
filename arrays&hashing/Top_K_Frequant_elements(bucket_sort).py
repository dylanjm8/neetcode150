class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
# frequancy is a list of lists to accommodate for the key values from the count hash map that are to be inserted
        frequency = [[]for i in range(len(nums)+1)] # + 1 since a 0 value in this case is useless since 0 occurrences shouldn't be included
        for n in nums: # for each value in nums, count the number of occurrences it has in the list
            count[n] = 1 + count.get(n,0) # defualt 0 occurrences but add one if found
        for n, c in count.items(): # n,c format grabs the key and value, could be any variable
            frequancy[c].append(n) # at c (value) index of array which represents the frequency in the input, insert the corresponding number to the new array
       # above is backwards variables so that the value count of the numbers can become the index, and the number becomes the value
# getting the highest frequency elements in the array and putting them into the output array
        res = []
        for i in range((len(frequency) -1), 0 , -1): # from length-1 to 0 going in -1 order
            for n in frequancy[i]:
                res.append(n)
                if len(res) == k: # once the result array reaches the k size we know to return it since the question is looking for the k number of most frequent elements 
                    return res
