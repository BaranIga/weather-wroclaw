import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os
import seaborn as sns

from config import (
    PLOTS_DIR, PINK_PALETTE, 
    FIGSIZE_LARGE, FIGSIZE_MEDIUM, 
    DPI
)

plt.style.use("seaborn-v0_8-whitegrid")

plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.labelsize": 12
})

os.makedirs(PLOTS_DIR, exist_ok=True)

# PLOTS
# temperature over time
def plot_temperature_time(df):
    plt.figure(figsize=(FIGSIZE_LARGE))
    plt.plot(df["time"], df["temperature"], color="#ff69b4", linewidth=1.5)
    plt.title("Hourly Temperature - Wrocław 2024")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(f"{PLOTS_DIR}/temp_trend.png", dpi=DPI)
    plt.show()

# average monthly temperature
def plot_monthly_temp(df):
    monthly_temp = df.groupby("month")["temperature"].mean()

    plt.figure(figsize=(FIGSIZE_MEDIUM))
    monthly_temp.plot(kind="bar", color=PINK_PALETTE, edgecolor="white")
    plt.title("Average Monthly Temperature")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(f"{PLOTS_DIR}/monthly_temp.png", dpi=DPI)
    plt.show()

# monthly precipitation
def plot_monthly_rain(df):
    monthly_rain = df.groupby("month")["precipitation"].sum()

    plt.figure(figsize=(FIGSIZE_MEDIUM))
    monthly_rain.plot(kind="bar", color=PINK_PALETTE[::-1], edgecolor="white")
    plt.title("Monthly Precipitation")
    plt.xlabel("Month")
    plt.ylabel("Rain (mm)")
    plt.tight_layout()
    plt.savefig(f"{PLOTS_DIR}/monthly_rain.png", dpi=DPI)
    plt.show()

# temperature heatmap graph
def plot_temperature_heatmap(df):
    heatmap_data = df.pivot_table(
        values="temperature",
        index="hour",
        columns="month",
        aggfunc="mean"
    )

    heatmap_data.columns = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    plt.figure(figsize=(12,6))

    ax = sns.heatmap(
        heatmap_data,
        cmap="PuRd",
        center=df["temperature"].mean(),
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": "Temperature °C", "shrink": 0.8}
    )

    ax.invert_yaxis()

    plt.title("Average Temperature Heatmap")
    plt.xlabel("Month")
    plt.ylabel("Hour")

    plt.tight_layout()

    plt.savefig(f"{PLOTS_DIR}/temp_heatmap.png", dpi=DPI)

    plt.show()