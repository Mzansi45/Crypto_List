# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import json

# Define a class for scraping data from CoinMarketCap
class CoinMarketCapScraper:
    def __init__(self):
        self.base_url = 'https://coinmarketcap.com/coins/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def scrape_coin_data(self, page=1):
        # Construct the URL for the specific page
        url = f'{self.base_url}?page={page}'
        
        # Send a GET request to the URL with headers
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            # Parse the HTML response using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the table containing the coin data
            table = soup.find('table', class_='sc-14cb040a-3')
            
            if not table:
                print("Table not found.")
                return None
            
            # Extract the headers from the table
            headers = [header.text.strip() for header in table.find_all('th')]
            
            coins_data = []
            for row in table.find_all('tr'):
                cells = row.find_all('td')
                
                if len(cells) == len(headers):
                    coin_data = {}
                    for header, cell in zip(headers, cells):
                        # Check if the header is for 1h %, 24h %, or 7d %
                        if header in ['1h %', '24h %', '7d %']:
                            # Check if the class "icon-Caret-up" is present
                            if cell.find(class_='icon-Caret-up'):
                                coin_data[header] = f"{cell.text.strip()} (Up)"
                            # Check if the class "icon-Caret-down" is present
                            elif cell.find(class_='icon-Caret-down'):
                                coin_data[header] = f"{cell.text.strip()} (Down)"
                            else:
                                coin_data[header] = cell.text.strip()
                        else:
                            coin_data[header] = cell.text.strip()
                    
                    coins_data.append(coin_data)
            
            return coins_data
        else:
            print(f"Failed to retrieve data from page {page}.")
            return None

    def save_to_json(self, data):
        # Save the data to a JSON file
        with open('coinmarketcap_coins.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print("Data saved to coinmarketcap_coins.json")

    def run(self, start_page=1, end_page=11):
        all_coins_data = []
        for page in range(start_page, end_page+1):
            # Scrape data for each page and append to the list
            coin_data = self.scrape_coin_data(page)
            if coin_data:
                all_coins_data.extend(coin_data)
        
        if all_coins_data:
            # Save all the scraped data to a JSON file
            self.save_to_json(all_coins_data)

# Entry point of the script
if __name__ == "__main__":
    # Create an instance of the CoinMarketCapScraper class
    scraper = CoinMarketCapScraper()
    
    # Run the scraper to scrape data from pages 1 to 11
    scraper.run(start_page=1, end_page=11)
