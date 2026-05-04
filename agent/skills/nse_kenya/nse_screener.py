import pandas as pd
from src.data.nse_kenya import get_nse_prices

def run(sector=None, min_price=None, min_volume=None):
    df = get_nse_prices()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["volume"] = pd.to_numeric(df["volume"].str.replace(",",""), errors="coerce")

    if min_price:
        df = df[df["price"] >= float(min_price)]
    if min_volume:
        df = df[df["volume"] >= int(min_volume)]

    return df.to_dict(orient="records")