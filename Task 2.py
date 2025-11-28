import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

stock = "AAPL"   # Change to TESLA = "TSLA"
df = yf.download(stock, start="2018-01-01", end="2024-12-31")

df["Next_Close"] = df["Close"].shift(-1)
df = df.dropna()

X = df[["Open", "High", "Low", "Volume"]]
y = df["Next_Close"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

plt.figure(figsize=(12, 6))
plt.plot(y_test.values, label="Actual Close Price")
plt.plot(predictions, label="Predicted Close Price")
plt.title(f"Actual vs Predicted Closing Price for {stock}")
plt.xlabel("Time")
plt.ylabel("Close Price ($)")
plt.legend()
plt.show()
