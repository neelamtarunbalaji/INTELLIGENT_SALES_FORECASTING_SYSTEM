import streamlit as st


def save_dataframe(df):

    st.session_state["sales_df"] = df


def get_dataframe():

    return st.session_state.get(
        "sales_df",
        None
    )


def has_dataframe():

    return "sales_df" in st.session_state