import streamlit as st

from src.session_manager import (
    get_dataframe
)

st.set_page_config(
    page_title="Smart Recommendations",
    layout="wide"
)

st.title(
    "🚨 Smart Recommendations"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset first."
    )

else:

    st.subheader(
        "Business Intelligence Insights"
    )

    st.markdown("---")

    # ==========================
    # Best Product
    # ==========================

    best_product = (
        df.groupby(
            "Product Name"
        )["Revenue"]
        .sum()
        .idxmax()
    )

    best_product_revenue = (
        df.groupby(
            "Product Name"
        )["Revenue"]
        .sum()
        .max()
    )

    # ==========================
    # Worst Product
    # ==========================

    worst_product = (
        df.groupby(
            "Product Name"
        )["Revenue"]
        .sum()
        .idxmin()
    )

    worst_product_revenue = (
        df.groupby(
            "Product Name"
        )["Revenue"]
        .sum()
        .min()
    )

    # ==========================
    # Best Region
    # ==========================

    best_region = (
        df.groupby(
            "Region"
        )["Revenue"]
        .sum()
        .idxmax()
    )

    # ==========================
    # Worst Region
    # ==========================

    worst_region = (
        df.groupby(
            "Region"
        )["Revenue"]
        .sum()
        .idxmin()
    )

    c1, c2 = st.columns(2)

    with c1:

        st.success(
            f"🏆 Best Product: {best_product}"
        )

        st.write(
            f"Revenue: ₹ {best_product_revenue:,.0f}"
        )

    with c2:

        st.error(
            f"📉 Worst Product: {worst_product}"
        )

        st.write(
            f"Revenue: ₹ {worst_product_revenue:,.0f}"
        )

    st.markdown("---")

    c3, c4 = st.columns(2)

    with c3:

        st.success(
            f"🌎 Best Region: {best_region}"
        )

    with c4:

        st.warning(
            f"⚠ Worst Region: {worst_region}"
        )

    st.markdown("---")

    # ==========================
    # Low Stock Alert
    # ==========================

    low_stock = df[
        df["Inventory Level"] < 50
    ]

    st.subheader(
        "📦 Low Stock Alerts"
    )

    if len(low_stock) > 0:

        st.dataframe(
            low_stock[
                [
                    "Product Name",
                    "Inventory Level"
                ]
            ].drop_duplicates(),
            use_container_width=True
        )

    else:

        st.success(
            "No Low Stock Alerts"
        )

    st.markdown("---")

    # ==========================
    # Business Recommendations
    # ==========================

    st.subheader(
        "💡 AI Business Recommendations"
    )

    recommendations = []

    recommendations.append(
        f"Increase inventory for '{best_product}' due to high revenue performance."
    )

    recommendations.append(
        f"Investigate poor sales performance of '{worst_product}'."
    )

    recommendations.append(
        f"Expand marketing efforts in '{best_region}' region."
    )

    recommendations.append(
        f"Review sales strategy for '{worst_region}' region."
    )

    if len(low_stock) > 0:

        recommendations.append(
            "Reorder inventory for low-stock products immediately."
        )

    for rec in recommendations:

        st.info(rec)