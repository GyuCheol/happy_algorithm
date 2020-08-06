package algorithm.lv4.n17685;

import java.util.Arrays;

class Solution {

    private int getLengthIncluded(String a, String b) {
        int compare = 0;

        while (compare < a.length() && a.charAt(compare) == b.charAt(compare)) {
            ++compare;
        }

        return compare;
    }

    public int solution(String[] words) {
        Arrays.sort(words);
        int[] length = new int[words.length];

        for (int i = 0; i < words.length - 1; i++) {
            String a = words[i];
            String b = words[i + 1];

            // 전제1 : a가 b에 포함된 경우라면, a는 항상 b보다 짧거나 같다.
            // 전제2 : a가 b에 포함된 경우라면, a 다음으로 b가 올 수 있다. (물론 b가 a를 포함하는 문자열 중에 가장 작다는 가정)

            int compare = getLengthIncluded(a, b);

            length[i] = Math.max(length[i], compare + (compare == a.length() ? 0 : 1));
            length[i + 1] = compare + 1;

        }

        return Arrays.stream(length).sum();
    }

    public static void main(String[] args) {

        new Solution().solution(new String[] {"word", "war", "warrior", "world"});
        new Solution().solution(new String[] {"go", "gone", "guild"});
        new Solution().solution(new String[] {"abc", "def", "igh"});

    }

}
