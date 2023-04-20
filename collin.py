import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd



driver = webdriver.Chrome()
driver.get("https://www.collincad.org/propertysearch")
time.sleep(15)
    
df = pd.read_csv('Probate_Sample.csv')
# x=df.Decedent
name=df.loc[df['Decedent'].str.split().str.len() == 2, 'last name'] = df['Decedent'].str.split().str[0]
print(name)
temp1=[]
temp2=[]
temp3=[]
temp4=[]
temp5=[]
temp6=[]
all_data=[]

    
for names in name:
    print(names)
    driver.get("https://www.collincad.org/propertysearch")
    search_input = driver.find_element(by='xpath', value='//input[@name="owner_name"]')
    search_input.clear()
    search_input.send_keys(names)
    search_button=driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()
    time.sleep(15)
   
    try:
            
        product_id=driver.find_elements(by='xpath', value='//tr[@class="proptype_r"]//td[2]')
        for i in product_id:
            a=i.text
            temp1.append(a)
        OWNER_NAME=driver.find_elements(by='xpath', value='//tr[@class="proptype_r"]//td[3]')
        for ownername in OWNER_NAME:
            d=ownername.text
            temp2.append(d)
        
        PROPERTY_ADDRESS=driver.find_elements(by='xpath', value='//tr[@class="proptype_r"]//td[4]')
        for address in PROPERTY_ADDRESS:
            e=address.text
            temp3.append(e)
        legal_description=driver.find_elements(by='xpath', value='//tr[@class="proptype_r"]//td[6]')
        for description in legal_description:
            b=description.text
            temp4.append(b)
            print(b)
        market_value=driver.find_elements(by='xpath', value='//tr[@class="proptype_r"]//td[7]')
        for market in  market_value:
            f=market.text
            temp5.append(f)
            print(market.text)
        with open('collin.csv', 'w', newline='', encoding='utf-8') as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow([i,temp1[-1],temp2[-1],temp3[-1],temp4[-1],temp5[-1]])
        all_data.append([temp1[-1],temp2[-1],temp3[-1],temp4[-1],temp5[-1]])
                
    except:
        pass
