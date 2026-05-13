from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

import os
import logging

from config import (
  PLOTS_DIR, OUTPUTS,
  START_DATE, END_DATE
)

def save_report_to_pdf(summary, output_path=OUTPUTS["pdf"]):
    os.makedirs("output", exist_ok=True)

    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()

    elements = []

    # TITLE
    elements.append(Paragraph(
        f"Weather Report ({START_DATE} → {END_DATE})", 
        styles["Title"]
    ))
    elements.append(Spacer(1, 12))

    # DATA GENERATION DATE
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elements.append(Paragraph(f"Generated at: {generated_at}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # SUMMARY
    elements.append(Paragraph("Summary", styles["Heading2"]))
    elements.append(Spacer(1, 6))

    elements.append(Paragraph(f"Rain hours: {summary['rain_hours']}", styles["Normal"]))
    elements.append(Paragraph(f"Average temperature: {summary['avg_temperature']:.2f} °C", styles["Normal"]))
    elements.append(Paragraph(f"Max temperature: {summary['max_temperature']:.2f} °C", styles["Normal"]))
    elements.append(Paragraph(f"Min temperature: {summary['min_temperature']:.2f} °C", styles["Normal"]))
    elements.append(Spacer(1, 6))

    elements.append(Paragraph(f"Hottest day: {summary['hottest_day']}", styles["Normal"]))
    elements.append(Paragraph(f"Coldest day: {summary['coldest_day']}", styles["Normal"]))
    elements.append(Paragraph(f"Wettest month: {summary['wettest_month']}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # PLOTS
    elements.append(Paragraph("Charts", styles["Heading2"]))
    elements.append(Spacer(1, 6))

    plots = [
        "temp_trend.png",
        "monthly_temp.png",
        "monthly_rain.png",
        "temp_heatmap.png"
    ]

    for plot in plots:
        path = os.path.join(PLOTS_DIR, plot)

        if os.path.exists(path):
            img = Image(path, width=500, height=300)
            elements.append(img)
            elements.append(Spacer(1, 12))
        else:
            logging.warning(f"Missing plot: {plot}")

    doc.build(elements)