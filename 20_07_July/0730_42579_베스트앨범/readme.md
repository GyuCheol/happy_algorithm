* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42579
* 문제 유형 : hash, 정렬
* 시간 복잡도 : O(NlogN)

각 장르에 대한 데이터를 개체화 한 후 정렬을 수행하여
조건에 맞는 정렬 기준을 충족시킨다.

각 장르에 대한 개체로 Genre
재생에 대한 개체로 Play를 만들어

Genre에 Play List를 포함하도록 설계한 후
Genre를 정렬한 후 가지고 있는 Play List를 정렬하여 답을 반환한다.



# 언어별 특이사항

- C++

자료구조 내에 sort 메소드가 없으므로, algorithm의 sort를 이용해야 함.
포인터, 참조를 잘 이해하지 않으면 이 부분을 제대로 처리하기 힘들다.

- Python
딱히 개체화 없이 기본적인 문법 만으로 문제가 요구하는 로직을 수행하여 풀이할 수 있다.

- Java

원하는 정렬 기준의 interface에 맞는 람다식 작성
