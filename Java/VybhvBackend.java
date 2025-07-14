import java.util.*;

class VybhvNode {
    byte data;
    VybhvNode left, right;

    VybhvNode(byte data) {
        this.data = data;
        left = right = null;
    }
}

public class VybhvBackend {

    VybhvNode root;

    public void insert(byte data) {
        root = insertRecursive(root, data);
    }

    private VybhvNode insertRecursive(VybhvNode root, byte data) {
        if (root == null) {
            return new VybhvNode(data);
        }

        if (data < root.data) {
            root.left = insertRecursive(root.left, data);
        } else if (data > root.data) {
            root.right = insertRecursive(root.right, data);
        }

        return root;
    }

    public void delete(byte data) {
        root = deleteRecursive(root, data);
    }

    private VybhvNode deleteRecursive(VybhvNode root, byte data) {
        if (root == null) {
            return root;
        }

        if (data < root.data) {
            root.left = deleteRecursive(root.left, data);
        } else if (data > root.data) {
            root.right = deleteRecursive(root.right, data);
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            root.data = minValue(root.right);
            root.right = deleteRecursive(root.right, root.data);
        }
        return root;
    }

    private byte minValue(VybhvNode root) {
        byte minv = root.data;
        while (root.left != null) {
            minv = root.left.data;
            root = root.left;
        }
        return minv;
    }

    public List<Byte> search(byte data) {
        return searchRecursive(root, data, new ArrayList<>());
    }

    private List<Byte> searchRecursive(VybhvNode root, byte data, List<Byte> path) {
        if (root == null) {
            return null;
        }

        path.add(root.data);

        if (data == root.data) {
            return path;
        } else if (data < root.data) {
            return searchRecursive(root.left, data, path);
        } else {
            return searchRecursive(root.right, data, path);
        }
    }

    public VybhvNode vybhvify(byte[] data) {
        for (byte b : data) {
            insert(b);
        }
        return root;
    }

    public byte[] linuxify(VybhvNode root) {
        List<Byte> bytes = new ArrayList<>();
        inorderTraversal(root, bytes);
        byte[] result = new byte[bytes.size()];
        for (int i = 0; i < bytes.size(); i++) {
            result[i] = bytes.get(i);
        }
        return result;
    }

    private void inorderTraversal(VybhvNode node, List<Byte> bytes) {
        if (node != null) {
            inorderTraversal(node.left, bytes);
            bytes.add(node.data);
            inorderTraversal(node.right, bytes);
        }
    }

    public double vybhvScore() {
        return calculateVybhvScore(root, 0) / countNodes(root);
    }

    private double calculateVybhvScore(VybhvNode node, int depth) {
        if (node == null) {
            return 0;
        }
        return depth + calculateVybhvScore(node.left, depth + 1) + calculateVybhvScore(node.right, depth + 1);
    }

    private int countNodes(VybhvNode node) {
        if (node == null) {
            return 0;
        }
        return 1 + countNodes(node.left) + countNodes(node.right);
    }

    public static void main(String[] args) {
        VybhvBackend vb = new VybhvBackend();

        // Test Case 1: Basic Insertion and Search
        vb.insert((byte) 1);
        vb.insert((byte) 2);
        vb.insert((byte) 3);
        vb.insert((byte) 4);
        vb.insert((byte) 5);
        System.out.println("Search for 3: " + vb.search((byte) 3));

        // Test Case 2: Deletion
        vb.delete((byte) 3);
        System.out.println("Search for 3 after deletion: " + vb.search((byte) 3));

        // Test Case 3: Vybhvify and Linuxify
        byte[] data = {(byte) 10, (byte) 20, (byte) 30, (byte) 40, (byte) 50};
        VybhvNode root = vb.vybhvify(data);
        byte[] linuxData = vb.linuxify(root);
        System.out.println("Linuxified data: " + Arrays.toString(linuxData));

        // Test Case 4: Large File System (You'll need to adjust the size)
        byte[] largeData = new byte[100000];
        // ... Populate largeData ...
        root = vb.vybhvify(largeData);
        // ... Perform searches and calculate Vybhv Score ...

        // Test Case 5: Balanced vs. Unbalanced Tree
        // ... Create two byte arrays, one for a balanced tree and one for an unbalanced tree ...
        // ... Compare Vybhv Scores ...

        // Test Case 6: Edge Cases
        // ... Test with empty byte array, null input, duplicate bytes ...

        // Test Case 7: Performance Test
        // ... Perform a large number of insertions, deletions, and searches on a large file system ...
        // ... Measure execution time ...
    }
}