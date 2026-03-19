import pandas as pd
import numpy as np

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
# Goal: Increase Savings Rate by 5% through "Smart Alerts"
control_savings_rate = young_users['Savings_Rate'].mean()
variation_savings_rate = control_savings_rate * 1.5 # Assume 50% improvement for the sake of simulation

print("\n--- Hypothetical A/B Test for 18-25 Group ---")
print(f"Control (Standard Dashboard) Savings Rate: {control_savings_rate:.2%}")
print(f"Variation (Budget Alerts) Savings Rate: {variation_savings_rate:.2%}")
print(f"Lift: {variation_savings_rate - control_savings_rate:.2%}")
