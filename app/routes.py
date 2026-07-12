from flask import Blueprint, render_template, request, redirect, url_for, session, Response
import pandas as pd
from app.services import process_dataframe, calculate_kpis, run_ml_forecasting

main_bp = Blueprint('main', __name__)

data_df = None

@main_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username") == "admin" and request.form.get("password") == "admin123":
            session["user"] = "admin"
            return redirect(url_for("main.dashboard"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@main_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    global data_df

    if "user" not in session:
        return redirect(url_for("main.login"))

    # File Upload Handling
    if request.method == "POST" and request.files.get("file"):
        file = request.files["file"]
        try:
            raw_df = pd.read_csv(file, encoding="latin1")
            required = ["Product", "Region", "Sales", "Revenue", "Profit", "Date"]
            
            for col in required:
                if col not in raw_df.columns:
                    return render_template("dashboard.html", error=f"Missing column: {col}", chart_data=None)

            data_df = process_dataframe(raw_df)
        except Exception as e:
            return render_template("dashboard.html", error=str(e), chart_data=None)

    if data_df is None:
        return render_template("dashboard.html", chart_data=None)

    # Filter Application
    df = data_df.copy()
    region = request.form.get("region")
    product = request.form.get("product")

    if region:
        df = df[df["Region"] == region]
    if product:
        df = df[df["Product"] == product]

    if df.empty:
        return render_template("dashboard.html", error="No data found for selected filters.", chart_data=None)

    # Analytics & ML
    kpis = calculate_kpis(df)
    ml_prediction, ml_accuracy = run_ml_forecasting(df)

    # Chart Generation
    product_sales = df.groupby("Product")["Sales"].sum()
    region_revenue = df.groupby("Region")["Revenue"].sum()
    profit_trend = df.groupby("Date")["Profit"].sum().sort_index()

    chart_data = {
        "products": product_sales.index.tolist(),
        "product_sales": product_sales.values.tolist(),
        "regions": region_revenue.index.tolist(),
        "region_revenue": region_revenue.values.tolist(),
        "dates": profit_trend.index.astype(str).tolist(),
        "profit_trend": profit_trend.values.tolist()
    }

    return render_template(
        "dashboard.html",
        total_revenue=kpis["total_revenue"],
        total_sales=kpis["total_sales"],
        total_profit=kpis["total_profit"],
        profit_margin=kpis["profit_margin"],
        insight=kpis["insight"],
        ml_prediction=ml_prediction,
        ml_accuracy=ml_accuracy,
        chart_data=chart_data
    )

@main_bp.route("/download")
def download():
    global data_df
    if data_df is None:
        return "No data"
    return Response(
        data_df.to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=report.csv"}
    )

@main_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))