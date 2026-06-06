import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Main. */
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
            int n=sc.nextInt();
            int[] arr= new int[n];
            for(int r=0;r<n;r++)
            {
                arr[r]=sc.nextInt();
            }
            long ans=0;
            for (int i=0;i<31;i++)
            {
                int count=0;
                for(int j=0;j<n;j++)
                {
                    if (((arr[j]>>i)&1 )== 1)
                    {
                        count+=1; 
                    }
                }
                ans +=( (count * (n-count) )* (1L<<i));
            }
            System.out.println(2*ans);
        }
    }
}
