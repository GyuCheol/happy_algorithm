package algorithm.lv2.n17683;

import java.util.ArrayList;

class Solution {

    private static class MusicInfo {
        private int playTime;
        private String title;
        private String melodies;
        private String stretchedMelodies;

        public MusicInfo(int playTime, String title, String melodies) {
            this.playTime = playTime;
            this.title = title;
            this.melodies = melodies;

            makeStretchedMelodies();
        }

        private void makeStretchedMelodies() {
            StringBuilder sb = new StringBuilder(playTime + 1);

            int repeat = (playTime + 1) / melodies.length();

            for (int i = 0; i < repeat; i++) {
                sb.append(melodies);
            }

            sb.append(melodies.substring(0, (playTime + 1) % melodies.length()));

            stretchedMelodies = sb.toString();
        }
    }

    private String replaceMelodies(String melodies) {
        StringBuilder sb = new StringBuilder(melodies.length());
        
        // C# 2글자를 1글자 멜로디로 변환
        for (int i = 0; i < melodies.length();++i) {

            if ((i + 1) < melodies.length() && melodies.charAt(i + 1) == '#') {
                switch (melodies.charAt(i)) {
                    case 'C':
                        sb.append('N');
                        break;
                    case 'D':
                        sb.append('M');
                        break;
                    case 'E':
                        sb.append('O');
                        break;
                    case 'F':
                        sb.append('P');
                        break;
                    case 'G':
                        sb.append('Q');
                        break;
                    case 'A':
                        sb.append('R');
                        break;
                }
                // # 건너뛰기
                ++i;
            } else {
                sb.append(melodies.charAt(i));
            }

        }

        return sb.toString();
    }

    private int timeToInt(String time) {
        int hour = Integer.parseInt(time.substring(0, 2));
        int minutes = Integer.parseInt(time.substring(3, 5));

        return (hour * 60) + minutes;
    }

    public String solution(String m, String[] musicinfos) {
        ArrayList<MusicInfo> musicInfoList = new ArrayList<>(musicinfos.length);

        for (String info : musicinfos) {
            String[] split = info.split(",");
            int playTime = timeToInt(split[1]) - timeToInt(split[0]);
            musicInfoList.add(new MusicInfo(playTime, split[2], replaceMelodies(split[3])));
        }

        // 정렬 기준 : 음악 시간 내림차순
        musicInfoList.sort((a, b) -> b.playTime - a.playTime);

        String replacedMelodies = replaceMelodies(m);

        for (MusicInfo info : musicInfoList) {
            if (info.stretchedMelodies.contains(replacedMelodies)) {
                return info.title;
            }
        }

        return "(None)";
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.solution("ABCDEFG", new String[] {"12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"}));
        System.out.println(solution.solution("ABAB", new String[] {"12:00,12:14,HELLO,ABCDABCDAB", "13:00,13:25,WORLD,ABAB"}));
        System.out.println(solution.solution("CDABACDAB", new String[] {"12:00,12:14,HELLO,ABCDABACD", "13:00,13:25,WORLD,CDAABACDABD"}));
        System.out.println(solution.solution("ABB", new String[] {"12:00,12:14,HELLO,ABCDABCDAB", "13:00,13:25,WORLD,ABAB"}));
        System.out.println(solution.solution("ABC", new String[] {"12:00,12:14,HELLO,ABC#", "13:00,13:04,WORLD,ABC"}));
    }

}