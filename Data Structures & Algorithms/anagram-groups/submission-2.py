class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in sorted_strs:
                sorted_strs[sorted_word].append(word)
            else:
                sorted_strs[sorted_word] = [word]               

        output = [value for value in sorted_strs.values()]
        return output
