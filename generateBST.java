import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class generateBST {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,8,10};
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 1; i < 11; i++) {
            list.add(i);
        }

        System.out.println(list);
        Node newNode = new Node(0);
     
        generateBST Tree = new generateBST();
        Node root = Tree.makeTree(list);
        
        for (ArrayList<Integer> level : Tree.displayTree(root)) {
            System.out.print("Level = ");
            for (int ele : level) {
                System.out.print(ele + " ");
            }
            System.out.println();
        }
        
    } 

    public Node makeTree(ArrayList<Integer> arr) {
        int size = arr.size();

        if (size == 0) {
            return null;
        }

        int middle = size / 2;

        Node root = new Node (arr.get(middle));
        root.left = makeTree(new ArrayList<>(arr.subList(0, middle)));
        root.right = makeTree(new ArrayList<>(arr.subList(middle + 1, size)));

        return root;


    }

    public ArrayList<ArrayList<Integer>>  displayTree(Node root) {
        if (root == null) {
            return new ArrayList<>(null);
        }

        Queue<Node> q = new LinkedList<>();
        q.add(root);
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();

        while (!q.isEmpty()) {
            int qLen = q.size();
            ArrayList<Integer> level = new ArrayList<>();

            for (int i = 0; i < qLen; i++) {
                Node curr = q.poll();
                level.add(curr.val);
                if (curr.left != null) 
                    q.add(curr.left); 
                if (curr.right != null)
                    q.add(curr.right);
            }
            res.add(level);
        }
        return res;
    }
    
    static class Node {
        int val;
        Node right;
        Node left;
        

        public  Node (int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        public Node (int val) {
            this.val = val;
        }
    }
}
