class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        
        while x:
            digit = int(math.fmod(x,10)) # step 1 (very last digit)
            x = int(x/10) # step 2 (first x digits)

            if(res > MAX // 10 or (res == MAX and digit >= MAX % 10)):
                return 0
            if(res < MIN // 10 or (res == MIN and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit

        return res
