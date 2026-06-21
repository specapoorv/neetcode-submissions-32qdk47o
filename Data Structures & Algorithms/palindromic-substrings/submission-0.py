class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.expand_and_count(i,i, s)
            count += self.expand_and_count(i,i+1, s)
        
        return count


    
    def expand_and_count(self, left: int, right: int, s) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

        