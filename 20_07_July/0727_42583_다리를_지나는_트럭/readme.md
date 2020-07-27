* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42583
* 문제 유형 : 자료구조 Queue 활용 문제
* 시간 복잡도 : O(N * M) N은 트럭의 개수, M은 다리의 길이

트럭은 순차적으로 다리에 봐야하니, queue 구조에 넣고
truck이 다리 위에 올 수 있는지 검사.
다리 위에 있는 truck도 순차적으로 나가므로 queue에 넣는다.

truck나갈 수 있는 타이밍을 계산하기 위해
truck이 추가된 시간으로 초기화하여 queue의 가장 첫 truck의
들어온 시간과 현재 시간으로 다리 위에서 빠져나갈 수 있는지 비교한다.


# 언어별 특이사항

- C++
값 복사가 일어나기 때문에, MovingQueue에 Truck 포인터로 값을 저장한다.
class 크기가 크지 않아 그닥 차이는 없겠지만 (오히려 스택 메모리에 있는게 캐시 되어 더 빠를듯?)
포인터 연습겸, 메모리 관리 부분도 해볼겸 고려해보았다.

- Python
파이썬은 별도로 queue라는 구조 없이, deque 구조를 queue와 stack 함께 퉁쳐서 쓰곤 한다.