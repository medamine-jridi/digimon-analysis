
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DigiDB_digimonlist.csv")

print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nDescriptive statistics:")
print(df.describe())
print("\nColumns:")
print(df.columns)

print("\nMissing values per column:")
print(df.isnull().sum())

df = df.dropna(subset=["Lv50 Atk", "Type", "Stage"])
plt.figure(figsize=(8, 5))
df["Lv50 Atk"].plot(kind="hist", bins=15)
plt.title("Distribution of Lv50 Attack")
plt.xlabel("Attack")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

avg_attack_by_type = df.groupby("Type")["Lv50 Atk"].mean().sort_values(ascending=False)
print("\nAverage Lv50 Attack by Type:")
print(avg_attack_by_type)

plt.figure(figsize=(8, 5))
avg_attack_by_type.plot(kind="bar")
plt.title("Average Lv50 Attack by Type")
plt.xlabel("Type")
plt.ylabel("Average Attack")
plt.tight_layout()
plt.show()

avg_attack_by_stage = df.groupby("Stage")["Lv50 Atk"].mean().sort_values(ascending=False)
print("\nAverage Lv50 Attack by Stage:")
print(avg_attack_by_stage)

plt.figure(figsize=(8, 5))
avg_attack_by_stage.plot(kind="bar")
plt.title("Average Lv50 Attack by Stage")
plt.xlabel("Stage")
plt.ylabel("Average Attack")
plt.tight_layout()
plt.show()

top_10 = df.nlargest(10, "Lv50 Atk")[["Digimon", "Stage", "Type", "Lv50 Atk"]]
print("\nTop 10 Digimon by Lv50 Attack:")
print(top_10)
