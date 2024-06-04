import java.util.ArrayList; 

class Heap <T extends Comparable<T>>{


    private ArrayList<T> list;
    public Heap() {
        list = new ArrayList<>();
    }

    public void swap(int first, int second) {
        T temp = list.get(first);
        list.set(first, list.get(second));
        list.set(second, temp);
    }

    private int parent(int index) {
        return (index - 1) / 2 ;
    }
  
    private int left(int index) { 
        return (2 * index) + 1;
    }

    private int right(int index) { 
        return (2 * index) + 2;
    }


    public static int insert(T val) {
        list.add(val);
        uphead(list.size() - 1);
    }

    private void uphead(int index) {
        if (index == 0) return;
        int p = parent(index);

        if (list.get(index).compareTo(list.get(p))) swap(index, p);
    }

    public T remove() throws Exception {
        if (list.isEmpty()) {
            throw new Exception("removing from an empty heap!");
        }

        T temp = list.get(0);

        T last  = list.remove(list.size() - 1);
        if (!list.isEmpty()) {
            list.set(0, last); 
            downheap(0);
        }
        returm temp;
    }

    public void downheap(int index) {
        int min = index;
        int left = left(index);
        int right = rigtht(index);

        if (left < list.size && list.get(min).compareTo(list.get(left)) > 0) {
            min = left;
        }

        if (left < list.size && list.get(min).compareTo(list.get(rightt)) > 0) {
            min = right;
        }

        if (min != index) {
            swap(min, index);
            downhead(min);
        }
    }

    public ArrayList<T> heapSort() throws Exception {
        ArrayList<T> data = new ArrayList<>();
        while (!list.isEmpty()){
            data.add(this.remove());
        }
        return data;
    }
}
