import pandas as pd

def transform_weather(data):

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
        "precipitation": data["hourly"]["precipitation"]
    })

    df["time"] = pd.to_datetime(df["time"])
    df["day"] = df["time"].dt.date
    df["month"] = df["time"].dt.month
    df["hour"] = df["time"].dt.hour

    return df