import os
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import (
    LinearRegression
)

from sklearn.ensemble import (
    RandomForestRegressor
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

try:
    from xgboost import XGBRegressor
except Exception:
    XGBRegressor = None


def train_models(df):

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

    X = df[features]

    y = df["Revenue"]

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42

    )

    models = {

    "Linear Regression":
    LinearRegression(),

    "Random Forest":
    RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "XGBoost":
    XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        random_state=42
    )

}

    results = {}

    best_model = None

    best_model_name = ""

    best_score = -999

    for name, model in models.items():

        model.fit(

            X_train,

            y_train

        )

        predictions = model.predict(

            X_test

        )

        mae = mean_absolute_error(

            y_test,

            predictions

        )

        rmse = (

            mean_squared_error(

                y_test,

                predictions

            ) ** 0.5

        )

        r2 = r2_score(

            y_test,

            predictions

        )

        results[name] = {

            "MAE":
            round(mae, 2),

            "RMSE":
            round(rmse, 2),

            "R2":
            round(r2, 4),

            "Actual":
            y_test,

            "Predictions":
            predictions

        }

        if r2 > best_score:

            best_score = r2

            best_model = model

            best_model_name = name

    model_folder = os.path.join(

        "models",

        "trained_models"

    )

    os.makedirs(

        model_folder,

        exist_ok=True

    )

    joblib.dump(

        best_model,

        os.path.join(

            model_folder,

            "best_model.pkl"

        )

    )

    return (

        results,

        best_model_name

    )