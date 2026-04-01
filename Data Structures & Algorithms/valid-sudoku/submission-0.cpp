class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> row(9, vector<int>(9, 0));
        vector<vector<int>> col(9, vector<int>(9, 0));
        vector<vector<int>> box(9, vector<int>(9, 0));

        for(int i=0; i<board.size(); ++i){
            for(int j=0; j<board[i].size(); ++j) {
                if (board[i][j] == '.') continue;
                int digit = board[i][j] - '1';
                if (row[i][digit]){ return false;}
                row[i][digit]++;
                if (col[j][digit]){ return false;}
                col[j][digit]++;

                int row_div = i / 3;
                int col_div = j / 3;
                int box_index = 3*row_div + col_div;

                if (box[box_index][digit]){ return false;}
                box[box_index][digit]++;    

            }
        }
        return true;                         

    }
};
