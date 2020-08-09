package algorithm.lv4.n12983;

import java.util.Arrays;
import java.util.HashSet;

class Solution {

    public int solution(String[] strs, String t) {
        int[] dp = new int[t.length() + 1];
        HashSet<String> set = new HashSet<String>(Arrays.asList(strs));
        
        // 첫 시작 부분 초기화
        for (int i = 1; i <= 5; i++) {
            if (i <= t.length() && set.contains(t.substring(0, i))) {
                dp[i] = 1;
            }
        }
        
        for (int i = 2; i <= t.length(); i++) {
            int tmp = i - 1;

            if (dp[tmp] != 0) {
                for (int j = 1; j <= 5; j++) {
                    if ((tmp + j) <= t.length() && set.contains(t.substring(tmp, tmp + j))) {
                        if (dp[tmp + j] == 0) {
                            dp[tmp + j] = dp[tmp] + 1;
                        } else {
                            dp[tmp + j] = Math.min(dp[tmp + j], dp[tmp] + 1);
                        }
                    }
                }
            }
        }

        return (dp[t.length()] == 0) ? -1 : dp[t.length()];
    }

    public static void main(String[] args) {
        new Solution().solution(new String[] {"ab", "bc"}, "abc");
        new Solution().solution(new String[] {"app", "le"}, "apple");
        new Solution().solution(new String[] {"ab", "na", "n", "a", "bn"}, "nabnabn");
        new Solution().solution(new String[] {"ba", "na", "n", "a"}, "banana");
        new Solution().solution(new String[] {"app", "ap", "p", "l", "e", "ple", "pp"}, "apple");
        new Solution().solution(new String[] {"ba", "an", "nan", "ban", "n"}, "banana");

    }
}