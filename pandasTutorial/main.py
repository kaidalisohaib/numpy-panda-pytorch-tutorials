import numpy as np
import pandas as pd

data = {
    "name": ["Xavier", "Ann", "Jana", "Yi", "Robin", "Amal", "Nori"],
    "city": [
        "Mexico City",
        "Toronto",
        "Prague",
        "Shanghai",
        "Manchester",
        "Cairo",
        "Osaka",
    ],
    "age": [41, 28, 33, 34, 38, 31, 37],
    "py-score": [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0],
}
row_labels = [101, 102, 103, 104, 105, 106, 107]
df = pd.DataFrame(data=data, index=row_labels)


# Introduction
def introduction():
    print("Introduction".center(40, "="))

    # Pandas DataFrame
    print(df)

    print("\n", df.head(2))
    print(df.tail(2))

    print("\n", df["city"][103])
    print("\n", df.loc[103])


# Creating Pandas DataFrames
def creating_dataframes():
    print("Creating Pandas DataFrames".center(40, "="))
    # From a dictionary
    d = {"x": [1, 2, 3], "y": np.array([2, 4, 8]), "z": 100}
    print(pd.DataFrame(d), "\n")
    print(pd.DataFrame(d, columns=["z", "y", "x"], index=[100, 200, 300]))

    # From a list or numpy array
    list_data = [
        {"x": 1, "y": 2, "z": 100},
        {"x": 2, "y": 4, "z": 100},
        {"x": 3, "y": 8, "z": 100},
    ]
    print(pd.DataFrame(list_data))

    list_data = np.array([[1, 2, 100], [2, 4, 100], [3, 8, 1]])
    print(pd.DataFrame(list_data, columns=["x", "y", "z"], copy=True))

    # From Files
    df.to_csv("data.csv")

    print(pd.read_csv("data.csv", index_col=0))


# Retrieving Labels and Data
def retrieving_labels_and_data():
    print("Retrieving Labels and Data".center(40, "="))
    print(df.index)
    print(df.columns)
    print(df.columns[1])
    df.index = np.arange(10, 17)
    print(df)
    print(df.to_numpy())
    print(df.dtypes)
    df_ = df.astype(dtype={"age": np.int32, "py-score": np.float32})
    print(df_.dtypes)
    print("Number of dimension:", df_.ndim, "Shape:", df_.shape, "Size", df_.size)
    print(df_.memory_usage())


# Accessing and Modifying Data
def accessing_and_modifying_data():
    print("Accessing and Modifying Data".center(40, "="))
    print(df["name"])
    print(df.loc[10])
    print(df.iloc[0])
    print(df.loc[:, "city"])
    print(df.iloc[1:6, [0, 1]])
    print(df.at[12, "name"])
    print(df.iat[2, 0])
    df.loc[:13, "py-score"] = [40, 50, 60, 70]
    df.loc[14:, "py-score"] = 0
    print(df)
    df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
    print(df)


if __name__ == "__main__":
    introduction()
    creating_dataframes()
    retrieving_labels_and_data()
    accessing_and_modifying_data()
