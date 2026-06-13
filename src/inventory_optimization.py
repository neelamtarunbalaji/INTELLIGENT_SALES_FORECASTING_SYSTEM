import pandas as pd


def calculate_inventory_metrics(df):

    avg_daily_demand = (
        df["Quantity Sold"].mean()
    )

    demand_std = (
        df["Quantity Sold"].std()
    )

    lead_time = 7

    service_factor = 1.65

    safety_stock = (
        service_factor
        * demand_std
        * (lead_time ** 0.5)
    )

    reorder_point = (
        avg_daily_demand * lead_time
        + safety_stock
    )

    annual_demand = (
        df["Quantity Sold"].sum()
    )

    ordering_cost = 100

    holding_cost = 5

    eoq = (
        (
            2
            * annual_demand
            * ordering_cost
        )
        / holding_cost
    ) ** 0.5

    return {

        "Average Demand":
        round(avg_daily_demand, 2),

        "Safety Stock":
        round(safety_stock, 2),

        "Reorder Point":
        round(reorder_point, 2),

        "EOQ":
        round(eoq, 2)
    }


def stock_alerts(df, reorder_point):

    current_stock = (
        df["Inventory Level"].mean()
    )

    if current_stock < reorder_point:

        status = "Low Stock Alert"

    elif current_stock > reorder_point * 3:

        status = "Overstock Alert"

    else:

        status = "Stock Level Healthy"

    return current_stock, status