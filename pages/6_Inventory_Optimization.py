import streamlit as st

from src.session_manager import (
    get_dataframe
)

from src.inventory_optimization import (
    calculate_inventory_metrics,
    stock_alerts
)


st.title(
    "📦 Inventory Dashboard"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset in Executive Dashboard first."
    )

else:

    metrics = calculate_inventory_metrics(df)

    stock, status = stock_alerts(
        df,
        metrics["Reorder Point"]
    )

    st.subheader(
        "Inventory Metrics"
    )

    st.write(metrics)

    st.success(status)