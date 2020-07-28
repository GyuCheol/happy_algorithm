package algorithm.lv2.n42583;

import java.util.LinkedList;
import java.util.Queue;

class Solution {

    private static class Truck {

        private int startTime;
        private int weight;

        public Truck(int weight, int startTime) {
            this.weight = weight;
            this.startTime = startTime;
        }

    }

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> truckQueue = new LinkedList<>();
        Queue<Truck> movingTrucks = new LinkedList<>();
        int seconds = 0;
        int totalWeight = 0;

        // 큐에 모든 트럭 추가
        for (int w : truck_weights) {
            truckQueue.add(w);
        }
        
        // 모든 트럭이 도착할 때까지 순회한다.
        while (truckQueue.size() != 0 || movingTrucks.size() != 0) {
            
            // 트럭이 다리 끝에 도달 했다면 queue에서 제거
            if (movingTrucks.isEmpty() == false && (seconds - movingTrucks.peek().startTime) == bridge_length) {
                // 현재 다리 하중에서 제외
                totalWeight -= movingTrucks.poll().weight;
            }
            
            // 남은 트럭이 있는 경우
            if (truckQueue.isEmpty() == false) {
                int w = truckQueue.peek();

                // 현재 큐의 맨 앞 트럭을 추가할 수 있는지 검사
                if ((totalWeight + w) <= weight) {
                    // 큐에서 트럭 꺼내어 건너는 중인 트럭에 넣기
                    movingTrucks.add(new Truck(w, seconds));
                    totalWeight += w;
                    truckQueue.poll();
                }
            }

            seconds += 1;
        }

        return seconds;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        assert solution.solution(2, 10, new int[] {7, 4, 5, 6}) == 8;
        assert solution.solution(100, 100, new int[] {10}) == 101;
        assert solution.solution(100, 100, new int[] {10, 10, 10, 10, 10, 10, 10, 10, 10, 10}) == 110;

    }

}