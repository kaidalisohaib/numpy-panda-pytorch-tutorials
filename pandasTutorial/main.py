import pandas as pd


def introduction():
    print("Introduction".center(30, "="))
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

    # Pandas DataFrame
    df = pd.DataFrame(data=data, index=row_labels)
    print(df)

    print("\n", df.head(2))
    print(df.tail(2))

    print("\n", df["city"][103])
    print("\n", df.loc[103])


if __name__ == "__main__":
    introduction()
