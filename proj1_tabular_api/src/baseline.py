import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score

# 1) load CSV
df = pd.read_csv(r"data\telco.csv")   # or telco_clean.csv

# 2) split features vs target
X = df.drop("Churn", axis=1)
y_str = df["Churn"]

# 3) encode Yes/No -> 1/0
le = LabelEncoder()
y = le.fit_transform(y_str)           # ['No','Yes'] -> [0,1]

# 4) most-frequent baseline
baseline = DummyClassifier(strategy="most_frequent")

# 5) 5-fold cross-validated F1
f1 = cross_val_score(baseline, X, y, cv=5, scoring="f1").mean()
print(f"Baseline F1: {f1:.3f}")
