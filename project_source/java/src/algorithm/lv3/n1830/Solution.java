package algorithm.lv3.n1830;

import java.util.HashSet;

class Solution {
    private static final String INVALID = "invalid";
    private static final int COUNT = 0;
    private static final int MIN = 1;
    private static final int MAX = 2;

    private HashSet<Character> set;
    private String sentence;
    private int[][] info;

    private String getWord(int start, int end) {

        if (start > end) {
            return null;
        }

        StringBuilder sb = new StringBuilder();

        if (end >= sentence.length()) {
            return null;
        }

        if ((start + 1) < end && Character.isLowerCase(sentence.charAt(start + 1))) {
            char splitter = sentence.charAt(start + 1);

            if (!set.add(splitter)) {
                return null;
            }

            for (int i = start; i <= end; i+=2) {
                char ch = sentence.charAt(i);

                if (Character.isLowerCase(ch)) {
                    return null;
                }
                sb.append(ch);
            }

            for (int i = start + 1; i <= end; i+=2) {
                if (sentence.charAt(i) != splitter) {
                    return null;
                }
            }

            if (Character.isLowerCase(sentence.charAt(end))) {
                return null;
            }
        } else {
            for (int i = start; i <= end; i++) {
                if (Character.isLowerCase(sentence.charAt(i))) {
                    return null;
                }

                sb.append(sentence.charAt(i));
            }
        }

        return sb.toString();
    }

    private int getNextLower(int begin) {
        for (int i = begin; i < sentence.length(); i++) {
            if (Character.isLowerCase(sentence.charAt(i))) {
                return i;
            }
        }

        return -1;
    }

    public String solution(String sentence) {
        if (sentence.indexOf(' ') != -1) {
            // 공백 존재시 바로 INVALID
            return INVALID;
        }

        int id = 0;
        StringBuilder sb = new StringBuilder(sentence.length());

        this.info = new int[125][3];
        this.sentence = sentence;
        this.set = new HashSet<>();

        for (int i = 'a'; i <= 'z'; i++) {
            info[i][MIN] = -1;
        }

        for (int i = 0; i < sentence.length(); i++) {
            char ch = sentence.charAt(i);

            if (Character.isLowerCase(ch)) {
                ++info[ch][COUNT];

                if (info[ch][MIN] == -1) {
                    info[ch][MIN] = i;
                }

                info[ch][MAX] = i;
            }
        }

        while (id < sentence.length()) {
            char ch = sentence.charAt(id);

            if (sb.length() > 0) {
                sb.append(' ');
            }

            if (Character.isLowerCase(ch)) {
                // Wrapper

                if (!set.add(ch)) {
                    return INVALID;
                }

                String tmp = getWord(info[ch][MIN] + 1, info[ch][MAX] - 1);

                if (tmp == null) {
                    return INVALID;
                }

                sb.append(tmp);
                id = info[ch][MAX] + 1;

                continue;
            }

            if ((id + 1) < sentence.length()) {
                char nextCh = sentence.charAt(id + 1);

                if (Character.isLowerCase(nextCh)) {
                    if (info[nextCh][0] == 2) {
                        // wrapper
                        sb.append(ch);
                        ++id;
                    } else {
                        // splitter라면 단어로 만듦
                        String tmp = getWord(id, info[nextCh][MAX] + 1);

                        if (tmp == null) {
                            return INVALID;
                        }

                        sb.append(tmp);
                        id = info[nextCh][MAX] + 2;
                    }

                    continue;
                }

                // 대문자 연속이라면,
                // 다음 소문자 위치 찾기
                int nextLower = getNextLower(id);

                if (nextLower == -1) {
                    sb.append(sentence.substring(id, sentence.length()));
                    break;
                }

                char nextLowerCh = sentence.charAt(nextLower);
                int end = 0;

                if (info[nextLowerCh][COUNT] == 2) {
                    // wrapper
                    end = info[nextLowerCh][MIN] - 1;
                } else {
                    // splitter
                    end = info[nextLowerCh][MIN] - 2;
                }

                String tmp = getWord(id, end);

                if (tmp == null) {
                    return INVALID;
                }

                sb.append(tmp);

                id = end + 1;
                continue;
            }

            sb.append(ch);
            ++id;

        }

        return sb.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();


        System.out.println(solution.solution("HaEaLaLaObWORLDbSpIpGpOpNpGJqOqAdGcWcFcDdeGfWfLeoBBoAAAAxAxAxAA"));
        System.out.println(solution.solution("AxAxAxA"));
        System.out.println(solution.solution("zHaEzyLbLyqOcWqxOdRxgLeDg"));
        System.out.println(solution.solution("HELLOWORLD"));
        System.out.println(solution.solution("HaELbLOcWOdRLeD"));
        System.out.println(solution.solution("aASBCABabCbSDASD"));
        System.out.println(solution.solution("AAAaBaAbBBBBbCcBdBdBdBcCeBfBeGgGGjGjGRvRvRvRvRvR"));
        System.out.println(solution.solution("aABBBAa"));
        System.out.println(solution.solution("aAbBbBbBbAa"));
        System.out.println(solution.solution("aAbBbBbBbAacAdBdCc"));
        System.out.println("-------");

        System.out.println(solution.solution("aABCabb")); // inv
        System.out.println(solution.solution("AxAxAxAx")); // inv
        System.out.println(solution.solution("aAbBbBbBbAacAdBdCdc")); // inv
        System.out.println(solution.solution("aAbBbBbBbAabABCb")); // inv
        System.out.println(solution.solution("aAbBbBbBbAaaABCa")); // inv
        System.out.println(solution.solution("aABCabb")); // inv
        System.out.println(solution.solution("aCaCa")); // inv
        System.out.println(solution.solution("aABCabABCbcABC")); // inv
        System.out.println(solution.solution("aAdBdCabAfBfCbaAeBeCa")); // inv
        System.out.println(solution.solution("asHELLOas")); // inv
        System.out.println(solution.solution("aAeBeCeabABCbcABCc")); // inv
        System.out.println("----inv---");

        System.out.println(solution.solution("aAeBeCabABCbcABCc"));
        System.out.println(solution.solution("AAAaBaAbBBBBb"));
        System.out.println(solution.solution("aAdBdCabAfBfCbcAeBeCc"));
        System.out.println(solution.solution("SpIpGpOpNpGJqOqA"));
        System.out.println(solution.solution("HELLObWORLDb"));
        System.out.println(solution.solution("aGbWbFbDakGnWnLk"));
        System.out.println(solution.solution("dAzBzCd"));
        System.out.println(solution.solution("AaBcCc"));
        System.out.println(solution.solution("aHELLOa"));
        System.out.println(solution.solution("aHELLOabWORLDb"));
        System.out.println(solution.solution("HaEaLaLaO"));
        System.out.println(solution.solution("bHaEaLaLaOb"));
        System.out.println(solution.solution("HaEaLaLaObWORLDb"));
        System.out.println(solution.solution("AaAaAaBaBaBaCCbCbC"));
    }

}
