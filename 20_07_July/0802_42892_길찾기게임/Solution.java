import java.util.ArrayList;
import java.util.Arrays;

class Solution {

    private static class Node {
        private int x;
        private int y;
        private int value;
        private Node left;
        private Node right;

        public Node(int x, int y, int value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }

        public void findPreOrder(ArrayList<Integer> routine) {
            routine.add(this.value);

            if (left != null) {
                left.findPreOrder(routine);
            }

            if (right != null) {
                right.findPreOrder(routine);
            }
        }

        public void findPostOrder(ArrayList<Integer> routine) {

            if (left != null) {
                left.findPostOrder(routine);
            }

            if (right != null) {
                right.findPostOrder(routine);
            }

            routine.add(this.value);
        }

    }

    private static class Tree {
        private Node root;
        private int size;

        public void addNode(Node node) {
            ++size;

            if (root == null) {
                root = node;
                return;
            }

            Node tmp = root;

            while (true) {

                if (node.x < tmp.x) {
                    if (tmp.left == null) {
                        tmp.left = node;
                        return;
                    } else {
                        tmp = tmp.left;
                    }
                } else {
                    if (tmp.right == null) {
                        tmp.right = node;
                        return;
                    } else {
                        tmp = tmp.right;
                    }
                }

            }

        }

        public int[] getPreOrderRoutine() {
            ArrayList<Integer> routine = new ArrayList<Integer>(size);

            if (root != null) {
                root.findPreOrder(routine);
            }

            return routine.stream().mapToInt(x -> x).toArray();
        }

        public int[] getPostOrderRoutine() {
            ArrayList<Integer> routine = new ArrayList<Integer>(size);

            if (root != null) {
                root.findPostOrder(routine);
            }

            return routine.stream().mapToInt(x -> x).toArray();
        }


    }

    private int compareNodes(Node a, Node b) {
        // y 내림차순 > x 오름차순
        return (a.y != b.y) ? -Integer.compare(a.y, b.y) : Integer.compare(a.x, b.x);
    }


    public int[][] solution(int[][] nodeinfo) {
        Tree tree = new Tree();
        Node[] nodes = new Node[nodeinfo.length];

        for (int i = 0; i < nodeinfo.length; i++) {
            nodes[i] = new Node(nodeinfo[i][0], nodeinfo[i][1], i + 1);
        }

        Arrays.sort(nodes, this::compareNodes);

        for (Node node : nodes) {
            tree.addNode(node);
        }

        return new int[][] { tree.getPreOrderRoutine(), tree.getPostOrderRoutine() };
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] reuslt = sol.solution(new int[][] {{5, 3}, {11, 5}, {13, 3}, {3, 5}, {6, 1}, {1, 3}, {8, 6}, {7, 2}, {2, 2}});
    }

}