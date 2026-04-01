class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 0);
        int multiple {1};
        bool includes1_zero {false};
        bool includes_zeros {false};
        int zero_index;
        for (int i=0; i<nums.size(); ++i){
            if (nums[i] == 0){
                if (includes1_zero == false) {
                    includes1_zero = true;
                    zero_index = i;
                }
                else {includes_zeros = true;}
            }
            else {multiple *= nums[i];}
        }

        if (includes_zeros) {return result;}
        if (includes1_zero) {
            result[zero_index] = multiple;
            return result;
        }else{
            for (int i=0; i<nums.size(); ++i){
                int result_i = multiple / nums[i];
                result[i] = result_i;
            }
            return result;
        }
        


    }
};
