import pandas as pd
import plotly.express as px
import joblib


def actual_vs_predicted_chart(
    actual,
    predicted
):

    forecast_df = pd.DataFrame({

        "Actual":
        actual.values,

        "Predicted":
        predicted

    })

    fig = px.line(
        forecast_df,
        title="Actual vs Predicted Revenue"
    )

    return fig


def generate_future_forecast():

    model = joblib.load(
        "models/trained_models/best_model.pkl"
    )

    future_data = pd.DataFrame({

        "Quantity Sold":
        [10] * 30,

        "Inventory Level":
        [500] * 30,

        "Promotion Flag":
        [0] * 30,

        "Holiday Indicator":
        [0] * 30,

        "Day":
        list(range(1, 31)),

        "Month":
        [12] * 30,

        "Quarter":
        [4] * 30,

        "Year":
        [2026] * 30,

        "Week":
        list(range(1, 31))

    })

    predictions = model.predict(
        future_data
    )

    future_data["Forecast Revenue"] = (
        predictions
    )

    return future_data