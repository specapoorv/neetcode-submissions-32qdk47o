class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest_so_far{prices[0]};
        int best_profit{0};
        for (int i=1; i<prices.size(); ++i){
            int profit = prices[i] - lowest_so_far;
            if (profit>best_profit) best_profit = profit;
            if (prices[i]<lowest_so_far) lowest_so_far=prices[i];
        }
        return best_profit;
    }
};
