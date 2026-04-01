class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        pair<int, int> max = {nums[0], 0}; //element, index
        for(int i=1; i<k; i++){
            if (max.first < nums[i]) max = {nums[i], i};
        }
        ans.push_back(max.first);

        for(int i=k; i<nums.size(); i++) {
            if (i - max.second < k) {
                // prev max still in window
                if (nums[i] > max.first) max = {nums[i], i};
            }
            else {
                // prev max gone compare all k?
                max = {nums[i-k+1], i-k+1};
                for (int j=i-k+2; j<i+1; j++) {
                    if (nums[j]>max.first) max = {nums[j], j};
                }
            }
            ans.push_back(max.first);
        }

        return ans;
    }
};
