class Solution {
    public int getSum(int a, int b) {
        while (b != 0){ //until carry is = 0
            int tmp = (a & b) << 1; 
            a = a ^ b; // This is the sum value
            b = tmp; // this is the carry

        }
        return a;
    }
}
