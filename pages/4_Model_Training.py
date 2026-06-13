import streamlit as st
import pandas as pd

from src.session_manager import (
    get_dataframe
)

from src.model_training import (
    train_models
)

st.set_page_config(
    page_title="Model Training",
    layout="wide"
)

st.title(
    "🤖 Model Training"
)

df = get_dataframe()

if df is None:

    st.warning(
        "Please upload dataset first."
    )

else:

    st.subheader(
        "Machine Learning Models"
    )

    st.write(
        """
        Models Used:
        - Linear Regression
        - Random Forest Regressor
        - XGBoost Regressor
        """
    )

    if st.button(
        "🚀 Train Models"
    ):

        with st.spinner(
            "Training Models..."
        ):

            results, best_model_name = train_models(df)

        st.success(
            f"🏆 Best Model: {best_model_name}"
        )

        st.markdown("---")

        st.subheader(
            "Model Comparison"
        )

        comparison_data = []

        for model_name, metrics in results.items():

            comparison_data.append({

                "Model":
                model_name,

                "MAE":
                metrics["MAE"],

                "RMSE":
                metrics["RMSE"],

                "R2 Score":
                metrics["R2"]

            })

        comparison_df = pd.DataFrame(
            comparison_data
        )

        st.dataframe(
            comparison_df,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader(
            "Best Model Summary"
        )

        best_metrics = results[
            best_model_name
        ]

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "MAE",
                best_metrics["MAE"]
            )

        with c2:

            st.metric(
                "RMSE",
                best_metrics["RMSE"]
            )

        with c3:

            st.metric(
                "R² Score",
                best_metrics["R2"]
            )

        st.markdown("---")

        st.success(
            f"""
            Best Performing Model:
            {best_model_name}
            """
        )