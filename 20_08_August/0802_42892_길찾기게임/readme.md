* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42892
* 문제 유형 : 트리, 트리 순회
* 시간 복잡도 : O(NlogN)

y 내림차순 > x 오름차순으로 정렬하면
root 노드 > 가장 마지막 leaf 노드 순서대로 정렬할 수 있다.

즉, y가 높은 값 순서대로 트리를 구성하면 x값만 비교하여 트리에 추가하면 다른 제어 없이 쉽게 left, right 노드를 결정 지을 수 있다.

해당 방법으로 트리를 완성 시킨 후, pre-order, post-order로 탐색한 array를 리턴하면 된다.


# 언어별 특이사항

- C++

다른 언어와는 다르게 생성된 메모리를 잘 관리 해주어야 한다.

node vector를 만들어, 노드 값을 복사하고, 그 값을 가지고 있게 한다.
그리고 해당 node vector의 값을 포인터로 root, left, right 등 모든 node를 관리한다.
그러면, 소멸 단계에서 메모리 관리가 편히 될 것이다.

- Python

call stack의 깊이가 stack 메모리가 아닌, depth 크기로만 따지기에 별도로 call stack exceed limit을 변경 해주어야 한다.
딱 1,000은 안되고 (기본적으로 호출되는 콜 스택 고려) 대충 어림 잡아 1,500정도로 설정해주었다.


- Java



