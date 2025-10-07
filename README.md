#  Transfer Val — Football Player Market Value Prediction  
##  Overview  

**Transfer Val** is a machine learning project that predicts and analyzes the market value of professional football players from **Europe’s Top 5 Leagues** — the Premier League, La Liga, Serie A, Bundesliga, and Ligue 1.  

The project combines **data science and football analytics** to understand what influences a player’s market value. Using attributes such as age, position, performance metrics, and reputation, Transfer Val provides data-driven insights into player valuation and the financial dynamics of modern football.

---

##  Data Collection  

The dataset was built using a combination of **web scraping** and **open-source data**.  

---

##  Web Scraping Process  

The Premier League data was extracted through automated scraping of structured JSON endpoints. Each iteration collected player statistics and appended them to a clean dataset, later saved as a CSV file for integration with Kaggle data.  

This ensured **real-time, authentic player information**, capturing live performance metrics such as goals, assists, club affiliation, and position.

- **Premier League Data:** Player statistics were gathered by scraping the official Premier League API using Python libraries such as *BeautifulSoup*, *cloudscraper*, and *requests*. The data included player names, clubs, countries, positions, goals, and assists for the 2024 season.  
- **Other Leagues Data:** Information for La Liga, Serie A, Bundesliga, and Ligue 1 players was sourced from **Kaggle**, containing detailed attributes on performance, defense, passing, possession, and overall ratings.  

This blend of live and public data created a comprehensive dataset representing Europe’s elite competitions.


```python

goals=[]
assists=[]
name=[]
country=[]
club=[]
position=[]
url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v2/competitions/8/seasons/2024/players/stats/leaderboard?_sort=goals%3Adesc&_limit=10"
for i in range (0,25):
    scraper = cloudscraper.create_scraper()

    response = scraper.get(url)
    data1 = response.json()
    next_token = data1["pagination"]["_next"]
    
```
---

##  Data Cleaning & Preparation  

Extensive preprocessing steps were applied to ensure data quality:  
- Removed unnecessary columns such as player rank and redundant identifiers.  
- Filtered out rows with missing market-value data.  
- Dropped columns containing more than 70 % missing values.  
- Distinguished and formatted categorical and numerical features for later modeling.  
- Standardized data types and column structures for compatibility.  

These steps produced a clean, consistent dataset ready for feature engineering and model training.
```python
df = pd.read_excel(r"D:\TransferVal\PLAYER_DATA.xlsx")
df_clean = df.drop(columns=["Rk", "Player"], errors="ignore").copy()
df_clean = df_clean[df_clean["Market_Value_Million_EUR"].notnull()]
threshold = 0.7
missing_ratio = df_clean.isnull().mean()
cols_to_drop = missing_ratio[missing_ratio > threshold].index
df_clean.drop(columns=cols_to_drop, inplace=True)

categorical_cols = df_clean.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = df_clean.select_dtypes(include=["int64", "float64"]).columns.tolist()
```
---

##  Feature Engineering  

Categorical variables were converted into numeric form, and numerical attributes were standardized.  
Features such as position, age, goals, assists, expected goals (xG), expected assists (xAG), and progressive metrics were retained, resulting in a well-structured feature matrix suitable for predictive modeling.

---

##  Model Building & Training  

The dataset was split into **training (80 %)** and **testing (20 %)** sets, maintaining balanced representation across leagues and positions.  
Missing numerical values were imputed using statistical methods to ensure completeness.  

A **Linear Regression** model was trained as the baseline predictor for *Market Value (M €)* and evaluated using RMSE, MAE, and R² scores to measure its accuracy and explanatory power.

---

##  Exploratory Data Analysis (EDA)  

Comprehensive analysis and visualization were conducted to understand the relationships between variables:  
- **Position Analysis:** Forwards and attacking midfielders generally exhibit higher market values.  
- **Age Trend:** Player valuation peaks between ages 24 and 29, aligning with prime career years.  
- **Performance Correlation:** Goals, assists, and xG/xAG metrics show strong positive correlation with value.  
- **League Comparison:** Premier League players, on average, hold the highest market values among all five leagues.  

These findings validated feature selection and guided modeling decisions.

```python
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


```

![Alt text](https://github.com/pranvpv/TransferVal/blob/main/Graphs/Screenshot%202025-10-08%20011758.png)
![Alt text](https://github.com/pranvpv/TransferVal/blob/main/Graphs/Screenshot%202025-10-08%20011815.png)

---

##  Model Evaluation  

Model performance was assessed through:  
- **RMSE (Root Mean Squared Error)** – overall prediction accuracy  
- **MAE (Mean Absolute Error)** – average deviation from actual market values  
- **R² Score** – proportion of variance explained by the model  

The model achieved an **accuracy of approximately 53 %**, showing strong correlation between predicted and actual market values.  

This baseline model successfully captured key patterns in player valuation using simple linear regression.

```python
categorical_cols = df_clean.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = df_clean.select_dtypes(include=["int64", "float64"]).columns.tolist()

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df_clean, columns=categorical_cols, drop_first=True)

# Define features (X) and target (y)
X = df_encoded.drop(columns=["Market_Value_Million_EUR"])
y = df_encoded["Market_Value_Million_EUR"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42 )
```
![Alt text](https://github.com/pranvpv/TransferVal/blob/main/Graphs/Screenshot%202025-10-08%20012837.png)

---

##  Key Insights  

- **Premier League** players were found to be the most highly valued among all leagues.  
- **Forwards** held the highest market value on average, followed by attacking midfielders.  
- **Expected Goals (xG)** and **Expected Assists (xAG)** were the **most influential features** driving player valuation.  
- Player **age**, **position**, and **performance metrics** significantly affect market value.  
- Data-driven models can offer a quantitative view of how player performance translates into financial worth.

---

##  Tech Stack  

- **Programming:** Python  
- **Libraries:** pandas • NumPy • scikit-learn • Matplotlib • Seaborn  
- **Web Scraping:** BeautifulSoup • requests • cloudscraper  
- **Visualization & Analysis:** Jupyter Notebook  
- **Deployment (optional):** FastAPI  

---

##  Summary  

**Transfer Val** is an end-to-end data-science project integrating data collection, web scraping, preprocessing, exploratory analysis, and machine learning to predict football player market values.  
It demonstrates practical skills in **data engineering, model development, and sports analytics**, achieving **53 % prediction accuracy** while uncovering key factors influencing player valuation across Europe’s top leagues.

---

