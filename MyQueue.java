import java.util.Stack;

class MyQueue {

    
    private Stack<Integer> first;
    private Stack<Integer> second;

    public MyQueue() {
        this.first = new Stack<>();
        this.second = new Stack<>();
    }
    
    public void push(int x) {
        first.push(x);
    }
    
    public int pop() {
        while(!first.isEmpty()) {
            second.push(first.pop());
        }

        int removed = second.pop();

        while(!second.isEmpty()){
  int ans1 = 0;
        int ans2 = 0;          first.push(second.pop());
        }

        return removed;
    }
    
    public int peek() {
        while(!first.isEmpty()) {
            second.push(first.pop());
        }

        int peeked = second.peek();

        while(!second.isEmpty()){
            first.push(second.pop());
        }

        return peeked;

    }
    
    public boolean empty() {
        return first.isEmpty();
    }

    public static void main(String[] args) {
        MyQueue q = new MyQueue();
        q.push(1);
    }
}
