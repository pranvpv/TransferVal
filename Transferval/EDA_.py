import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Market value by Position

plt.figure(figsize=(10,6))
sns.boxplot(x="Pos", y="Market_Value_Million_EUR", data=df_clean)
plt.title("Market Value Distribution by Position")
plt.xticks(rotation=45)
plt.ylabel("Market Value (M €)")
plt.show()

# 2. Market Value vs Age

plt.figure(figsize=(8,5))
sns.scatterplot(x="Age", y="Market_Value_Million_EUR", data=df_clean, alpha=0.5)
plt.title("Market Value vs Age")
plt.xlabel("Age")
plt.ylabel("Market Value (M €)")
plt.show()


# 3. Market Value vs Goals/Assists

if "Gls" in df_clean.columns and "Ast" in df_clean.columns:
    fig, ax = plt.subplots(1, 2, figsize=(14,5))

    sns.scatterplot(x="Gls", y="Market_Value_Million_EUR", data=df_clean, alpha=0.5, ax=ax[0])
    ax[0].set_title("Market Value vs Goals")

    sns.scatterplot(x="Ast", y="Market_Value_Million_EUR", data=df_clean, alpha=0.5, ax=ax[1])
    ax[1].set_title("Market Value vs Assists")

    plt.show()


# 4. League/Competition influence

plt.figure(figsize=(12,6))
avg_value_by_league = df_clean.groupby("Comp")["Market_Value_Million_EUR"].mean().sort_values(ascending=False).head(15)
sns.barplot(x=avg_value_by_league.values, y=avg_value_by_league.index, palette="viridis")
plt.title("Average Market Value by Competition")
plt.xlabel("Average Market Value (M €)")
plt.show()