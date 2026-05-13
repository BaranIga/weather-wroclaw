def get_summary(df):
    rain_hours = (df["precipitation"] > 0).sum()
    monthly_rain = df.groupby("month")["precipitation"].sum()
    daily_temp = df.groupby("day")["temperature"].mean()
    avg_temp = df["temperature"].mean()
    max_temp = df["temperature"].max()
    min_temp = df["temperature"].min()

    hottest_day = daily_temp.idxmax()
    coldest_day = daily_temp.idxmin()
    wettest_month = monthly_rain.idxmax()

    return {
        "rain_hours": int(rain_hours),
        "avg_temperature": float(avg_temp),
        "max_temperature": float(max_temp),
        "min_temperature": float(min_temp),
        "hottest_day": str(hottest_day),
        "coldest_day": str(coldest_day),
        "wettest_month": str(wettest_month)
    }