-- 프로그래머스 Lv.3 없어진 기록 찾기 (JOIN)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59042
SELECT ao.ANIMAL_ID, ao.NAME
FROM ANIMAL_OUTS ao
LEFT JOIN ANIMAL_INS ai ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ai.ANIMAL_ID IS NULL
ORDER BY ao.ANIMAL_ID, ao.NAME
