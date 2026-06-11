import pandas as pd

perf   = pd.read_csv('data/raw/07_scheme_performance.csv')
master = pd.read_csv('data/raw/01_fund_master.csv')

RISK_MAP = {
    'low'      : 'Low',
    'moderate' : 'Moderate',
    'high'     : 'High',
}

def recommend_funds(risk_appetite: str) -> pd.DataFrame:
    key = risk_appetite.strip().lower()

    if key not in RISK_MAP:
        print("❌ Invalid input! Choose from: Low / Moderate / High")
        return pd.DataFrame()

    risk_grade = RISK_MAP[key]

    filtered = perf[perf['risk_grade'] == risk_grade].copy()

    top3 = (filtered
            .sort_values('sharpe_ratio', ascending=False)
            .head(3)
            [['scheme_name', 'fund_house', 'category',
              'sharpe_ratio', 'return_1yr_pct', 'return_3yr_pct',
              'risk_grade', 'expense_ratio_pct', 'morningstar_rating']]
            .reset_index(drop=True))

    top3.index += 1

    print(f"\n✅ Top 3 Funds for Risk Appetite: {risk_grade}\n")
    print(top3.to_string())
    return top3

if __name__ == '__main__':
    user_input = input("\nEnter risk appetite (Low / Moderate / High): ")
    recommend_funds(user_input)