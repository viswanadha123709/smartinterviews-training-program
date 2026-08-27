class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        curr = 0
        ans = ""

        for i in range(n):
            if s[i] == '1':
                curr += 1

            while curr > k:
                if s[left] == '1':
                    curr -= 1
                left += 1

            if curr == k:
                while s[left] == '0':
                    left += 1

                cur = s[left:i + 1]

                if (not ans or
                    len(cur) < len(ans) or
                    (len(cur) == len(ans) and cur < ans)):
                    ans = cur

        return ans