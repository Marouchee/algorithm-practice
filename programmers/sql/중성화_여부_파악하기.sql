-- 프로그래머스 Lv.2 중성화 여부 파악하기 (String, Date)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59409
SELECT ANIMAL_ID, NAME, CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' or SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O' ELSE 'X' END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
