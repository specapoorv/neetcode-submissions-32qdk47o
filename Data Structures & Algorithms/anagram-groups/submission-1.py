class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_keys = {}
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] += 1
            if tuple(count) in word_keys:
                word_keys[tuple(count)].append(word)
            else:
                word_keys[tuple(count)] = [word]

        output = [value for value in word_keys.values()]
        return output            

