package algorith.lv1.n17681;

/*
* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17681?language=java
*
* 각 배열 값을 2진으로 연산할 수 있어야 한다.
* arr1과 arr2는 2진 | 연산으로 결과에 필요한 비트 결과를 얻을 수 있다.
* 그 결과를 토대로 각 line을 만들면 된다.
*
* line을 만들기 위해 #과 ' ' 문자를 만들어야 하는데
* 이때 String += 연산자를 이용하면 잉여 String 생성이 많이 되므로
* StringBuilder 개체로 append와 clear를 반복하여 String 생성하기
* 각 자릿수가 1인지 0인지 판단하는건 & 연산자로 가능하다.
*
* 시간 복잡도 : O(N^2)
* */

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
