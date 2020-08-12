package algorithm.lv2.n1835;

import java.util.ArrayList;

class Solution {

    private ArrayList<Criterion> criteria;
    private char[] chars = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};

    private class Criterion {

        private char a;
        private char b;
        private char method;
        private int distance;


        public Criterion(char a, char b, char method, int distance) {
            this.a = a;
            this.b = b;
            this.method = method;
            this.distance = distance;
        }

        public boolean check() {
            int posA = findChar(a);
            int posB = findChar(b);
            int dist = Math.abs(posA - posB) - 1;

            switch (method) {
                case '=':
                    return dist == distance;
                case '>':
                    return dist > distance;
                case '<':
                    return dist < distance;
                default:
                    return false;
            }
        }

    }

    private int findChar(char ch) {

        for (int i = 0; i < 8; i++) {
            if (chars[i] == ch) {
                return i;
            }
        }
        
        return -1;
    }

    private void swap(int a, int b) {
        char tmp = chars[a];

        chars[a] = chars[b];
        chars[b] = tmp;
    }

    private int permute(int n, int i) {
        int cnt = 0;
        
        // 마지막에 도달 시, 조건에 맞는지 검사하기
        if (i == n) {
            if (criteria.stream().allMatch(x -> x.check())) {
                return 1;
            } else {
                return 0;
            }
        }
        
        // 순열 진행
        for (int j = i; j < n; j++) {
            swap(i, j);
            cnt += permute(n, i + 1);
            swap(i, j);
        }

        return cnt;
    }

    public int solution(int n, String[] data) {
        criteria = new ArrayList<>(n);

        for (String d : data) {
            criteria.add(new Criterion(d.charAt(0), d.charAt(2), d.charAt(3), d.charAt(4) - '0'));
        }

        return permute(chars.length, 0);
    }

    public static void main(String[] args) {
        new Solution().solution(2, new String[] {"N~F=0", "R~T>2"});
    }
}