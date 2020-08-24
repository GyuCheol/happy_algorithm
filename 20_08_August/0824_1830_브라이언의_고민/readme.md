* 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/1830
* 문제 유형 : 문자열 파싱 (구문 분석?)
* 시간 복잡도 : O(N)

생각보다 미치도록 어려웠던 문제 lv3? 노노.. 알고리즘이 아니라 큰 로직 구현 문제이다.  

뻥 안치고 지금 껏 정신력 쏟은 알고리즘 문제 중에 TOP이다..  
점수도 13점 짜리..  

로직은, 기호(소문자)에 해당하는 알파벳의 count, 시작 위치, 끝 위치를 미리 불러와놓고  
단어 단위로 문자열을 완성해나간다.  

- 용어  
wrapper : 단어를 감싸는 기호를 뜻함 (ex: xABCx)  
splitter : 단어 안에서 다른 글자들을 나누는 기호 (ex: AaBaC)


단어 단위는 아래와 같이 구분한다.  
1. 단어의 시작 글자가 소문자 (wrapper)
2. 단어의 시작 글자가 대문자인데 뒷글자가 소문자  
    2-1] 소문자 count가 2개라면 wrapper으로 처리하기 위해 continue (현재 글자는 별개로 단어로 추가해놓기)  
    2-2] 이외 splitter로 처리
3. 뒷 글자도 대문자  
    3-1] 대문자 이후 첫 소문자가 splitter  
    3-2] 대문자 이후 첫 소문자가 wrapper

이걸 위한 테스트 케이스는 다음과 같다.. 미친...  
정말 미칠뻔한 문제..

```
"HaEaLaLaObWORLDbSpIpGpOpNpGJqOqAdGcWcFcDdeGfWfLeoBBoAAAAxAxAxAA"
"AxAxAxA"
"zHaEzyLbLyqOcWqxOdRxgLeDg"
"HELLOWORLD"
"HaELbLOcWOdRLeD"
"aASBCABabCbSDASD"
"AAAaBaAbBBBBbCcBdBdBdBcCeBfBeGgGGjGjGRvRvRvRvRvR"
"aABBBAa"
"aAbBbBbBbAa"
"aAbBbBbBbAacAdBdCc"
"aABCabb" // inv
"AxAxAxAx" // inv
"aAbBbBbBbAacAdBdCdc" // inv
"aAbBbBbBbAabABCb" // inv
"aAbBbBbBbAaaABCa" // inv
"aABCabb" // inv
"aCaCa" // inv
"aABCabABCbcABC" // inv
"aAdBdCabAfBfCbaAeBeCa" // inv
"asHELLOas" // inv
"aAeBeCeabABCbcABCc" // inv
"aAeBeCabABCbcABCc"
"AAAaBaAbBBBBb"
"aAdBdCabAfBfCbcAeBeCc"
"SpIpGpOpNpGJqOqA"
"HELLObWORLDb"
"aGbWbFbDakGnWnLk"
"dAzBzCd"
"AaBcCc"
"aHELLOa"
"aHELLOabWORLDb"
"HaEaLaLaO"
"bHaEaLaLaOb"
"HaEaLaLaObWORLDb"
"AaAaAaBaBaBaCCbCbC"
```


# 언어별 특이사항

- C++

- Python

- Java

