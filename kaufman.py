from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd

def scrape_kufman(filename):
    df = pd.read_csv(filename)

    # Find rows where 'PropStreet' and 'PropCity' columns are empty
    rows_to_scrape = df[(df['PropStreet'].isna()) & (df['PropCity'].isna())]

    # Start the Selenium webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://esearch.kaufman-cad.org/")

    all_data = []
    for index, row in rows_to_scrape.iterrows():
        name = row['Decedent'].split()[0]
        print(name)
        # Perform web scraping
        try:
            input = driver.find_element(by='xpath', value='//input[@name="keywords"]')
            input.clear()
            input.send_keys(name)

            btn = driver.find_element(by='xpath', value='//button[@value="Search"]')
            btn.click()
            time.sleep(4)

            Property_id = driver.find_elements(by=By.XPATH, value='//div//tbody//tr//td[@role="gridcell"][2]')
            Geo_id = driver.find_elements(by=By.XPATH, value='//div//tbody//tr//td[@role="gridcell"][4]')
            TYPES = driver.find_elements(by=By.XPATH, value='//div//tbody//tr//td[@role="gridcell"][6]')
            OWNER_NAME = driver.find_elements(by=By.XPATH, value='//div//tbody//tr//td[@role="gridcell"][7]')
            PROPERTY_ADDRESS = driver.find_elements(by=By.XPATH, value='//div//tbody//tr//td[@role="gridcell"][8]')
            APPRAISED = driver.find_elements(by=By.XPATH, value='//div//tbody//tr//td[@role="gridcell"][10]')

            prop_street = PROPERTY_ADDRESS[-1].text.split(',')[0].strip()
            prop_city = PROPERTY_ADDRESS[-1].text.split(',')[1].strip()

            all_data.append([Property_id[-1].text, Geo_id[-1].text, TYPES[-1].text, OWNER_NAME[-1].text, PROPERTY_ADDRESS[-1].text, APPRAISED[-1].text])

            # Update the values of 'PropStreet' and 'PropCity'
            df.loc[index, 'PropStreet'] = prop_street
            df.loc[index, 'PropCity'] = prop_city
        except:
            pass

    # Save the updated dataframe to the CSV file
    df.to_csv(filename, index=False)

    # Write the scraped data to a new CSV file
    with open('kufman.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(all_data)

    # Quit the webdriver
    driver.quit()

# Call the function with the filename as an argument
scrape_kufman('Decedents (1).csv')
