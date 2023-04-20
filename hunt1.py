import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd



driver = webdriver.Chrome()
driver.get("https://esearch.hunt-cad.org/")
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
   
    driver.get("https://esearch.hunt-cad.org/")
    time.sleep(15) 
    search_input = driver.find_element(by='xpath', value='//input[@class="form-control"]')
    search_input.clear()
    search_input.send_keys(names)
    time.sleep(5)
    search_Button =  driver.find_element(by='xpath', value='//button[@class="btn btn-default"]').click()
    time.sleep(5)
    
    try:
        Property_id=  driver.find_elements(by=By.XPATH , value= '//div//tbody//tr//td[@role="gridcell"][2]')
        for prop in Property_id:
            a=prop.text
            temp1.append(a)
            
        Geo_id= driver.find_elements(by=By.XPATH , value= '//div//tbody//tr//td[@role="gridcell"][4]')
        for geo in Geo_id:
            b= geo.text
            temp2.append(b)
            
        TYPES= driver.find_elements(by=By.XPATH , value= '//div//tbody//tr//td[@role="gridcell"][6]')
        for typee in TYPES:
            typee.text
            temp3.append(c)
            
        OWNER_NAME= driver.find_elements(by=By.XPATH , value= '//div//tbody//tr//td[@role="gridcell"][7]')
        for ownername in OWNER_NAME:
            d=ownername.text
            temp4.append(d)
            
        PROPERTY_ADDRESS= driver.find_elements(by=By.XPATH , value= '//div//tbody//tr//td[@role="gridcell"][8]')
        for address in PROPERTY_ADDRESS:
            e = address.text
            temp5.append(e)
            
        APPRAISED= driver.find_elements(by=By.XPATH , value= '//div//tbody//tr//td[@role="gridcell"][10]')
        for app in APPRAISED:
            f = app.text
            temp6.append(f)

        
            
        with open('hunt-cad848.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i,temp1[-1],temp2[-1],temp3[-1],temp4[-1],temp5[-1],temp6[-1]])
        all_data.append([temp1[-1],temp2[-1],temp3[-1],temp4[-1],temp5[-1],temp6[-1]])
    except:
        pass