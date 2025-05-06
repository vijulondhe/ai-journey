import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score
import joblib

# paths
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "telco.csv"
MODEL_OUT = ROOT / "model.joblib"

# load & split
df = pd.read_csv(DATA)
X = df.drop("Churn", axis=1)
y = (df["Churn"] == "Yes").astype(int)   # encode Yes/No -> 1/0

num_cols = X.select_dtypes("number").columns
cat_cols = X.select_dtypes(exclude="number").columns

pre = ColumnTransformer(
    [("num", StandardScaler(), num_cols),
     ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)]
)

pipe = Pipeline(
    [("prep", pre),
     ("clf", RandomForestClassifier(
         n_estimators=300,
         class_weight="balanced",
         random_state=42,
         n_jobs=-1))]
)

# 5-fold CV F1
f1 = cross_val_score(pipe, X, y, cv=5, scoring="f1").mean()
print(f"RandomForest CV F1: {f1:.3f}")

# fit on full data & save
pipe.fit(X, y)
joblib.dump(pipe, MODEL_OUT)
print(f"Model saved to {MODEL_OUT}")
