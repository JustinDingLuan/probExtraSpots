import pandas as pd

df = pd.read_csv("data.csv")
idx = df.groupby(['student_id', 'name'])['timestamp'].idxmax()
df = df.loc[idx]
df.to_csv('data_v1.csv', index=False)