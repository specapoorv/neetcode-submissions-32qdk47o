class MinStack {
public:
    stack<int> main_stack;
    stack<int> min_stack; 

    MinStack() {}
    
    void push(int val) {
        main_stack.push(val);
        if(min_stack.empty() || min_stack.top()>=val) min_stack.push(val);
    }
    
    void pop() {
        if (main_stack.top()==min_stack.top()) min_stack.pop();
        main_stack.pop();
    }

    int top() {
        return main_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};
