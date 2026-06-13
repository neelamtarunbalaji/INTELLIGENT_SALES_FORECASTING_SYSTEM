import streamlit as st

from src.session_manager import (
    get_dataframe
)

from src.database import (
    save_dataset
)

from src.eda import (
    get_kpis
)

st.set_page_config(
    page_title="Executive Dashboard",
    layout="wide"
)

st.title(
    "📋 Executive Dashboard"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset in Data Upload page first."
    )

else:

    (
        total_revenue,
        total_quantity,
        average_revenue,
        total_products
    ) = get_kpis(df)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Revenue",
            f"₹ {total_revenue:,.0f}"
        )

    with c2:

        st.metric(
            "Quantity Sold",
            total_quantity
        )

    with c3:

        st.metric(
            "Average Revenue",
            f"₹ {average_revenue:,.0f}"
        )

    with c4:

        st.metric(
            "Products",
            total_products
        )

    st.markdown("---")

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    if st.button(
        "💾 Save Dataset To Database"
    ):

        save_dataset(df)

        st.success(
            "Dataset Saved Successfully"
        )