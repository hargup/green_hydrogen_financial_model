# Green Hydrogen Profitability Calculator

Analyzes the green energy prices data to calculate how much profit you can expect to make if you produce green hydrogen when the prices are low.
Two parts to the repo:

## Extracting Electricity Prices Data

- [Indian Energy Exchange](https://www.iexindia.com/) has Green Day Ahead Market data which gives the electricity prices in per 15 minute window. We downloaded the PDF data for Jan-Dec 2023 add to the `./data` folder.
- Then all the PDFs are converted to text using [Apache Tika](https://www.apache.org/dyn/closer.lua/tika/2.9.1/tika-app-2.9.1.jar) and appended into one large text file at `./all_text_data.txt`
- Then we have a script at `txt_to_data.py` which converts the text data into json to used for profitability calculator. The data has the format:
```{"<date>: <list of price data per 15 minute window, example ["00:00", "00:15", "4617"], where 00:00 is the start time, 00:15 is the end time and 4617 is the price for that duration in rupees per mega-watt-hour.}```

## Plugging the data into the profitability Calculator

- From the raw data, we can calculate `thresholds_data.json` using `./data_to_threshold_data.py`, which gives the number of hours of the electricity prices have been below a certain rate, and the average price for that duration.
- And then we plug the data into `profit_calculator.py` to get the potential profit per year and IRR and the capex
