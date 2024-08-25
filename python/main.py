import figma_api
import website_scrapper
import comparison
from os import getenv

def main():
  figma_token = getenv("FIGMA_TOKEN")
  figma_file_id = getenv("FIGMA_FILE_ID")
  website_url = "http://127.0.0.1:5500/website/index.html"

  # Fetch Figma data
  figma_data = figma_api.fetch_figma_data(figma_token, figma_file_id)

  # Extract button data from Figma
  figma_button_data = figma_data["document"]["children"][0]["children"][0]

  # Scrape website button
  website_button = website_scrapper.scrape_website_button(website_url)

  # Compare buttons and highlight discrepancies
  comparison.compare_buttons(figma_button_data, website_button)

if __name__ == "__main__":
  main()
