import java.util.LinkedList;
import java.util.Queue;

class Solution {
    private static final int[][] DIRECTIONS = new int[][] {
            {0, -1}, {0, 1}, {-1, 0}, {1, 0}
    };

    private static class Node {
        private int x;
        private int y;
        private int color;

        private Node(int x, int y, int color) {
            this.x = x;
            this.y = y;
            this.color = color;
        }
    }

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[][] visited = new int[m][n];
        Queue<Node> q = new LinkedList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && visited[i][j] == 0) {
                    q.add(new Node(j, i, picture[i][j]));
                    ++numberOfArea;

                    int size = 1;

                    visited[i][j] = 1;

                    while (!q.isEmpty()) {
                        Node node = q.poll();

                        // 상하좌우
                        for (int[] d : DIRECTIONS) {
                            int nx = node.x + d[0];
                            int ny = node.y + d[1];

                            if (0 <= ny && ny < m && 0 <= nx && nx < n && picture[ny][nx] == node.color && visited[ny][nx] == 0) {
                                visited[ny][nx] = 1;
                                q.add(new Node(nx, ny, node.color));
                                ++size;
                            }
                        }
                    }

                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, size);
                }
            }
        }

        return new int[] {numberOfArea, maxSizeOfOneArea};
    }

    public static void main(String[] args) {
        new Solution().solution(6, 4, new int[][] {{1, 1, 1, 0}, {1, 1, 1, 0}, {0, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 1}});
    }
}