import java.util.Scanner;

public class Solution {
    
    static abstract class Heap {
        int[] elems;
        int length;
        
        public Heap(int n) {
            elems = new int[n/2+2];
            length = 0;
        }
        
        public int top() {
            return elems[1];
        }
        
        public int pop() {
            int result = elems[1];
            if (length > 1) {
                elems[1] = elems[length];
                length--;
                sink(1);
            }
            return result;
        }
        
        private void sink(int i) {
            while (2*i < length) {
                int moveToIndex = 2*i;
                if (2*i+1 < length && priority(2*i+1, 2*i)) {
                    moveToIndex = 2*i+1;
                }
                if (priority(moveToIndex, i)) {
                    int tmp = elems[i];
                    elems[i] = elems[moveToIndex];
                    elems[moveToIndex] = tmp;
                    i = moveToIndex;
                } else {
                    break;
                }
            }
        }

        abstract protected boolean priority(int i, int j);

        public void insert(int e) {
            elems[length+1] = e;
            swim(length+1);
            length++;
        }

        private void swim(int i) {
            while (i > 1 && priority(i, i/2)) {
                int tmp = elems[i/2];
                elems[i/2] = elems[i];
                elems[i] = tmp;
                i /= 2;
            }
            
        }
        
        public int size() {
            return length;
        }
        
    }
    
    static class MaxHeap extends Heap {

        public MaxHeap(int n) {
            super(n);
        }

        @Override
        protected boolean priority(int i, int j) {
            return elems[i] > elems[j];
        }
        
    }
    
    static class MinHeap extends Heap {

        public MinHeap(int n) {
            super(n);
        }

        @Override
        protected boolean priority(int i, int j) {
            return elems[i] < elems[j];
        }
        
    }
    
    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        MaxHeap maxH = new MaxHeap(n);
        MinHeap minH = new MinHeap(n);

        int curr = scan.nextInt();
        maxH.insert(curr);
        System.out.println((double) curr);

        for (int i = 1; i < n; i++) {
            curr = scan.nextInt();
            if (maxH.size() > minH.size()) {
                if (curr > maxH.top()) {
                    minH.insert(curr);
                } else {
                    maxH.insert(curr);
                    int toMove = maxH.pop();
                    minH.insert(toMove);
                }
                System.out.println((maxH.top() + minH.top())/2.0);
            } else if (maxH.size() < minH.size()) {
                if (curr < minH.top()) {
                    maxH.insert(curr);
                } else {
                    minH.insert(curr);
                    int toMove = minH.pop();
                    maxH.insert(toMove);
                }
                System.out.println((maxH.top() + minH.top())/2.0);
            } else {
                if (curr > maxH.top()) {
                    minH.insert(curr);
                    System.out.println((double)minH.top());
                } else {
                    maxH.insert(curr);
                    System.out.println((double)maxH.top());
                }
            }
        }
        
    }
}
