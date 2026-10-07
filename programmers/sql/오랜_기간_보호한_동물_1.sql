-- 프로그래머스 Lv.3 오랜 기간 보호한 동물(1) (JOIN)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59044
SELECT ai.NAME, ai.DATETIME
FROM ANIMAL_INS ai
LEFT JOIN ANIMAL_OUTS ao ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ao.ANIMAL_ID IS NULL
ORDER BY ai.DATETIME
LIMIT 3
