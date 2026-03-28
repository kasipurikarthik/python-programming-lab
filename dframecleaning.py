import pandas as pd
data = {
    "Name": ["karthik", "akhil", "chandu", "surya"],
    "Age": [20, None, 20, 22],
    "Marks": [None, 90, 85, None]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df["Name"] = df["Name"].str.strip()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(0)
df.drop_duplicates(inplace=True)
print("After Data Cleaning:")
print(df)
df["Result"] = "Pass"
df.loc[df["Marks"] < 40, "Result"] = "Fail"
df.rename(columns={"Marks": "Score"}, inplace=True)
df.drop("Age", axis=1, inplace=True)
print("After DataFrame Modification:")
print(df)