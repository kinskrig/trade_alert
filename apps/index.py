# Environment variables
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import sys
load_dotenv(Path("/local/.env"))
key = os.getenv("ALPHA_VAN_API")

# alpha vantage api
from alpha_vantage.timeseries import TimeSeries
app = TimeSeries(key)



appl = app.get_daily_adjusted('AAPL', outputsize='full')
print(appl)
