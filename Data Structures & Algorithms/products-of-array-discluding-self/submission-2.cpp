class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 0);
        vector<int> multiply_left(nums.size(), 0);
        vector<int> multiply_right(nums.size(), 0);
        int multiply {1};
        bool one_zero {false};
        int zero_index;
        bool multiple_zeros {false};

        for (int i=0; i<nums.size(); ++i){
            if (nums[i]==0) {
                if (!one_zero){
                    one_zero = true;
                    zero_index = i;
                } else {multiple_zeros = true;}
            }
            else{
                multiply *= nums[i];
                multiply_left[i] = multiply;
            }
        }
        multiply = 1;
        for (int i=nums.size() - 1; i>=0; --i) {
            if (nums[i]!=0){
                multiply *= nums[i];
                multiply_right[i] = multiply;
            }
        }


        if (multiple_zeros) return result;
        if (one_zero) {
            if (zero_index == 0) {
                result[zero_index] = multiply_right[1];
            }
            else if (zero_index == nums.size() - 1) {
                result[zero_index] = multiply_left[nums.size() - 2];
            }
            else {
                result[zero_index] = multiply_left[zero_index - 1] * 
                                    multiply_right[zero_index + 1];
            }
            return result;
        }

        for (int i=0; i<nums.size(); ++i) {
            if (i==0){
                result[i] = multiply_right[i+1];
            }
            else if (i==nums.size()-1) {
                result[i] = multiply_left[i-1];
            }
            else{
                result[i] = multiply_left[i-1] * multiply_right[i+1];
            }
        }

        return result;
    }

};
