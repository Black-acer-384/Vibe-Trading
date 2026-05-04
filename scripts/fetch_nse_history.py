import pandas as pd
import os
from agent.src.data.nse_kenya import get_nse_history

# List of Nairobi Securities Exchange tickers you want to track
TICKERS = ["SCOM", "EQTY", "KCB", "BATK", "SAFBOND", "EABL"]

# Create the data folder if it doesn't exist
os.makedirs("agent/data/nse", exist_ok=True)

for ticker in TICKERS:
    print(f"Fetching data for {ticker}...")
    # This calls the function you built in the previous steps
    data = get_nse_history(ticker, days=365)
    df = pd.DataFrame(data)
    
    # Saves the data to a CSV file for the backtest engine
    df.to_csv(f"agent/data/nse/{ticker}.csv", index=False)
    print(f"Saved {ticker}.csv")