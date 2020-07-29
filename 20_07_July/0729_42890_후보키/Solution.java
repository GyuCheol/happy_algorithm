import java.util.ArrayList;
import java.util.HashSet;

class Solution {

    private boolean isUniqueColumns(String[][] relation, int columns) {
        HashSet<Integer> set = new HashSet<>();

        for (String[] record : relation) {
            int tmp = 0;

            for (int i = 0; i < record.length; i++) {
                // 해당 칼럼이 선택된 경우, set에 포함
                if ((columns & (1 << i)) != 0) {
                    tmp += record[i].hashCode();
                    tmp <<= 1;
                }
            }

            if (set.contains(tmp)) {
                // 이미 존재하는 record가 있으므로 유일성 만족X
                return false;
            }

            set.add(tmp);
        }

        return true;
    }

    private boolean isMinimum(ArrayList<Integer> results, int columns) {

        for (int result : results) {
            // or 연산으로 i가 result에 포함되어 있는지 확인
            if ((columns | result) == columns) {
                return false;
            }
        }

        return true;
    }

    public int solution(String[][] relation) {
        int columns = relation[0].length;
        int limit = 1 << columns;
        ArrayList<Integer> results = new ArrayList<>();

        for (int i = 1; i <= limit; i++) {
            // 최소성 만족 검사
            if (isMinimum(results, i) == false) {
                continue;
            }

            // 유일성 만족 검사
            if (isUniqueColumns(relation, i)) {
                results.add(i);
            }
        }

        return results.size();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.solution(new String[][] {{"100", "ryan", "music", "2"}, {"200", "apeach", "math", "2"}, {"300", "tube", "computer", "3"}, {"400", "con", "computer", "4"}, {"500", "muzi", "music", "3"}, {"600", "apeach", "music", "2"}}));
    }
}
