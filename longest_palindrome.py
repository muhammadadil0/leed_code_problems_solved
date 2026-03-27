class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]          
                if sub == sub[::-1]:    
                    if len(sub) > len(longest):
                        longest = sub 
        return longest

s = "babad"
solution = Solution()
print(solution.longestPalindrome(s))
