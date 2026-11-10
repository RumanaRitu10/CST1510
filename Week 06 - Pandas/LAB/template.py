"""
RECORD CHECK  -  my version
===========================

Name  :Rumana Jannat Ritu
Lane  :  AI 
Date  :29/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import pandas as pd


df = pd.read_csv(r"C:\Users\USER\Documents\CST1510\Week 06 - Pandas\LAB\records_sample.csv")

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK"))


print(df)
filter_df = df[df["status"] != "OK"]
print(filter_df)
