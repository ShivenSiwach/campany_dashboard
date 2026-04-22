#  Company Analytics Dashboard with Flask, HTML & Machine Learning


An interactive **Company Analytics Dashboard** built using **Flask, HTML, Pandas, Chart.js, and Scikit-learn** that allows users to upload CSV business/sales data, analyze key performance indicators (KPIs), apply filters, visualize insights, and generate a simple **machine learning-based revenue prediction**.

This project demonstrates how **data analysis, business intelligence, web development, and machine learning** can be combined into a lightweight dashboard for reporting and decision-making.

---

#  Project Overview

This dashboard is designed as a **mini business intelligence application** where users can:

- Log in securely
- Upload CSV datasets
- View dynamic KPI cards
- Filter data by region and product
- Analyze sales, revenue, and profit trends
- Generate visual insights with charts
- Predict future revenue using a **Linear Regression model**
- Download processed reports

It is a strong **portfolio project** for:

- **Data Analyst**
- **Business Analyst**
- **Python Developer**
- **Flask Developer**
- **Entry-Level Data Science / ML roles**

---

# Features

## Authentication
- Basic login system using Flask sessions
- Session-based access control for dashboard pages
- Logout functionality included

## CSV Upload
- Upload business/sales data in CSV format
- File validation before dashboard processing

## KPI Dashboard
Automatically calculates and displays:

- **Total Revenue**
- **Total Sales**
- **Total Profit**
- **Profit Margin (%)**

## Interactive Filtering
Filter data dynamically by:

- **Region**
- **Product**

## Visual Analytics (Chart.js)
Includes interactive business charts such as:

- **Product-wise Sales**
- **Region-wise Revenue**
- **Profit Trend Over Time**

## Machine Learning Revenue Prediction
- Uses **Linear Regression**
- Predicts future revenue based on date trend
- Computes **Mean Absolute Error (MAE)** for basic model evaluation

## Export Reports
- Download processed or filtered data as a CSV file

## Business Insights
The dashboard can also highlight:

- Best-performing region
- Top-selling product
- Profitability condition (good vs low margin)

---

# Tech Stack

## Backend
- **Python**
- **Flask**

## Data Processing
- **Pandas**
- **NumPy**

## Machine Learning
- **Scikit-learn**
  - `LinearRegression`
  - `train_test_split`
  - `mean_absolute_error`

## Frontend
- **HTML**
- **Chart.js**

## Optional Improvements (Future)
- CSS / Bootstrap / Tailwind CSS
- SQLite / PostgreSQL
- Docker
- Deployment on Render / Railway / PythonAnywhere

---

# Recommended Professional Project Structure

> **Important:** For a professional Flask project, HTML files should be placed inside a `templates/` folder.

```bash
company_dashboard_with_html_and_flask/
│── app.py
│── requirements.txt
│── README.md
│── Two_months_of_daily_data__preview_.csv
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── static/                 # (Optional - recommended for CSS/JS/images)
│   ├── css/
│   ├── js/
│   └── images/
│
└── uploads/                # (Optional - for uploaded CSV files)
