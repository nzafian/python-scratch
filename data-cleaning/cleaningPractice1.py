import numpy as np
import pandas as pd

# Raw or messy data
df = pd.read_csv("Messy_Employee_dataset.csv")

print(f"Loaded Raw Dataset: {df.shape[0]} rows, {df.shape[1]} columns\n")

#How to clean headers
print("Before cleaning header:")
print(df.columns.tolist())

df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
print("After cleaning:")
print(f"{df.columns.tolist()}\n")