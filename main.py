from scripts.extract import get_weather_data
from scripts.transform import transform_weather
from scripts.load import save_to_csv

from analysis.stats import get_summary
from analysis.export import save_summary_to_json
from analysis.plots import (
    plot_temperature_time,
    plot_monthly_temp,
    plot_monthly_rain,
    plot_temperature_heatmap
)
from analysis.export_pdf import save_report_to_pdf

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Starting ETL pipeline...")

    # ETL
    data = get_weather_data()

    if data is None:
        logging.error("No data from API")
        return
    
    logging.info("Data fetched successfully")

    df = transform_weather(data)

    if df is None or df.empty:
        logging.error("DataFrame is empty after transformation")
        return

    logging.info(f"DataFrame ready: {len(df)} rows")

    save_to_csv(df)

    # analysis
    summary = get_summary(df)

    # output -> json
    save_summary_to_json(summary)
    logging.info("Summary saved to JSON")

    plot_temperature_time(df)
    plot_monthly_temp(df)
    plot_monthly_rain(df)
    plot_temperature_heatmap(df)

    save_report_to_pdf(summary)

    logging.info("All plots generated successfully")

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()