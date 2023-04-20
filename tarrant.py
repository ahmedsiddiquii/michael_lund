from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import csv
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.tarrantappraisal.org/")
df = pd.read_csv('Probate_Sample.csv')
# x=df.Decedent
name=df.loc[df['Decedent'].str.split().str.len() == 2, 'last name'] = df['Decedent'].str.split().str[0]
print(name)
temp1=[]
temp2=[]
temp3=[]
all_data=[]
# name=['131 marcos']
address=df['PropZip'].str.split()[0]
print(address)
na=name+address

for i in na:
    input=driver.find_element(by='xpath',value= '//input[@name="name-addr-acctno"]').send_keys(i)

    btn=driver.find_element(by='xpath',value= '//button[@type="submit"]').click()
    time.sleep(2)

    try:
        account=driver.find_elements(by='xpath',value= '//div[@class="col-sm-12"]//tbody//td[1]')
        for i in account:
            a=i.text
            print(a)
            temp1.append(a)

        name=driver.find_elements(by='xpath',value= '//div[@class="col-sm-12"]//tbody//td[2]')
        for j in name:
            b=j.text
            print(b)
            temp2.append(b)

        street=driver.find_elements(by='xpath',value= '//div[@class="col-sm-12"]//tbody//td[3]')
        for k in street:
            c=k.text
            print(c)
            temp3.append(c)

        with open('tarrent.csv', 'a',newline="") as f:
            writer = csv.writer(f)
            writer.writerow([i,temp1[-1],temp2[-1],temp3[-1]])
        all_data.append([temp1[-1],temp2[-1],temp3[-1]])

    except:
        pass
    
