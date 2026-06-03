# Data Dictionary

## nav_clean.csv

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual fund scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## transactions_clean.csv

| Column | Data Type | Description |
|----------|-----------|-------------|
| investor_id | String | Investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Fund code |
| transaction_type | String | SIP/LUMPSUM/REDEMPTION |
| amount_inr | Integer | Transaction amount |
| state | String | Investor state |
| city | String | Investor city |
| kyc_status | String | KYC status |

## performance_clean.csv

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Fund code |
| scheme_name | String | Scheme name |
| return_1yr_pct | Float | 1 year return |
| return_3yr_pct | Float | 3 year return |
| return_5yr_pct | Float | 5 year return |
| expense_ratio_pct | Float | Expense ratio |
| risk_grade | String | Risk category |