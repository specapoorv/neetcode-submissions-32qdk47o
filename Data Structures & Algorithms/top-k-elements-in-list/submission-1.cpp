#include <bits/stdc++.h>
using namespace std;

struct Node {
    int element;
    int frequency;
};


class Heap {
private:
    vector<Node> heap;

    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1)  / 2;
            if (heap[parent].frequency > heap[index].frequency) {
                swap(heap[parent], heap[index]);
                index = parent;
            }
            else break;  
        }    
    }

    void heapifyDown(int index) {
        int size = heap.size();
        while (true) {
            int left = 2*index + 1;
            int right =  2*index + 2;
            int smallest = index;
        
            if (left < size && heap[left].frequency < heap[smallest].frequency) {
                smallest = left;
            }
            if (right < size && heap[right].frequency < heap[smallest].frequency) {
                smallest = right;
            }
            if (smallest!=index) {
                swap(heap[smallest], heap[index]);
                index = smallest;
            } else break;
        } 
    }

public:
    void insert(Node node){
        heap.push_back(node);
        heapifyUp(heap.size() - 1);
    }

    Node extract() {
        Node root = heap[0];
        swap(heap[0], heap.back());
        heap.pop_back();

        if (!heap.empty()) heapifyDown(0);

        return root;
    }

    Node peek(){
        Node root = heap[0];
        return root;
    }

    int size(){
        return heap.size();
    }

};


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int i=0; i<nums.size(); i++) {
            count[nums[i]]++;
        }

        Heap heap;
        
        for (auto i : count){
            Node node;
            node.element = i.first;
            node.frequency = i.second;

            if (heap.size()<k){
                heap.insert(node);
            } else {
                if (node.frequency > heap.peek().frequency){
                    heap.extract();
                    heap.insert(node);
                }
            }
        }

        vector<int> result;
        while (heap.size() > 0) {
            result.push_back(heap.extract().element);
        }

        return result;

    }
};
