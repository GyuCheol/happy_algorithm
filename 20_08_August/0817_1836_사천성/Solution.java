import java.util.ArrayList;
import java.util.HashMap;

class Solution {

    private static class Location {
        private int y;
        private int x;
        private char ch;

        public Location(int y, int x, char ch) {
            this.y = y;
            this.x = x;
            this.ch = ch;
        }
    }

    private static class Pair {
        private Location loc1;
        private Location loc2;

        public Pair(Location loc1, Location loc2) {
            this.loc1 = loc1;
            this.loc2 = loc2;
        }
    }

    private static class Line {
        private int y1;
        private int x1;
        private int y2;
        private int x2;

        public Line(int y1, int x1, int y2, int x2) {
            this.y1 = y1;
            this.x1 = x1;
            this.y2 = y2;
            this.x2 = x2;
        }
    }

    private int[][] createLines(Location loc, char[][] map) {
        int[][] tmp = new int[map.length][map[0].length];

        tmp[loc.y][loc.x] = 2;

        // 상
        for (int y = loc.y - 1; y >= 0; y--) {
            if (map[y][loc.x] != '.') break;
            tmp[y][loc.x] = 1;
        }

        // 하
        for (int y = loc.y + 1; y < tmp.length; y++) {
            if (map[y][loc.x] != '.') break;
            tmp[y][loc.x] = 1;
        }

        // 좌
        for (int x = loc.x - 1; x >= 0; x--) {
            if (map[loc.y][x] != '.') break;
            tmp[loc.y][x] = 1;
        }

        // 우
        for (int x = loc.x + 1; x < map[0].length; x++) {
            if (map[loc.y][x] != '.') break;
            tmp[loc.y][x] = 1;
        }

        return tmp;
    }

    private boolean canMatch(Pair pair, char[][] map) {

        // 상하좌우에 바로 붙어있는 경우 true 리턴
        if ((Math.abs(pair.loc1.x - pair.loc2.x) + Math.abs(pair.loc1.y - pair.loc2.y)) == 1) {
            return true;
        }

        int[][] lines1 = createLines(pair.loc1, map);
        int[][] lines2 = createLines(pair.loc2, map);

        for (int y = 0; y < map.length; y++) {
            for (int x = 0; x < map[0].length; x++) {
                if (lines1[y][x] == 1 && lines2[y][x] == 1) {
                    // 서로 교차하므로
                    return true;
                }

            }
        }

        return false;
    }

    public String solution(int m, int n, String[] board) {
        StringBuilder result = new StringBuilder();
        char[][] map = new char[m][n];

        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                map[y][x] = board[y].charAt(x);
            }
        }

        ArrayList<Pair> tmp = new ArrayList<>();
        HashMap<Character, Location> hashMap = new HashMap<>();

        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (hashMap.containsKey(map[y][x]) == false) {
                    if (map[y][x] != '.' && map[y][x] != '*') {
                        hashMap.put(map[y][x], new Location(y, x, map[y][x]));
                    }
                } else {
                    tmp.add(new Pair(hashMap.get(map[y][x]), new Location(y, x, map[y][x])));
                }
            }
        }

        // 알파벳 순서 정렬
        tmp.sort((a, b) -> Character.compare(a.loc1.ch, b.loc1.ch));

        main:
        while (tmp.size() > 0) {
            int cnt = tmp.size();

            for (Pair pair : tmp) {
                // 해당 쌍이 제거 가능한가?
                if (canMatch(pair, map)) {
                    map[pair.loc1.y][pair.loc1.x] = '.';
                    map[pair.loc2.y][pair.loc2.x] = '.';
                    result.append(pair.loc1.ch);

                    tmp.remove(pair);
                    continue main;
                }
            }

            return "IMPOSSIBLE";
        }


        return result.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.solution(4, 4, new String[] {
                ".A*.",
                "..*.",
                "..*A",
                "...."
        }));


        System.out.println(sol.solution(2, 4, new String[] {
                "NRYN",
                "ARYA"
        }));
    }
}