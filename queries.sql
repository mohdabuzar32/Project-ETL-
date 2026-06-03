
-- 1. Top funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC;

-- 2. SIP vs Lumpsum
SELECT transaction_type, COUNT(*), SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

-- 3. State wise investment
SELECT state, SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;

-- 4. Average NAV by Fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 5. Funds with expense ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Risk grade distribution
SELECT risk_grade, COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;

-- 7. Top 5 performing funds (1 year return)
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 8. Average transaction amount by type
SELECT transaction_type, AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Total transactions by city tier
SELECT city_tier, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY city_tier;

-- 10. Fund count by category
SELECT category, COUNT(*) AS total_funds
FROM fact_performance
GROUP BY category;
