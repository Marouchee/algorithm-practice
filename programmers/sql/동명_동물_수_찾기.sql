-- 프로그래머스 Lv.2 동명 동물 수 찾기 (GROUP BY)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59041
SELECT NAME, COUNT(*) AS cnt
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING cnt >= 2
ORDER BY NAME;
