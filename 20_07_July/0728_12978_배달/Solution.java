import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {

    private static class Edge {
        private int to;
        private int cost;

        public Edge(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }

    private static class Node {
        private int id;
        private int minimumCost = Integer.MAX_VALUE;
        private ArrayList<Edge> edges = new ArrayList<>();
        
        public Node(int id) {
            this.id = id;
        }

        public void addEdge(Edge edge) {
            this.edges.add(edge);
        }

        public Iterable<Edge> getEdgeIter() {
            return edges;
        }
    }


    public int solution(int N, int[][] road, int K) {
        Node[] nodes = new Node[N + 1];
        Queue<Node> queue = new LinkedList<>();
        
        // N개 노드 초기화
        for (int i = 1; i <= N; i++) {
            nodes[i] = new Node(i);
        }
        
        // 간선 등록
        for (int[] r : road) {
            int from = r[0];
            int to = r[1];
            int cost = r[2];

            nodes[from].addEdge(new Edge(to, cost));
            nodes[to].addEdge(new Edge(from, cost));
        }
        
        // 1번 정점에서 시작
        nodes[1].minimumCost = 0;
        queue.add(nodes[1]);
        
        // 모든 노드를 순회할 때 까지
        while (queue.isEmpty() == false) {
            Node n = queue.poll();

            for (Edge e : n.getEdgeIter()) {
                int tmpCost = n.minimumCost + e.cost;

                if (tmpCost < nodes[e.to].minimumCost) {
                    nodes[e.to].minimumCost = tmpCost;
                    queue.add(nodes[e.to]);
                }
            }
        }


        return (int) Arrays.stream(nodes)
                .skip(1) // 맨 앞 0번째 node는 null이다.
                .filter(n -> n.minimumCost <= K)
                .count();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.solution(5, new int[][] {
                {1, 2, 1},
                {2, 3, 3},
                {5, 2, 2},
                {1, 4, 2},
                {5, 3, 1},
                {5, 4, 2}
        }, 3) == 4;
    }
}