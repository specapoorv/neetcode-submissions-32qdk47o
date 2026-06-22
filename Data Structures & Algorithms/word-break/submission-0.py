class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            temp = s[:i]
            if temp in wordDict:
                dp[i] = True
            else:
                for j in range(i):
                    if dp[j]:
                        temp2 = temp[j:i]
                        if temp2 in wordDict:
                            dp[i] = True
                            break
        
        return dp[len(s)]
            

            

        