
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
