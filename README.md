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
* 1. Clone this repository to your local machine:

  2. Navigate to the project directory:

  3. Run the script with Python:
   
* download the zipfile from the repository, unzip and navigate to folder that contains script

By default, the script will scrape data from the first page to the eleventh page of CoinMarketCap's cryptocurrency list and save it to a JSON file named `coinmarketcap_coins.json`.

You can also customize the number of pages to scrape by modifying the `start_page` and `end_page` parameters in the `run` method of the `CoinMarketCapScraper` class.

```python
if __name__ == "__main__":
    scraper = CoinMarketCapScraper()
    scraper.run(start_page=1, end_page=11)  # Scrapes data from page 1 to 11
```

##### This project is licensed under the MIT License - see the LICENSE file for details.

This README.md file includes sections for installation, usage, contributing, and licensing, providing users with comprehensive information about the script. You can adjust the content and formatting as needed.
