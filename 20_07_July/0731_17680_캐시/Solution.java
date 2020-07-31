import java.util.LinkedList;
import java.util.Queue;

class Solution {

    public int solution(int cacheSize, String[] cities) {
        Queue<String> queue = new LinkedList<>();
        int cost = 0;

        for (String city : cities) {
            String lower = city.toLowerCase();

            if (queue.contains(lower)) {
                cost += 1;
                queue.remove(lower);
            } else {
                cost += 5;
            }

            queue.add(lower);

            if (queue.size() > cacheSize) {
                queue.poll();
            }
        }

        return cost;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.solution(3, new String[] {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"}));
        System.out.println(solution.solution(0, new String[] {"A", "A", "A", "A"}));
    }
}
