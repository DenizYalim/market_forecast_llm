from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

# wsj blocks.
def scrape_wsj_headlines(): 
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # Maybe turn this into firefox

    driver.get("https://www.wsj.com/")
    time.sleep(5)  # let page load

    headline_element_XPATH = "//h3"
    headlines = driver.find_elements(By.XPATH, headline_element_XPATH)

    print(f"Headlines({len(headlines)}):\n")
    for h in headlines:
        print("-", h.text)

    driver.quit()

if __name__ == "__main__":
    scrape_wsj_headlines()
