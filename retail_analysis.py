import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Sales Data")
print(df)

print("\nAverage Sales:", df["Sales"].mean())
print("Highest Sales:", df["Sales"].max())
print("Lowest Sales:", df["Sales"].min())
