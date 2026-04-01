class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> seen;
        int longest{0};
        int c = 0;
        while (c<s.size()){
            if(seen.count(s[c])){
                c = seen[s[c]];
                seen.clear();
            }else {
                seen[s[c]] = c;
                if (seen.size()>longest) longest=seen.size();
            }
            c++;
        }
        return longest; 
    }
};
