-- 프로그래머스 Lv.4 보호소에서 중성화한 동물 (JOIN)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59045
SELECT ai.ANIMAL_ID, ai.ANIMAL_TYPE, ai.NAME
FROM ANIMAL_INS ai
JOIN ANIMAL_OUTS ao ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE SEX_UPON_INTAKE LIKE '%Intact%' AND (SEX_UPON_OUTCOME LIKE '%Spayed%' or SEX_UPON_OUTCOME LIKE '%Neutered%')
ORDER BY ai.ANIMAL_ID
