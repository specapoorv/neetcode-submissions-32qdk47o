class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> operands;
        for (int i=0; i<tokens.size(); i++) {
            if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/"){
                char op = tokens[i][0];
                int a = operands.top();
                operands.pop();
                int b = operands.top();
                operands.pop();
                operands.push(applyOp(b, a, op));
            }
            else{
                int num = stoi(tokens[i]);
                operands.push(num);
            }
        }
        return operands.top();
    }

    int applyOp(int a, int b, char op){
        if(op == '+') return a + b;
        if(op == '-') return a - b;
        if(op == '*') return a * b;
        if(op == '/') return a / b;
        return 0;
    }
};
