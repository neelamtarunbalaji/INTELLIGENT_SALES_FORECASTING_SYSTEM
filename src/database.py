import sqlite3
import pandas as pd


DB_NAME = "sales_forecasting.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        order_date TEXT,

        product_id TEXT,

        product_name TEXT,

        category TEXT,

        region TEXT,

        quantity_sold INTEGER,

        revenue REAL,

        inventory_level INTEGER,

        promotion_flag INTEGER,

        holiday_indicator INTEGER

    )
    """)

    conn.commit()

    conn.close()


def save_dataset(df):

    create_database()

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO sales_data
            (
                order_date,
                product_id,
                product_name,
                category,
                region,
                quantity_sold,
                revenue,
                inventory_level,
                promotion_flag,
                holiday_indicator
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(row["Order Date"]),
                str(row["Product ID"]),
                str(row["Product Name"]),
                str(row["Category"]),
                str(row["Region"]),
                int(row["Quantity Sold"]),
                float(row["Revenue"]),
                int(row["Inventory Level"]),
                int(row["Promotion Flag"]),
                int(row["Holiday Indicator"])
            )
        )

    conn.commit()

    conn.close()


def load_database_data():

    create_database()

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM sales_data",
        conn
    )

    conn.close()

    return df