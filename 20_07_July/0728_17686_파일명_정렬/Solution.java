
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {

    // HEAD (숫자 이외 모든 글자)    : [^\d]+
    // NUMBER (숫자)               : \d+
    // TAIL (숫자 끝나고 나머지 부분) : .* (정렬에 필요 없다)
    private Pattern pattern = Pattern.compile("([^\\d]+)(\\d+).*");

    private int compare(String a, String b) {
        // a, b를 모두 HEAD, NUMBER, TAIL을 나눈다.
        Matcher aMatcher = pattern.matcher(a);
        Matcher bMatcher = pattern.matcher(b);

        aMatcher.find();
        bMatcher.find();
        
        // group(1)은 대소문자 무시하게 검사
        int compare = String.CASE_INSENSITIVE_ORDER.compare(aMatcher.group(1), bMatcher.group(1));

        if (compare == 0) {
            int aNum = Integer.parseInt(aMatcher.group(2));
            int bNum = Integer.parseInt(bMatcher.group(2));

            return Integer.compare(aNum, bNum);
        }
        else {
            return compare;
        }
    }

    public String[] solution(String[] files) {
        String[] answer = Arrays.stream(files)
                .sorted(this::compare)
                .toArray(String[]::new);

        return answer;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        String[] answer = solution.solution(new String[] {
                "img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"
        });

        for (String s : answer)  {
            System.out.println(s);
        }

        solution.solution(new String[] {
                "img12.png", "imG12", "img00012.abc"
        });

    }
}