import streamlit as st
import pandas as pd
import joblib
import os

from src.session_manager import (
    get_dataframe
)


st.set_page_config(
    page_title="Sales Forecasting",
    layout="wide"
)

st.title(
    "🔮 Sales Forecasting"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset first."
    )

else:

    model_path = os.path.join(

        "models",
        "trained_models",
        "best_model.pkl"

    )

    if not os.path.exists(

        model_path

    ):

        st.warning(
            "Please train models first."
        )

    else:

        model = joblib.load(

            model_path

        )

        st.success(
            "Best Model Loaded Successfully"
        )

        forecast_days = st.slider(

            "Forecast Period (Days)",

            min_value=7,

            max_value=90,

            value=30

        )

        if st.button(

            "Generate Forecast"

        ):

            latest_data = df.tail(
                forecast_days
            ).copy()

            features = [

                "Quantity Sold",
                "Inventory Level",
                "Promotion Flag",
                "Holiday Indicator",
                "Day",
                "Month",
                "Quarter",
                "Year",
                "Week"

            ]

            predictions = model.predict(

                latest_data[
                    features
                ]

            )

            forecast_df = pd.DataFrame({

                "Forecast":
                predictions

            })

            st.subheader(
                "Forecast Results"
            )

            st.dataframe(

                forecast_df,

                use_container_width=True

            )

            st.line_chart(

                forecast_df,

                use_container_width=True

            )

            st.success(
                f"{forecast_days} Day Forecast Generated"
            )