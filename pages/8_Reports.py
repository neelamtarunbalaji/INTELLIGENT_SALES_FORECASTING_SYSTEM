import streamlit as st
import os

from src.session_manager import (
    get_dataframe
)

from src.report_generator import (
    generate_pdf_report,
    generate_excel_report,
    generate_csv_report
)

st.set_page_config(
    page_title="Reports",
    layout="wide"
)

st.title(
    "📄 Reports Dashboard"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset first."
    )

else:

    if st.button(
        "📊 Generate Reports"
    ):

        generate_pdf_report(df)

        generate_excel_report(df)

        generate_csv_report(df)

        st.success(
            "Reports Generated Successfully"
        )

    st.markdown("---")

    pdf_path = (
        "reports/pdf/sales_report.pdf"
    )

    excel_path = (
        "reports/excel/sales_report.xlsx"
    )

    csv_path = (
        "reports/csv/sales_report.csv"
    )

    st.subheader(
        "📥 Download Reports"
    )

    col1, col2, col3 = st.columns(3)

    # PDF
    with col1:

        if os.path.exists(pdf_path):

            with open(
                pdf_path,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download PDF",
                    data=file,
                    file_name="sales_report.pdf",
                    mime="application/pdf"
                )

    # Excel
    with col2:

        if os.path.exists(excel_path):

            with open(
                excel_path,
                "rb"
            ) as file:

                st.download_button(
                    label="📊 Download Excel",
                    data=file,
                    file_name="sales_report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    # CSV
    with col3:

        if os.path.exists(csv_path):

            with open(
                csv_path,
                "rb"
            ) as file:

                st.download_button(
                    label="📋 Download CSV",
                    data=file,
                    file_name="sales_report.csv",
                    mime="text/csv"
                )

    st.markdown("---")

    st.subheader(
        "📁 Generated Files"
    )

    if os.path.exists(pdf_path):

        st.success(
            f"PDF Report Ready ({round(os.path.getsize(pdf_path)/1024,2)} KB)"
        )

    if os.path.exists(excel_path):

        st.success(
            f"Excel Report Ready ({round(os.path.getsize(excel_path)/(1024*1024),2)} MB)"
        )

    if os.path.exists(csv_path):

        st.success(
            f"CSV Report Ready ({round(os.path.getsize(csv_path)/(1024*1024),2)} MB)"
        )