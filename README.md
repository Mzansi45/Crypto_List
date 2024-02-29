# CoinMarketCap Scraper

CoinMarketCap Scraper is a Python script that scrapes cryptocurrency data from CoinMarketCap website and saves it to a JSON file.

## Installation

To use this script, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can install the required packages using pip:

```cmd
pip install requests beautifulsoup4
```

## Usage

To run the script, follow these steps:

* 1. Clone this repository to your local machine
  2. Navigate to the project directory
  3. Run the script with Python

* download the zipfile from the repository, unzip and navigate to folder that contains script

## JSON output

```json
    {
      [{
          "": "",
          "#": "1",
          "Name": "BitcoinBTC",
          "Price": "$62,247.48",
          "1h %": "0.44% (Down)",
          "24h %": "8.93% (Up)",
          "7d %": "20.83% (Up)",
          "Market Cap": "$1.22T$1,220,334,139,690",
          "Volume(24h)": "$91,409,931,2471,471,189 BTC",
          "Circulating Supply": "19,640,556 BTC",
          "Last 7 Days": ""
      }]
    }
```

### Explanation of the JSON data

- `#`: The position of the cryptocurrency in the list.
- `Name`: The name of the cryptocurrency.
- `Price`: The current price of the cryptocurrency.
- `1h %`: The percentage change in price over the last 1 hour, along with the direction of change (Up or Down).
- `24h %`: The percentage change in price over the last 24 hours, along with the direction of change (Up or Down).
- `7d %`: The percentage change in price over the last 7 days, along with the direction of change (Up or Down).
- `Market Cap`: The total market capitalization of the cryptocurrency.
- `Volume(24h)`: The trading volume of the cryptocurrency over the last 24 hours, denoted in both USD and BTC.
- `Circulating Supply`: The total circulating supply of the cryptocurrency.
- `Last 7 Days`: Any additional information or events related to the cryptocurrency over the last 7 days.

By default, the script will scrape data from the first page to the eleventh page of CoinMarketCap's cryptocurrency list and save it to a JSON file named `coinmarketcap_coins.json`.

You can also customize the number of pages to scrape by modifying the `start_page` and `end_page` parameters in the `run` method of the `CoinMarketCapScraper` class.

```python
if __name__ == "__main__":
    scraper = CoinMarketCapScraper()
    scraper.run(start_page=1, end_page=11)  # Scrapes data from page 1 to 11
```

##### This project is licensed under the MIT License - see the LICENSE file for details

This README.md file includes sections for installation, usage, contributing, and licensing, providing users with comprehensive information about the script. You can adjust the content and formatting as needed.
