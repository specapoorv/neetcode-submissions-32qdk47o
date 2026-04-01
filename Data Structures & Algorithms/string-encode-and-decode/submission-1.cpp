class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_str;
        encoded_str.reserve(100000);
        for (string &str : strs) {
            encoded_str += to_string(str.size());
            encoded_str += '#';
            encoded_str += str;
        }

        return encoded_str;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        string temp_str;
        string len;
        string str;

        for (int i=0; i<s.size(); ++i){
            if (s[i] == '#'){
                int len_i = stoi(len);
                len = "";
                str = s.substr(i + 1, len_i);
                strs.push_back(str);
                i = i + len_i;
                continue;
            }
            len += s[i];
        }
        return strs;
    }
};
