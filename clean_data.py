import pandas as pd

df = pd.read_csv("data/raw/nav_history.csv")

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(['amfi_code', 'date'])
df = df.drop_duplicates()
df = df[df['nav'] > 0]

df['nav'] = df.groupby('amfi_code')['nav'].ffill()

df.to_csv("data/processed/nav_clean.csv", index=False)

print("DONE NAV CLEANING")

import pandas as pd

# -------------------------
# 1. NAV HISTORY CLEANING
# -------------------------
nav = pd.read_csv("data/raw/nav_history.csv")

nav['date'] = pd.to_datetime(nav['date'])
nav = nav.sort_values(['amfi_code', 'date'])
nav = nav.drop_duplicates()
nav = nav[nav['nav'] > 0]
nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()

nav.to_csv("data/processed/nav_clean.csv", index=False)
print("NAV CLEANED")


# -------------------------
# 2. TRANSACTIONS CLEANING
# -------------------------
txn = pd.read_csv("data/raw/investor_transactions.csv")

txn['date'] = pd.to_datetime(txn['date'])
txn['transaction_type'] = txn['transaction_type'].str.upper()

txn = txn[txn['transaction_type'].isin(['SIP', 'LUMPSUM', 'REDEMPTION'])]
txn = txn[txn['amount'] > 0]

txn.to_csv("data/processed/transactions_clean.csv", index=False)
print("TRANSACTIONS CLEANED")


# -------------------------
# 3. PERFORMANCE CLEANING
# -------------------------
perf = pd.read_csv("data/raw/scheme_performance.csv")

perf['returns'] = pd.to_numeric(perf['returns'], errors='coerce')
perf = perf.dropna()

perf = perf[(perf['expense_ratio'] >= 0.1) & (perf['expense_ratio'] <= 2.5)]

perf.to_csv("data/processed/performance_clean.csv", index=False)
print("PERFORMANCE CLEANED")


print("ALL CLEANING DONE SUCCESSFULLY")