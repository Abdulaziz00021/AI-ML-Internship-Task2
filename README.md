# 📈 Stock Price Prediction (Next-Day Close Forecasting)

 **Task Objective**

The objective of this project is to **predict the next day’s closing stock price** using historical data.
The goal is to build a simple machine learning model that learns from patterns in past stock prices (Open, High, Low, Volume) and forecasts the upcoming Close value.

---

**Dataset Used**

The dataset is downloaded using the **Yahoo Finance API (yfinance)** library.
It includes daily stock data such as:

* **Open Price**
* **High Price**
* **Low Price**
* **Close Price**
* **Volume**

Time Period Used:

* **2018 — 2024**

Example Stock:

* **Apple (AAPL)**
  (But the model can be used with any stock like TSLA, AMZN, GOOG, etc.)

---

##  **Models Applied**

This project uses **Random Forest Regressor**, a powerful ensemble machine learning model.

### Why Random Forest?

* Handles non-linear patterns
* Works well on financial data
* More accurate than simple Linear Regression
* Robust to noise and fluctuations

### Features Used for Prediction:

| Feature | Description              |
| ------- | ------------------------ |
| Open    | Price at market open     |
| High    | Highest price of the day |
| Low     | Lowest price of the day  |
| Volume  | Number of shares traded  |

Target Variable:

 **Next_Close** (next day’s closing price)

---

 **Key Results & Findings**

 Model Performance

* The model produced a reasonable **Mean Squared Error (MSE)**, showing it can detect price patterns.
* The **Actual vs Predicted Plot** shows that predictions closely follow the real closing prices, especially during stable market periods.

### Observations

* The model performs well for short-term forecasting (1-day ahead).
* Sudden market spikes, news events, and financial announcements still create prediction errors (normal for ML models).
* Adding more technical indicators (RSI, MACD, SMA) can further improve accuracy.
