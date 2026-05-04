import requests
from bs4 import BeautifulSoup
import pandas as pd

NSE_URL = "https://afx.kwayisi.org/nse/"

def get_nse_prices() -> pd.DataFrame:
    """Scrape live NSE price list from afx.kwayisi.org"""
    resp = requests.get(NSE_URL, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table")
    rows = []
    for tr in table.find_all("tr")[1:]:
        cols = [td.text.strip() for td in tr.find_all("td")]
        if cols:
            rows.append(cols)
    df = pd.DataFrame(rows, columns=["ticker", "name", "price", "change", "volume"])
    return df

def get_nse_ticker(symbol: str) -> dict:
    """Get data for a single NSE ticker e.g. 'SCOM' for Safaricom"""
    df = get_nse_prices()
    row = df[df["ticker"].str.upper() == symbol.upper()]
    if row.empty:
        return {"error": f"{symbol} not found on NSE"}
    return row.iloc[0].to_dict()