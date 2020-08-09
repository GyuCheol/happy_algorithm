import java.util.Stack;

class Solution {

    public int solution(int[][] board, int[] moves) {
        Stack<Integer>[] stacks = new Stack[board.length];
        Stack<Integer> result = new Stack<>();
        int cnt = 0;

        for (int i = 0; i < board.length; ++i) {

            stacks[i] = new Stack<>();

            for (int j = board.length - 1; j >= 0; --j) {
                if (board[j][i] > 0) {
                    stacks[i].push(board[j][i]);
                }
            }
        }

        for (int move : moves) {

            if (stacks[move - 1].empty()) {
                continue;
            }

            int top = stacks[move - 1].pop();

            if (!result.empty() && result.peek() == top) {
                cnt += 2;
                result.pop();
            } else {
                result.push(top);
            }

        }

        return cnt;
    }

    public static void main(String[] args) {
        new Solution().solution(new int[][] {{0, 0, 0, 0, 0}, {0, 0, 1, 0, 3}, {0, 2, 5, 0, 1}, {4, 2, 4, 4, 2}, {3, 5, 1, 3, 1}}, new int[] {1, 5, 3, 5, 1, 2, 1, 4});
    }
}
