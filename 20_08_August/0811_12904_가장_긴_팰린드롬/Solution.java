
class Solution
{

    private boolean check(String s, int start, int end) {
        int length = (end - start) / 2;

        for (int i = 0; i <= length; i++) {
            if (s.charAt(start + i) != s.charAt(end - 1 - i)) {
                return false;
            }
        }

        return true;
    }

    public int solution(String s)
    {
        int answer = 1;

        for (int i = 0; i < s.length(); i++) {

            for (int j = answer + 1; j <= s.length() - i; j++) {
                if (check(s, i, i + j)) {
                    answer = j;
                }
            }

        }

        return answer;
    }
}