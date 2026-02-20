import pandas as pd

def clean_train(df):
    df = df.copy()

    df = df.drop_duplicates()
    df = df[df["sales"] >= 0]

    df = df.sort_values(["store_nbr", "family", "date"])

    return df


def clean_oil(df):
    df = df.sort_values("date")
    df["dcoilwtico"] = df["dcoilwtico"].ffill().bfill()
    return df


def clean_holiday(df):
    df = df[df["transferred"] == False].copy()
    df["is_holiday"] = True
    return df[["date", "is_holiday"]]
