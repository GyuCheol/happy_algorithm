* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17681
* 시간 복잡도 : O(N^2)

각 배열의 숫자 값을 2진으로 연산할 수 있어야 한다.
arr1과 arr2는 2진 | 연산으로 결과에 필요한 비트 결과를 얻을 수 있다.
그 결과를 토대로 각 line을 만들면 된다.

# 언어별 특이사항
- Java
결과 문자열을 만들 때 StringBuilder를 쓰면 된다.

- Python
python은 긴 문자열을 합쳐야할 때 list에 각 문자열을 넣고 join하는 것이 best practice이다.

- C++
다른 언어들과 달리 string 형태가 immutable이므로 스트링 내부를 변경할 수 있다.

다만, java의 StringBuilder와 흡사한 역할을 하는 stringstream을 이용하여 풀이.
