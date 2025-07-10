class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1 #shifting n by i to right
            res = res | (bit<<(31 - i))
        return res
