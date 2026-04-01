class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result {0};
        unordered_set<int> hash;
        for (int num : nums) {
            hash.insert(num);
        }
        
        for (int i=0; i<nums.size(); i++){
            int count {1};
            int start = nums[i];
            int prev {start - 1};
            int next {start + 1};
            if (hash.find(prev) == hash.end()){
                while (hash.find(next) != hash.end()) {
                    count++;
                    next++;
                }

                if (count > result) result = count;
            }
        }

        return result;

    }
};
