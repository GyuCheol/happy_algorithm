package algorithm.lv3.n49189;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {

    private static class Step {
        private int node;
        private int distance;

        public Step(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }
    }

    public int solution(int n, int[][] edge) {
        ArrayList<Integer>[] edges = new ArrayList[n + 1];
        Queue<Step> queue = new LinkedList<>();
        int[] distance = new int[n + 1];

        for (int i = 1; i <= n; ++i) {
            edges[i] = new ArrayList<>();
        }

        for (int[] e : edge) {
            edges[e[0]].add(e[1]);
            edges[e[1]].add(e[0]);
        }

        distance[1] = 1;
        queue.add(new Step(1, 1));

        while (!queue.isEmpty()) {
            Step s = queue.poll();

            for (int to : edges[s.node]) {
                if (distance[to] == 0) {
                    distance[to] = s.distance + 1;
                    queue.add(new Step(to, distance[to]));
                }
            }
        }

        int max = Arrays.stream(distance).max().getAsInt();

        return (int) Arrays.stream(distance).filter(x -> x == max).count();
    }

}
