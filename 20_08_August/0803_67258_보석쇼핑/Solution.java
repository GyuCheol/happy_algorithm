import java.util.HashMap;
import java.util.HashSet;

class Solution {

    public int[] solution(String[] gems) {
        HashSet<String> allGems = new HashSet<>();
        HashMap<String, Integer> gemMap = new HashMap<>();
        int min = Integer.MAX_VALUE;
        int[] answer = new int[2];
        int i = 0;
        int j = 0;
        int cnt = 0;

        for (String g : gems) {
            allGems.add(g);
            gemMap.put(g, 0);
        }

        while (j < gems.length) {

            if (cnt < allGems.size()) {
                if (gemMap.get(gems[j]) == 0) {
                    ++cnt;
                }

                gemMap.put(gems[j], gemMap.get(gems[j]) + 1);
                j++;
            }

            while (allGems.size() == cnt) {
                // 답이 가능한 경우
                // 현재 답보다 최적인가.
                if (min > (j - i)) {
                    min = j - i;
                    answer[0] = i + 1;
                    answer[1] = j;
                }

                // i를 제거하고, i++
                gemMap.put(gems[i], gemMap.get(gems[i]) - 1);

                if (gemMap.get(gems[i]) == 0) {
                    --cnt;
                }

                i++;
            }

        }

        return answer;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] answer = solution.solution(new String[] {"A", "B", "A", "A", "C", "A", "A", "B", "A", "B", "C"});

        System.out.println(answer[0]);
        System.out.println(answer[1]);

        answer = solution.solution(new String[] {"ZZZ", "YYY", "NNNN", "YYY", "BBB"});

        System.out.println(answer[0]);
        System.out.println(answer[1]);

    }

}