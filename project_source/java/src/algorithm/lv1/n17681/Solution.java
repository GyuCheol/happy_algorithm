package algorithm.lv1.n17681;

public class Solution {

    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        StringBuilder sb = new StringBuilder(n);

        for (int i = 0; i < n; i++) {
            int tmp = arr1[i] | arr2[i];
    
            for (int j = n - 1; j >= 0; j--) {
                // 2진 자릿수 1, 0 확인
                if ((tmp & (1 << j)) != 0) {
                    sb.append('#');
                } else {
                    sb.append(' ');
                }
            }

            answer[i] = sb.toString();
            sb.setLength(0);
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        String[] answer = solution.solution(5,
                new int[] {9, 20, 28, 18, 11},
                new int[] {30, 1, 21, 17, 28});

        for (String line : answer) {
            System.out.println(line);
        }
    }
}
