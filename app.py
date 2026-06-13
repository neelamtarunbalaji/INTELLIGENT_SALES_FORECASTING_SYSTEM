import streamlit as st

st.set_page_config(
    page_title="Intelligent Sales Forecasting System",
    page_icon="📊",
    layout="wide"
)

st.title(
    "📊 Intelligent Sales Forecasting & Inventory Optimization System"
)

st.markdown("---")

st.markdown("""
### 🚀 AI-Powered Business Intelligence Platform

This system helps organizations:

✅ Forecast Future Sales

✅ Optimize Inventory Levels

✅ Prevent Stockouts

✅ Reduce Overstocking

✅ Generate Smart Recommendations

✅ Improve Business Decision Making
""")

st.markdown("---")

st.header("🔄 Project Workflow")

workflow_col1, workflow_col2, workflow_col3 = st.columns(3)

with workflow_col1:

    st.info("""
    📤 Data Upload

    🧹 Data Preprocessing

    📊 Sales Analytics
    """)

with workflow_col2:

    st.info("""
    🤖 Model Training

    🔮 Sales Forecasting

    📦 Inventory Optimization
    """)

with workflow_col3:

    st.info("""
    🚨 Smart Recommendations

    📄 Reports

    🗄 Database Management
    """)

st.markdown("---")

st.header("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
    Frontend

    • Streamlit
    """)

with col2:

    st.success("""
    Machine Learning

    • Scikit-Learn

    • XGBoost
    """)

with col3:

    st.success("""
    Visualization

    • Plotly

    • Matplotlib
    """)

st.markdown("---")

st.header("📁 Required Dataset Columns")

st.code("""
Order Date
Product ID
Product Name
Category
Region
Quantity Sold
Revenue
Inventory Level
Promotion Flag
Holiday Indicator
""")

st.markdown("---")

st.header("🎯 Expected Outcomes")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Sales Forecasting",
        "AI Enabled"
    )

with col2:
    st.metric(
        "Inventory Control",
        "Optimized"
    )

with col3:
    st.metric(
        "Business Insights",
        "Real-Time"
    )

with col4:
    st.metric(
        "Reports",
        "Automated"
    )

st.markdown("---")

st.success(
    "👈 Start by opening '📤 Data Upload' from the sidebar."
)