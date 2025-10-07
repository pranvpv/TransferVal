df = pd.read_excel(r"D:\TransferVal\PLAYER_DATA.xlsx")
df_clean = df.drop(columns=["Rk", "Player"], errors="ignore").copy()
df_clean = df_clean[df_clean["Market_Value_Million_EUR"].notnull()]
threshold = 0.7
missing_ratio = df_clean.isnull().mean()
cols_to_drop = missing_ratio[missing_ratio > threshold].index
df_clean.drop(columns=cols_to_drop, inplace=True)

categorical_cols = df_clean.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = df_clean.select_dtypes(include=["int64", "float64"]).columns.tolist()

