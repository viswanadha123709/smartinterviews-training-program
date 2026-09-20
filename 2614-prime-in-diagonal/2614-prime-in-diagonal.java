import java.util.*;
class Solution {
    public int diagonalPrime(int[][] nums) {
        int maxi=(int) Math.pow(10,6);
        boolean[] arr= new boolean[(4*maxi)+1];
        int n=nums.length;

        for(int i=0;i<=4*maxi;i++){
            arr[i]=true;
        }
        arr[1]=false;
        arr[0]=false;

        for (int i=2;i<=Math.sqrt(4*maxi);i++){
            if (arr[i]==true)
            {
                for (int j=i*i ; j<=4*maxi ; j+=i){
                    arr[j]=false;
                }
            }
        }
        ArrayList<Integer> diag=new ArrayList<>();
        for (int i=0;i<n;i++){
            diag.add(nums[i][i]);
            diag.add(nums[i][n-i-1]);
        }
        int ans=0;
        for (int i:diag){
            if (arr[i]){
                ans=Math.max(ans,i);
            }
        }
        return ans;
    }
} 