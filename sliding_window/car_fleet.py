class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## PROBLEM
        # position and speed arrays
        # cars can't pass each other, one lane (stack) and no overlap (car fleet)
        # fleet -> stack of cars, one car could be a car fleet
        # Read like slopes of pos,time

        ## SLTN     
        # linear time o(n)
        # determine fleets by finding if the previous car will reach faster than the car in front of it
        # (distance to go) / speed = time to reach destination
        # behind car takes speed of front car, cars could change speeds, (add to stack) in reverse. 
        pair = [[p , s] for p, s in zip(position, speed)] # making an array of pairs for distance and speeds (combining)
        # zip combines two iterables to one list
        print(pair)
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse order and sort stack
            stack.append((target - p) / s) # where target is 10 
            if len(stack) >= 2 and stack[-1] <= stack [-2]: # if stack has more than one fleet and 2nd is closing faster than first
                stack.pop() # pop ( create one fleet by 'combining' two cars to one)
        
        return len(stack)
        ## END
        # Return -> total number of car fleets that arrive at the destination 
        # Destination = position 10
