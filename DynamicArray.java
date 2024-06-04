import java.util.Arrays;

class DynamicArray{
    int capacity;
    int[] arr;
    int index;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.index = 0;
        this.arr = new int[capacity];
    }

    public int get(int i) {
        if (i < index) {
            return arr[i];

        }
        return -1;
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public int getSize() {
        return this.index;
    }

    public int popback() {
        if (this.index == 0){
            throw new IllegalStateException("Array Is Empty");
        }

        return this.arr[this.index--];
    }

    public void pushback(int n) {
        this.resize();
        this.arr[this.index] = n;
        this.index++;
    }

    public void resize() {
        this.capacity = 2 * this.capacity;
    }
    
    public int getCapacity() {
        return this.capacity;
    }

    public void print() {
        for (int i = 0; i < index; i++) {
            System.out.print(arr[i]);
        }
    }


    public static void main(String[] args) {
        DynamicArray arr = new DynamicArray(10);
        arr.pushback(1);
        arr.print();
        arr.pushback(2);
        arr.print();

        arr.pushback(3);
        arr.print();

        arr.pushback(4);
        arr.print();
        arr.pushback(5);
        arr.print();

        arr.pushback(6);
        arr.print();

        System.out.println(arr.getSize());
        arr.set(3,10);
        System.out.println(arr.getSize());
    
        System.out.println(arr.getSize());
    }
}
