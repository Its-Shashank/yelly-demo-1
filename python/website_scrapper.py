from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_website_button(website_url):
  driver = webdriver.Chrome()  # Replace with your preferred browser driver
  driver.get(website_url)

  button = driver.find_element(By.CSS_SELECTOR, "button")  # Replace with the appropriate CSS selector
  return button
