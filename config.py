# API
BASE_URL = "https://archive-api.open-meteo.com/v1/archive"
LATITUDE = 51.1079
LONGITUDE = 17.0385
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"
TIMEZONE = "Europe/Warsaw"

# Paths
DATA_PATH = "data/wroclaw_weather.csv"
OUTPUTS = {
  "json": "output/summary.json",
  "pdf": "output/report.pdf"
}
PLOTS_DIR = "plots"

# Plot settings
FIGSIZE_LARGE = (12, 5)
FIGSIZE_MEDIUM = (10, 5)
DPI = 300

# Style
PINK_PALETTE = [
    "#ffb6c1",
    "#ff69b4",
    "#db7093",
    "#c71585",
    "#ff85a2"
]