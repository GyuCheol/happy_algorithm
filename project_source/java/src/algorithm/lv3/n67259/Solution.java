package algorithm.lv3.n67259;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    private static final int[][] DIRECTION = new int[][] { {0, -1}, {0, 1}, {-1, 0}, {1, 0} };

    private int[][] board;
    private int[][][] costs;
    private Queue<Step> queue;
    private int len;

    private static class Step {
        private int x;
        private int y;
        private int dir;
        private int cost;

        public Step(int x, int y, int dir, int cost) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.cost = cost;
        }
    }

    private void search(Step step) {

        if (step.x < 0 || step.x >= len || step.y < 0 || step.y >= len || board[step.y][step.x] != 0) {
            return;
        }

        if (step.cost < costs[step.y][step.x][step.dir]) {
            costs[step.y][step.x][step.dir] = step.cost;
            queue.add(step);
        }

    }

    public int solution(int[][] board) {
        this.queue = new LinkedList<>();
        this.len = board.length;
        this.costs = new int[len][len][];
        this.board = board;

        for (int y = 0; y < len; ++y) {
            for (int x = 0; x < len; ++x) {
                this.costs[y][x] = new int[] { Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE, Integer.MAX_VALUE };
            }
        }

        this.costs[0][0] = new int[] {0, 0, 0, 0};

        search(new Step(1, 0, 3, 100));
        search(new Step(0, 1, 1, 100));

        while (queue.isEmpty() == false) {
            Step step = queue.poll();

            for (int d = 0; d < 4; ++d) {
                int[] dir = DIRECTION[d];

                search(new Step(step.x + dir[0], step.y + dir[1], d, step.cost + ((d == step.dir) ? 100 : 600)));
            }
        }

        return Arrays.stream(costs[len - 1][len - 1]).min().getAsInt();
    }

    public static void main(String[] args) {

    }

}
