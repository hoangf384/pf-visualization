import pandas as pd

# Load data
df = pd.read_csv('Data/synthetic_data_output.csv')

# Calculate Savings
df['Savings'] = df['Income'] - df['Total Spending']
df['Savings_Rate'] = df['Savings'] / df['Income']

# Group by Age Group
age_stats = df.groupby('Age_Group').agg({
    'Income': 'mean',
    'Total Spending': 'mean',
    'Savings': 'mean',
    'Savings_Rate': 'mean'
}).reset_index()

print("--- Age Group Stats ---")
print(age_stats)

# Non-essential spending (Eating Out, Entertainment, Miscellaneous)
non_essential_cols = ['Eating_Out', 'Entertainment', 'Miscellaneous']
df['Non_Essential'] = df[non_essential_cols].sum(axis=1)
df['NE_Ratio'] = df['Non_Essential'] / df['Total Spending']

print("\n--- Spending Pattern ---")
print(f"Average Non-Essential Ratio: {df['NE_Ratio'].mean():.2%}")

# Hypothesize an A/B test for 18-25 group
young_users = df[df['Age_Group'] == '18-25'].copy()

# Giả định: App giúp người dùng giảm 10% tổng chi tiêu (Spending Reduction)
reduction_rate = 0.10
variation_spending = young_users['Total Spending'] * (1 - reduction_rate)
variation_savings_rates = (young_users['Income'] - variation_spending) / young_users['Income']

control_savings_rate = young_users['Savings_Rate'].mean()
variation_savings_rate = variation_savings_rates.mean()

print("\n--- Hypothetical A/B Test for 18-25 Group ---")
print(f"Goal: Reduce spending by {reduction_rate:.0%} through Smart Alerts")
print(f"Control (Standard Dashboard) Savings Rate: {control_savings_rate:.2%}")
print(f"Variation (Budget Alerts) Savings Rate: {variation_savings_rate:.2%}")
print(f"Lift: {variation_savings_rate - control_savings_rate:.2%}")

# insight
if control_savings_rate < 0:
    print(f"\n[INSIGHT] Nhóm 18-25 đang chi tiêu vượt mức thu nhập ({control_savings_rate:.2%}).")
    print(f"Giải pháp 'Budget Alerts' giúp cải thiện đáng kể, giảm mức thâm hụt xuống còn {variation_savings_rate:.2%}.")
else:
    print(f"\n[INSIGHT] Nhóm 18-25 đang tiết kiệm ở mức {control_savings_rate:.2%}.")
    print(f"Giải pháp 'Budget Alerts' giúp nâng tỷ lệ tiết kiệm lên {variation_savings_rate:.2%}.")
