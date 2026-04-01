class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        priority_queue<pair<int,int>> pq;

        for (int i = 0; i < nums.size(); i++) {

            // 1️⃣ Push current element
            pq.push({nums[i], i});

            // 2️⃣ Remove elements outside window
            while (!pq.empty() && pq.top().second <= i - k) {
                pq.pop();
            }

            // 3️⃣ Record answer once first window is complete
            if (i >= k - 1) {
                ans.push_back(pq.top().first);
            }
        }

        return ans;
    }
};
