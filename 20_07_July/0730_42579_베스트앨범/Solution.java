import java.util.ArrayList;
import java.util.HashMap;

class Solution {

    private static class Play {
        private int id;
        private int play;

        public Play(int id, int play) {
            this.id = id;
            this.play = play;
        }
    }

    private static class Genre {
        private String genre;
        private int playTotal = 0;
        private ArrayList<Play> playList = new ArrayList<>();

        public Genre(String genre) {
            this.genre = genre;
        }

        public void addPlay(Play play) {
            this.playTotal += play.play;
            this.playList.add(play);
        }

    }

    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Genre> genreList = new ArrayList<>();
        HashMap<String, Genre> genreMap = new HashMap<>();
        
        // Map을 이용하여 각 데이터 장르별 개체화 후 저장
        for (int i = 0; i < genres.length; i++) {
            String name = genres[i];
            int play = plays[i];
            Genre genre;

            if (genreMap.containsKey(name)) {
                genre = genreMap.get(name);
            } else {
                genre = new Genre(name);

                genreMap.put(name, genre);
                genreList.add(genre);
            }

            genre.addPlay(new Play(i, play));
        }

        // 장르 별 play 총 합계 내림차순
        genreList.sort((a, b) -> Integer.compare(b.playTotal, a.playTotal));

        ArrayList<Integer> results = new ArrayList<>();

        for (Genre g : genreList) {
            // 정렬 기준 : play 내림차순, id 오름차순
            g.playList.sort((a, b) -> (a.play == b.play) ? Integer.compare(a.id, b.id) : Integer.compare(b.play, a.play));
            
            // 최대 2개까지 앨범 결과에 추가
            for (int i = 0; i < Math.min(2, g.playList.size()); i++) {
                results.add(g.playList.get(i).id);
            }
        }

        return results.stream().mapToInt(x -> x.intValue()).toArray();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        solution.solution(new String[] {"classic", "pop", "classic", "classic", "pop"}, new int[] {500, 600, 150, 800, 2500});
    }

}