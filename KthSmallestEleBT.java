class KthSmallestEleBT {

    int count = 0;
    int res = 0;

    public static void main(String[] args) {
        
        TreeNode node2 = new TreeNode(2, null, null);
        TreeNode node4 = new TreeNode(4, null, null);
        TreeNode node1 = new TreeNode(1, null, node2);
        TreeNode node3 = new TreeNode(3, node1, node4);

        
        KthSmallestEleBT ans = new KthSmallestEleBT();
        System.out.println(ans.kthSmallest(node3, 1));


    }

    public int kthSmallest(TreeNode root, int k) {
        helper(root, k);
        return res;
    }

    private void helper(TreeNode root, int k) {
        if (root == null || count >= k) {
            return ;
        }

        helper(root.left, k);
        
        count++;
        if (count == k) {
            res = root.val;
            return;
        }

        helper(root.right, k);
    }
}

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

