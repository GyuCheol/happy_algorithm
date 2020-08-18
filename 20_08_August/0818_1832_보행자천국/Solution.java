class Solution {
    int MOD = 20170805;

    public int solution(int m, int n, int[][] cityMap) {
        int[][][] dp = new int[m + 1][n + 1][2];
        int[][] map = new int[m + 1][n + 1];
        

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                map[i][j] = cityMap[i-1][j-1];
            }
        }
        // 0 세로, 1 가로, 초기값 설정 금지 나오기 전까지 1로
        for (int i = 1; i <= m; i++) {
            if (map[i][1] == 1) {
                break;
            }
            dp[i][1][0] = 1;
        }

        for (int i = 1; i <= n; i++) {
            if (map[1][i] == 1) {
                break;
            }
            dp[1][i][1] = 1;
        }

        for (int i = 2; i <= m; i++) {
            for (int j = 2; j <= n; j++) {
                if (map[i][j] == 1) {
                    continue;
                }

                dp[i][j][0] += dp[i-1][j][0];
                dp[i][j][0] %= MOD;

                if (map[i-1][j] == 0) {
                    dp[i][j][0] += dp[i-1][j][1];
                    dp[i][j][0] %= MOD;
                }

                dp[i][j][1] += dp[i][j-1][1];
                dp[i][j][1] %= MOD;

                if (map[i][j-1] == 0) {
                    dp[i][j][1] += dp[i][j-1][0];
                    dp[i][j][1] %= MOD;
                }
            }
        }

        return (dp[m][n][0] + dp[m][n][1]) % MOD;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // sol.solution(3, 3, new int[][] {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}});
        // sol.solution(3, 6, new int[][] {{0, 2, 0, 0, 0, 2}, {0, 0, 2, 0, 1, 0}, {1, 0, 0, 2, 2, 0}});
        System.out.println(sol.solution(5, 5, new int[][] {
                {0, 1, 0, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 1, 0, 0, 0}
        }));
    }

}

