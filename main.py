from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_search_parameters():
    while True:
        try:
            bedrooms = int(input("How many bedrooms are you looking for? (Enter a number: 1, 2, 3, 4, etc.): "))
            max_price = int(input("What is the maximum price you are willing to pay? (Enter a number): "))
            if bedrooms > 0 and max_price > 0:
                return f"{bedrooms}-bedrooms-under-{max_price}"
            else:
                print("Please enter valid numbers for bedrooms and max price (both greater than 0).")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def run_apartments_scraper():
    try:
        # Get user's bedroom preference and max price
        search_parameters = get_search_parameters()

        # setup WebDriver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = f'https://www.apartments.com/houses/san-luis-obispo-ca/{search_parameters}'

        # navigate to Apartments.com
        driver.get(url)

        # Wait for presence of XPath expression
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/section/div[1]/section[2]/div[2]')))

        # get the HTML source code of the loaded web page
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')

        # Extract data using Beautiful Soup:
        # get div elements with the class 'placardContainer'
        parent = soup.find('div', 'placardContainer').find('ul')
        # get all list elements with class "mortar-wrapper"
        listings = parent.find_all('li', "mortar-wrapper")

        print(str(len(listings)) + " houses found.")
        for i in listings:
            link = i.find("article")
            print(link.get('data-url'))
    finally:
        # Close the browser window when done
        driver.quit()

if __name__ == "__main__":
    run_apartments_scraper()