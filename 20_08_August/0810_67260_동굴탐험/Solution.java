
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {

    public boolean solution(int n, int[][] path, int[][] order) {
        ArrayList<Integer>[] graph = new ArrayList[n];
        Queue<Integer> queue = new LinkedList<>();
        ArrayList<Integer>[] chained = new ArrayList[n];
        int[] visited = new int[n];
        int[] required = new int[n];

        for (int i = 0; i < n; ++i) {
            graph[i] = new ArrayList<>();
            chained[i] = new ArrayList<>();
            required[i] = -1;
        }

        for (int[] p : path) {
            graph[p[0]].add(p[1]);
            graph[p[1]].add(p[0]);
        }

        // (8, 5) 5를 방문하려면, 먼저 8을 방문
        for (int[] o : order) {
            required[o[1]] = o[0];
            chained[o[0]].add(o[1]);
        }
        
        // 아예 0번조차 방문이 불가능하면 False 리턴
        if (required[0] != -1) {
            return false;
        }

        visited[0] = 1;
        queue.add(0);

        while (!queue.isEmpty()) {
            Integer node = queue.poll();

            for (int to : graph[node]) {

                if (visited[to] == 0) {

                    if (required[to] != -1 && visited[required[to]] != 1) {
                        visited[to] = 2;
                        continue;
                    }

                    visited[to] = 1;
                    queue.add(to);

                    for (int c : chained[to]) {
                        if (visited[c] == 2) {
                            visited[c] = 1;
                            queue.add(c);
                        }
                    }

                }

            }

        }

        return Arrays.stream(visited).filter(x -> x == 1).count() == n;
    }

    public static void main(String[] args) {
        new Solution().solution(9, new int[][] {{0, 1}, {0, 3}, {0, 7}, {8, 1}, {3, 6}, {1, 2}, {4, 7}, {7, 5}}, new int[][] {{8, 5}, {6, 7}, {4, 1}});
    }

}
