* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/49189
* 문제 유형 : BFS
* 시간 복잡도 : O(N*M) N은 정점 개수, M은 정점당 가진 간선 최댓값 

BFS로 이동하면서 각 노드 간의 이동된 거리를 업데이트 해준다.

이때 이동거리 최댓 값도 저장해두고, 계산이 끝난 후 각 노드별 최댓 값과 일치하는 노드의 개수를 세면 끝.

단순 BFS라서 어려움은 없음.


# 언어별 특이사항

- C++

- Python

- Java

stream을 이용해서 count 세기
