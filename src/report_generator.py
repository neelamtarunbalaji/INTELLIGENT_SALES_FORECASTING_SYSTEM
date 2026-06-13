import os
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_report_folders():

    os.makedirs(
        "reports/pdf",
        exist_ok=True
    )

    os.makedirs(
        "reports/excel",
        exist_ok=True
    )

    os.makedirs(
        "reports/csv",
        exist_ok=True
    )


def generate_pdf_report(df):

    create_report_folders()

    pdf_path = "reports/pdf/sales_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Sales Forecasting Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Total Revenue: ₹ {df['Revenue'].sum():,.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Total Quantity Sold: {df['Quantity Sold'].sum():,.0f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Unique Products: {df['Product ID'].nunique()}",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_path


def generate_excel_report(df):

    create_report_folders()

    excel_path = "reports/excel/sales_report.xlsx"

    df.to_excel(
        excel_path,
        index=False
    )

    return excel_path


def generate_csv_report(df):

    create_report_folders()

    csv_path = "reports/csv/sales_report.csv"

    df.to_csv(
        csv_path,
        index=False
    )

    return csv_path