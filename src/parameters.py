import pandas as pd

TOTAL_TIME = 1935  # heures

df = pd.read_csv("../data/downtime_data.csv")

df["uptime"] = TOTAL_TIME - df["total_downtime"]
df["MTBF"] = df["uptime"] / df["total_failures"]
df["lambda"] = 1 / df["MTBF"]

print(df)
