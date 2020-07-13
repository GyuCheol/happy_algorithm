/*
7월 13일

동물의 아이디와 이름
https://programmers.co.kr/learn/courses/30/lessons/59403
SELECT - lv1


*/

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

/*
7월 13일

여러 기준으로 정렬하기

https://programmers.co.kr/learn/courses/30/lessons/59404
SELECT - lv1


*/

SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;

/*
7월 13일

상위 n개 레코드

https://programmers.co.kr/learn/courses/30/lessons/59405
SELECT - lv1


*/

SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;

/*
7월 13일

중복 제거하기

https://programmers.co.kr/learn/courses/30/lessons/59408
SELECT - lv1


*/

SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS;
