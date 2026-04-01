class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> count; //count of char in s1 string
        unordered_map<char, int> count_subs;
        bool flag = false;

        int window = s1.size();
        for (char c : s1){count[c]++;}

        string subs = s2.substr(0, window);
        for (char c : subs) {count_subs[c]++;}

        if (count==count_subs) flag=true;

        for (int i=window; i<s2.size(); i++){
            count_subs[s2[i-window]]--;
            if (count_subs[s2[i-window]] == 0) count_subs.erase(s2[i-window]);
            count_subs[s2[i]]++;
            if (count==count_subs) flag=true;
        }

        return flag;

    }
};
