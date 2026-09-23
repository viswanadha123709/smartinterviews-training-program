import java.util.*;

class Solution {
    int m, n;
    String s, p;
    Boolean[][] dp;

    public boolean isMatch(String s, String p) {
        this.s = s;
        this.p = p;

        m = s.length();
        n = p.length();

        dp = new Boolean[m + 1][n + 1];

        return fun(0, 0);
    }

    private boolean fun(int p1, int p2) {

        // Both string and pattern finished
        if (p1 == m && p2 == n) {
            return true;
        }

        // Pattern finished but string remains
        if (p2 == n) {
            return false;
        }

        // String finished
        if (p1 == m) {
            while (p2 < n) {
                if (p.charAt(p2) != '*') {
                    return false;
                }
                p2++;
            }
            return true;
        }

        // Already calculated
        if (dp[p1][p2] != null) {
            return dp[p1][p2];
        }

        // '*'
        if (p.charAt(p2) == '*') {

            // Skip consecutive '*'
            while (p2 + 1 < n && p.charAt(p2 + 1) == '*') {
                p2++;
            }

            // '*' matches:
            // 1. zero characters
            // 2. current character
            return dp[p1][p2] =
                    fun(p1, p2 + 1) ||
                    fun(p1 + 1, p2);
        }


        if (p.charAt(p2) == '?' ||
            s.charAt(p1) == p.charAt(p2)) {

            return dp[p1][p2] =
                    fun(p1 + 1, p2 + 1);
        }

        return dp[p1][p2] = false;
    }
}