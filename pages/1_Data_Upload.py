import streamlit as st

from src.data_upload import (
    load_dataset,
    validate_dataset
)

from src.preprocessing import (
    clean_data,
    standardize_columns
)

from src.feature_engineering import (
    create_features
)

from src.session_manager import (
    save_dataframe
)

st.set_page_config(
    page_title="Data Upload",
    layout="wide"
)

st.title(
    "📤 Data Upload"
)

st.markdown(
    "Upload a CSV or Excel dataset to begin analysis."
)

uploaded_file = st.file_uploader(
    "Choose CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    try:

        df = load_dataset(
            uploaded_file
        )

        df = standardize_columns(
            df
        )

        missing_cols = validate_dataset(
            df
        )

        if len(missing_cols) > 0:

            st.error(
                f"❌ Missing Required Columns: {missing_cols}"
            )

        else:

            # ==========================
            # PREPROCESSING
            # ==========================

            df = clean_data(
                df
            )

            # ==========================
            # FEATURE ENGINEERING
            # ==========================

            df = create_features(
                df
            )

            # ==========================
            # SAVE TO SESSION
            # ==========================

            save_dataframe(
                df
            )

            st.success(
                "✅ Dataset Uploaded Successfully"
            )

            st.markdown("---")

            st.subheader(
                "Dataset Preview"
            )

            st.dataframe(
                df.head(),
                use_container_width=True
            )

            st.markdown("---")

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Rows",
                    df.shape[0]
                )

            with c2:

                st.metric(
                    "Columns",
                    df.shape[1]
                )

            st.subheader(
                "Column Names"
            )

            st.write(
                df.columns.tolist()
            )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

else:

    st.info(
        "📂 Upload a dataset to continue."
    )