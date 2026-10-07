-- 프로그래머스 Lv.2 고양이와 개는 몇 마리 있을까 (GROUP BY)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59040
SELECT ANIMAL_TYPE, COUNT(*) AS cnt
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Cat' or ANIMAL_TYPE = 'Dog'
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC
