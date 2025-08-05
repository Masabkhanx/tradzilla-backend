from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import os
os.environ["PYTHONHTTPSVERIFY"] = "0"

app = FastAPI()

# Allow frontend to access the API
origins = ["*"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True,
    allow_methods=[""], allow_headers=[""]
)

# Your trading data
PAIRS = [
    "USD/BRL", "USD/DZD", "USD/NGN", "USD/EGP", "USD/PKR",
    "USD/INR", "USD/ARS", "USD/MXN", "EUR/USD", "USD/BDT",
    "USD/JPY", "EUR/SGD", "EUR/NZD"
]
TIMEFRAMES = ["5sec", "10sec", "30sec", "1min", "5min", "30min"]
STRATEGIES = ["EMA + RSI", "MACD + Fibonacci", "Support & Resistance", "Quantum Momentum"]

@app.get("/signals")
def get_signals():
    signals = []
    for pair in PAIRS:
        signal = {
            "pair": pair,
            "timeframe": random.choice(TIMEFRAMES),
            "signal": random.choice(["BUY", "SELL"]),
            "confidence": random.randint(85, 99),
            "strength": random.choice(["Weak", "Moderate", "Strong"]),
            "strategy": random.choice(STRATEGIES)
        }
        signals.append(signal)
    return {"status": "success", "data": signals}

