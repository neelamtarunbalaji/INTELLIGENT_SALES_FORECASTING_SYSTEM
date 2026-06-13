import pandas as pd
import plotly.express as px


# =====================================
# KPI CALCULATIONS
# =====================================

def get_kpis(df):

    total_revenue = df["Revenue"].sum()

    total_quantity = df["Quantity Sold"].sum()

    average_revenue = round(
        df["Revenue"].mean(),
        2
    )

    total_products = (
        df["Product ID"]
        .nunique()
    )

    return (
        total_revenue,
        total_quantity,
        average_revenue,
        total_products
    )


# =====================================
# SALES TREND
# =====================================

def sales_trend_chart(df):

    daily_sales = (
        df.groupby("Order Date")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily_sales,
        x="Order Date",
        y="Revenue",
        title="Sales Trend Analysis"
    )

    return fig


# =====================================
# MONTHLY REVENUE
# =====================================

def monthly_revenue_chart(df):

    monthly = (
        df.groupby("Month")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        monthly,
        x="Month",
        y="Revenue",
        title="Monthly Revenue Analysis"
    )

    return fig


# =====================================
# CATEGORY PERFORMANCE
# =====================================

def category_chart(df):

    category = (
        df.groupby("Category")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category,
        x="Category",
        y="Revenue",
        title="Category Wise Revenue"
    )

    return fig


# =====================================
# REGION PERFORMANCE
# =====================================

def region_chart(df):

    region = (
        df.groupby("Region")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region,
        names="Region",
        values="Revenue",
        title="Region Wise Revenue"
    )

    return fig


# =====================================
# TOP PRODUCTS
# =====================================

def top_products_chart(df):

    top_products = (
        df.groupby("Product Name")
        ["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Product Name",
        y="Revenue",
        title="Top Selling Products"
    )

    return fig


# =====================================
# PROMOTION IMPACT
# =====================================

def promotion_chart(df):

    promotion = (
        df.groupby("Promotion Flag")
        ["Revenue"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        promotion,
        x="Promotion Flag",
        y="Revenue",
        title="Promotion Impact Analysis"
    )

    return fig