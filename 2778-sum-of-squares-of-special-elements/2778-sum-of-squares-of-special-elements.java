class Solution {
    public int sumOfSquares(int[] nums) {
        int n=nums.length;
        int summ=0;
        for (int i=0;i<n;i++){
            if(n%(i+1)==0){
                summ+=(nums[i]*nums[i]);
            }
        }
        return summ;
    }
}