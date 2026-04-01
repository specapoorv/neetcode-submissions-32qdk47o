class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        vector<int> freq_s(26, 0);
        vector<int> freq_t(26, 0);

        for (char c : s) {
            int index = c - 'a';
            freq_s[index]++;
        }
        for (char c : t) {
            int index = c - 'a';
            freq_t[index]++;
        }

        for (int i=0; i<26; i++) {
            if (freq_s[i] != freq_t[i]) return false;
        }
        return true;
    }
};
