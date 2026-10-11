-- 프로그래머스 Lv.2 입양 시각 구하기(1) (GROUP BY)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59412
SELECT HOUR(DATETIME), COUNT(*) AS cnt
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) < 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)
