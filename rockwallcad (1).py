import csv
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://www.rockwallcad.com/property-search")
time.sleep(20)

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
temp7=[]
temp8=[]
temp9=[]
all_data=[]

for names in name:
    
    search_input =driver.find_element('xpath',"//input[@placeholder='Search by Account Number, Address or Owner Name']") 
    search_input.clear()
    search_input.send_keys(names)
    button=driver.find_element('xpath',"//button[@class='MuiButtonBase-root MuiIconButton-root jss4']").click()
    
    time.sleep(10)
    rows=driver.find_elements('xpath',"//div[@role='row']")  
    
    try:
      
        product_id=driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][5]')
        for i in product_id:
            a=i.text
            temp1.append(a)
            
        types=driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][6]')
        for typee in types:
            b=typee.text
            temp2.append(b)
            
        geo=driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][7]')
        for id in geo:
            c=id.text
            temp3.append(c)
            
        OWNER_NAME=driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][8]')
        for ownername in OWNER_NAME:
            d=ownername.text
            temp4.append(d)
            
        address =driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][9]')
        for add in address:
            e=add.text
            temp5.append(e)
            
        cities= driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][10]')
        for city in cities:
            f=city.text
            temp6.append(f)
            
        legaL= driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][10]')
        for description in legaL:
            g=description.text
            temp7.append(g)
            
        market = driver.find_elements(by=By.XPATH , value= '//div[@class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-value"][2]')
        for value in market:
            h=value.text
            temp8.append(h)
            
        APPRAISED= driver.find_elements(by=By.XPATH , value= '//div//tbody//tr//td[@role="gridcell"][3]')
        for app in APPRAISED:
            k=app.text
            temp9.append(k)
        
        with open('rockwallcad.csv', 'w', newline='', encoding='utf-8') as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow([i,temp1[-1],temp2[-1],temp3[-1],temp4[-1],temp5[-1],temp6[-1],temp7[-1],temp8[-1],temp9[-1]])
        all_data.append([temp1[-1],temp2[-1],temp3[-1],temp4[-1],temp5[-1],temp6[-1],temp7[-1],temp8[-1],temp9[-1]])

    except:
        pass


        
