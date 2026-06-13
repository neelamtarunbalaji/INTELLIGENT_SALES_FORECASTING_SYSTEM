import streamlit as st

from src.session_manager import (
    get_dataframe
)

st.set_page_config(
    page_title="Data Preprocessing",
    layout="wide"
)

st.title(
    "🧹 Data Preprocessing"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset first."
    )

else:

    st.subheader(
        "Dataset Shape"
    )

    st.write(
        df.shape
    )

    st.markdown("---")

    st.subheader(
        "Missing Values"
    )

    st.dataframe(
        df.isnull().sum().reset_index(
            name="Missing Count"
        ),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Duplicate Records"
    )

    duplicates = df.duplicated().sum()

    st.metric(
        "Duplicate Rows",
        duplicates
    )

    st.markdown("---")

    st.subheader(
        "Data Types"
    )

    st.dataframe(
        df.dtypes.astype(str)
        .reset_index(),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Feature Engineered Columns"
    )

    st.write([

        "Day",
        "Month",
        "Quarter",
        "Year",
        "Week"

    ])

    st.markdown("---")

    st.subheader(
        "Processed Dataset Preview"
    )

    st.dataframe(
        df.head(),
        use_container_width=True
    )