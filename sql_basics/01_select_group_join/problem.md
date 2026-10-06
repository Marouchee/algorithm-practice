# SQL 드릴 01: SELECT · GROUP BY · JOIN

연습 DB는 `db.py`(SQLite, 가상 데이터)에 있다.

```
MEMBERS  (member_id, name, gender, birth_date, city)                    -- city는 NULL 가능
PRODUCTS (product_id, name, category, price)
ORDERS   (order_id, member_id, product_id, amount, order_date, status)  -- amount는 수량, status: DONE / CANCEL
```

## S1. SELECT · WHERE · ORDER BY · LIMIT

- S1-1. 서울에 사는 회원 이름, 이름 오름차순
- S1-2. 가장 비싼 상품 1개의 이름과 가격
- S1-3. 취소되지 않았고 수량 2 이상인 주문의 `order_id`, `order_date`, 최신순
- S1-4. 도시 정보가 없는 회원 / 있는 회원 (`= NULL`은 항상 0행 → `IS NULL`)

## S2. 집계 · GROUP BY · HAVING

- S2-1. 카테고리별 상품 수, 카테고리 오름차순
- S2-2. 취소 제외, 회원별 총 주문 수량(`SUM`), 수량 내림차순·`member_id` 오름차순
- S2-3. 주문 건수 2건 이상인 회원 (`HAVING`)
- S2-4. `COUNT(*)`와 `COUNT(city)`의 차이 → 8, 6
- S2-5. 2026-09-01 이후 주문만(`WHERE`, 날짜는 따옴표) 회원별 2건 이상(`HAVING`)

## S3. JOIN · LEFT JOIN

- S3-1. 취소된 주문의 `order_id`, 회원 이름, `order_date`
- S3-2. 취소 제외, 상품 카테고리별 주문 건수, 건수 내림차순·카테고리 오름차순
- S3-3. 한 번도 주문하지 않은 회원 (`LEFT JOIN` + 오른쪽 열 `IS NULL`)
- S3-4. LEFT JOIN 뒤 주문 없는 회원: `COUNT(*)` = 1, `COUNT(o.order_id)` = 0
- S3-5. 취소 제외, 회원별 총 결제 금액(가격 × 수량의 합), 금액 내림차순 (테이블 3개)

## 메모

- `COUNT()` 빈 괄호는 SQLite만 허용한다. MySQL/Oracle은 `COUNT(*)`
- SELECT에 쓴 일반 열은 모두 GROUP BY에 적는다 (Oracle은 빠지면 에러)
