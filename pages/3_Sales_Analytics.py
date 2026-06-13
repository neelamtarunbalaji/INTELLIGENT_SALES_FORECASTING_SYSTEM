import streamlit as st

from src.session_manager import (
    get_dataframe
)

from src.eda import (
    sales_trend_chart,
    monthly_revenue_chart,
    category_chart,
    region_chart,
    top_products_chart
)


st.title(
    "📈 Sales Analytics"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset in Executive Dashboard first."
    )

else:

    st.plotly_chart(
        sales_trend_chart(df),
        use_container_width=True
    )

    st.plotly_chart(
        monthly_revenue_chart(df),
        use_container_width=True
    )

    st.plotly_chart(
        category_chart(df),
        use_container_width=True
    )

    st.plotly_chart(
        region_chart(df),
        use_container_width=True
    )

    st.plotly_chart(
        top_products_chart(df),
        use_container_width=True
    )