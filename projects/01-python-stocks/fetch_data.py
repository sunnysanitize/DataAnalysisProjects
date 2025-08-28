import yfinance as yf
import sys
import pathlib

# Allow ticker from command-line, default = TSLA
ticker = sys.argv[1] if len(sys.argv) > 1 else "TSLA"

# Save into data/ folder
outdir = pathlib.Path(__file__).parent / "data"
outdir.mkdir(exist_ok=True)

# Download 6 months of daily prices
df = yf.download(ticker, period="6mo")
csv_path = outdir / f"{ticker.lower()}.csv"
df.to_csv(csv_path)

print(f"✅ Saved {ticker} data to {csv_path}")
