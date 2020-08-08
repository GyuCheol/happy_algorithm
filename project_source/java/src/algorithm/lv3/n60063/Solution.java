package algorithm.lv3.n60063;

import java.util.LinkedList;
import java.util.Queue;

class Solution {

    private static final int HORIZONTAL = 0;
    private static final int VERTICAL = 1;
    // 상하좌우
    private static final int[][] DIRECTION = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    // 가로모드 & 세로모드 (가로모드 각 xy 좌표를 yx로 사용하면 세로모드에 대응됨)
    private static final int[][][] ROTATION = {
            {
                {0, 0, 1, 1},
                {0, -1, 1, -1},
                {1, 0, 0, 1},
                {1, -1, 0, -1}
            },
            {
                {0, 0, 1, 1},
                {-1, 0, -1, 1},
                {0, 1, 1, 0},
                {-1, 1, -1, 0}
            }};

    private class Step {
        private int step;
        private int x;
        private int y;
        private int mode;

        public Step(int step, int x, int y, int mode) {
            this.step = step;
            this.x = x;
            this.y = y;
            this.mode = mode;

            // 추가된 step은 방문한 좌표로 기억시킨다.
            visited[y][x][mode] = 1;
        }
    }

    int length;
    int[][][] visited;
    int[][] board;

    Queue<Step> queue;

    private boolean checkRange(int x, int y) {
        return 0 <= x && x < length && 0 <= y && y < length && board[y][x] == 0;
    }

    private boolean checkAnotherLoc(int x, int y, int mode) {
        int nx = x + (mode == HORIZONTAL ? 1 : 0);
        int ny = y + (mode == VERTICAL ? 1 : 0);

        return checkRange(nx, ny);
    }

    private boolean isVisited(int x, int y, int mode) {
        return visited[y][x][mode] == 0;
    }

    public int solution(int[][] board) {
        this.board = board;
        this.length = board.length;
        // 각 좌표마다 가로 모드로 방문한 경우, 세로 모드로 방문한 경우
        this.visited = new int[length][length][2];
        queue = new LinkedList<>();

        queue.add(new Step(0, 0, 0, HORIZONTAL));

        while (!queue.isEmpty()) {
            Step step = queue.poll();

            // 목표 도착 시 종료
            // 가로인 경우, (l-2), (l-1), 세로는 (l-1), (l-2)
            if ((step.mode == HORIZONTAL && step.x == (length - 2) && step.y == (length - 1)) ||
                    (step.mode == VERTICAL && step.x == (length - 1) && step.y == (length - 2))) {
                return step.step;
            }

            // 상하좌우
            for (int i = 0; i < 4; ++i) {
                int nx = step.x + DIRECTION[i][0];
                int ny = step.y + DIRECTION[i][1];

                if (checkRange(nx, ny) && checkAnotherLoc(nx, ny, step.mode) && isVisited(nx, ny, step.mode)) {
                    queue.add(new Step(step.step + 1, nx, ny, step.mode));
                }
            }

            // 회전
            for (int i = 0; i < 4; ++i) {
                int nx = step.x + ROTATION[step.mode][i][0];
                int ny = step.y + ROTATION[step.mode][i][1];
                int rx = step.x + ROTATION[step.mode][i][2];
                int ry = step.y + ROTATION[step.mode][i][3];
                int mode = step.mode ^ 1;

                // 새롭게 배치될 위치 검사, 회전용 좌표 검사, 다른 좌표도 검사(다른 모드), 이미 방문한 좌표인지
                if (checkRange(nx, ny) && checkRange(rx, ry) && checkAnotherLoc(nx, ny, mode) && isVisited(nx, ny, mode)) {
                    queue.add(new Step(step.step + 1, nx, ny, mode));
                }
            }

        }

        return -1;
    }

    public static void main(String[] args) {

        // System.out.println(new Solution().solution(new int[][] {{0, 0, 0, 1, 1}, {0, 0, 0, 1, 0}, {0, 1, 0, 1, 1}, {1, 1, 0, 0, 1}, {0, 0, 0, 0, 0}}));
        System.out.println(new Solution().solution(new int[100][100]));
        // System.out.println(new Solution().solution(new int[][] {{0, 0, 0}, {1, 1, 0}, {0, 0, 0}}));
    }
}