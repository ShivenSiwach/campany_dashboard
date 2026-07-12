import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def process_dataframe(df):
    """Clean and validate incoming sales data."""
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df.dropna()

def calculate_kpis(df):
    """Calculate core business metrics."""
    total_revenue = float(df["Revenue"].sum())
    total_sales = float(df["Sales"].sum())
    total_profit = float(df["Profit"].sum())

    profit_margin = 0 if total_revenue == 0 else round((total_profit / total_revenue) * 100, 2)

    product_group = df.groupby("Product")["Sales"].sum()
    region_group = df.groupby("Region")["Revenue"].sum()

    top_product = product_group.idxmax() if not product_group.empty else "N/A"
    top_region = region_group.idxmax() if not region_group.empty else "N/A"

    insight = "Good Profit Zone" if profit_margin > 20 else "Low Profit"
    insight += f". Best Region: {top_region}. Top Product: {top_product}"

    return {
        "total_revenue": total_revenue,
        "total_sales": total_sales,
        "total_profit": total_profit,
        "profit_margin": profit_margin,
        "insight": insight
    }

def run_ml_forecasting(df):
    """Run Linear Regression for 30-day revenue prediction."""
    try:
        df_ml = df.copy()
        df_ml["Date_num"] = df_ml["Date"].map(pd.Timestamp.toordinal)

        X = df_ml[["Date_num"]]
        y = df_ml["Revenue"]

        if len(df_ml) > 5:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

            model = LinearRegression()
            model.fit(X_train, y_train)

            pred = model.predict(X_test)
            ml_accuracy = round(mean_absolute_error(y_test, pred), 2)

            future = np.array([[X["Date_num"].max() + 30]])
            ml_prediction = round(model.predict(future)[0], 2)

            return ml_prediction, ml_accuracy
    except Exception:
        pass
    return "ML failed", "Not calculated"