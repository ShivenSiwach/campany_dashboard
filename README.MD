# Company Analytics Dashboard with Flask, HTML & Machine Learning

An interactive Company Analytics Dashboard built using Flask, HTML, Pandas, Chart.js, and Scikit-learn that allows users to upload CSV business/sales data, analyze key performance indicators (KPIs), apply filters, visualize insights, and generate a simple machine learning-based revenue prediction.

This project demonstrates how data analysis, business intelligence, web development, and machine learning can be combined into a lightweight, production-ready dashboard for reporting and decision-making.

---

## 🚀 Project Overview

This dashboard is designed as a mini business intelligence application where users can:
- Log in securely
- Upload CSV datasets
- View dynamic KPI cards
- Filter data by region and product
- Analyze sales, revenue, and profit trends
- Generate visual insights with charts
- Predict future revenue using a Linear Regression model
- Download processed reports

**Ideal Portfolio Project For:**
- Data Analysts / Business Analysts
- Backend Python / Flask Developers
- Entry-Level Data Science / ML Engineers

---

## ✨ Core Features

### 🔐 Authentication
- Basic login system using Flask sessions.
- Session-based access control for dashboard pages.
- Secure logout functionality.

### 📁 Data Ingestion
- Upload business/sales data in CSV format.
- Strict file validation and error handling before processing.

### 📊 KPI Engine
Automatically calculates and displays:
- Total Revenue
- Total Sales
- Total Profit
- Profit Margin (%)

### 🎛️ Interactive Filtering
Filter data dynamically by:
- **Region**
- **Product**

### 📈 Visual Analytics
Interactive business charts powered by **Chart.js**:
- Product-wise Sales (Bar Chart)
- Region-wise Revenue (Pie Chart)
- Profit Trend Over Time (Line Chart)

### 🤖 Machine Learning Revenue Prediction
- Utilizes Scikit-learn's **Linear Regression** model.
- Predicts future 30-day revenue based on historical date trends.
- Computes Mean Absolute Error (MAE) for basic model evaluation.

### 💡 Business Insights & Exporting
- Algorithmic highlighting of best-performing regions and top-selling products.
- Automated profitability condition checks (Good vs. Low margin).
- Download processed or filtered data instantly as a CSV file.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Gunicorn
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Frontend:** HTML5, CSS3, Chart.js
- **Deployment:** Docker

---

## 🏗️ Enterprise Architecture (Application Factory)

This project utilizes the Flask Application Factory pattern to prevent circular imports and allow for scalable, modular development.

```text
company_dashboard_with_html_and_flask/
│── run.py                  # The entry point to launch the server
│── config.py               # Holds configuration and secret keys
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
│── Dockerfile              # Containerization instructions
│── Two_months_of_daily_data__preview_.csv
│
└── app/                    # The main application package
    ├── __init__.py         # Contains the create_app factory
    ├── routes.py           # Handles web URLs and routing
    ├── services.py         # Holds the ML forecasting & pandas logic
    ├── templates/          # HTML templates
    │   ├── login.html
    │   └── dashboard.html
    └── static/             # CSS/JS and image assets