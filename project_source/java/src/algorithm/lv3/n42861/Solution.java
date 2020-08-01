package algorithm.lv3.n42861;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.PriorityQueue;

public class Solution {

    private static class DisjointSet {
        private ArrayList<HashSet<Integer>> sets = new ArrayList<>();

        public DisjointSet(int n) {

            // to make sets
            for (int i = 0; i < n; i++) {
                HashSet<Integer> set = new HashSet<Integer>();

                set.add(i);

                sets.add(set);
            }
        }

        public int getSetCount() {
            return sets.size();
        }

        public HashSet<Integer> findOrNull(int n) {
            for (HashSet<Integer> set : sets) {
                if (set.contains(n)) {
                    return set;
                }
            }

            return null;
        }

        public void union(HashSet<Integer> a, HashSet<Integer> b) {
            for (Integer i : b) {
                a.add(i);
            }

            sets.remove(b);
        }

    }

    private static class Edge {
        private int cost;
        private int from;
        private int to;

        public Edge(int from, int to, int cost) {
            this.from = from;
            this.to = to;
            this.cost = cost;
        }
    }

    private int compareEdges(Edge a, Edge b) {
        return Integer.compare(a.cost, b.cost);
    }

    public int solution(int n, int[][] costs) {
        DisjointSet set = new DisjointSet(n);
        PriorityQueue<Edge> edges = new PriorityQueue<>(this::compareEdges);
        int total = 0;

        for (int[] cost : costs) {
            edges.add(new Edge(cost[0], cost[1], cost[2]));
        }

        while (set.getSetCount() > 1) {
            Edge edge = edges.poll();
            HashSet<Integer> setA = set.findOrNull(edge.from);
            HashSet<Integer> setB = set.findOrNull(edge.to);

            // 달라야 싸이클이 생기지 않는다.
            if (setA != setB) {
                set.union(setA, setB);
                total += edge.cost;
            }
        }

        return total;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.solution(4, new int[][] {{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}}));
    }

}