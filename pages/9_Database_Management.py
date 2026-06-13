import streamlit as st

from src.database import (
    load_database_data
)

st.set_page_config(
    page_title="Database Viewer",
    layout="wide"
)

st.title(
    "🗄 Database Records"
)

if st.button(
    "Load Records"
):

    df = load_database_data()

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success(
        f"{len(df)} Records Loaded"
    )