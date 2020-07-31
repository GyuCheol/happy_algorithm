* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17680
* 문제 유형 : Queue 문제
* 시간 복잡도 : O(N)

Queue 구조를 이용해서 LRU 캐시를 구현한다.
cache 사이즈가 많아질 것을 생각해서
LRU 캐시에 해당 데이터가 있는지 없는지를 HashSet을 이용할 수도 있을 것이다.
cache 사이즈는 30이 최대이니, 그냥 Queue자체의 contain과 remove로도 충분하다.

다만, cache 사이즈가 300, 1000 등으로 늘어난다면 HashSet으로 처리해야 성능이 더 빠를 것임.



# 언어별 특이사항

- C++

모두 소문자로 변경하는 함수를 inline으로 하여 함수 call에 대한 오버헤드 제거.

C++의 queue는 요소 탐색이 안되므로 탐색이 가능하면서도 queue처럼 사용 가능한 list를 사용하였다.

- Python

python은 set을 사용하여 cache hit이 되는지 miss가 되는지 판단했다.

- Java


