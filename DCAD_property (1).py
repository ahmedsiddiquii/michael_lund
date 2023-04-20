from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://dallascad.org/searchowner.aspx")


df = pd.read_csv('Probate_Sample.csv')
# x=df.Decedent
first_name=df.loc[df['Decedent'].str.split().str.len() == 2, 'last name'] = df['Decedent'].str.split().str[0]

temp1=[]
temp2=[]
temp3=[]
temp4=[]
temp5=[]
all_data=[]
# first_name=['michel','mark']
for i in first_name:

    name=i
    driver.get("https://dallascad.org/searchowner.aspx")
    res = driver.find_element(by='xpath',value= '//input[@name="txtOwnerName"]').send_keys(name)

    search = driver.find_element(by='xpath',value= '//input[@type="submit"]').click()

    time.sleep(5)
    
    city=driver.find_elements(by='xpath',value= '//div//p//tr//td[3]')
    for i in city:
        a=i.text
        print(a)
        temp1.append(a)

    owner_name=driver.find_elements(by='xpath',value= '//div//p//tr//td[4]')
    for j in owner_name:
        b=j.text
        print(b)
        temp2.append(b)

    totla_value=driver.find_elements(by='xpath',value= '//div//p//tr//td[5]')
    for k in totla_value:
        c=k.text
        print(c)
        temp3.append(c)

    type=driver.find_elements(by='xpath',value= '//div//p//tr//td[6]')
    for l in type:
        d=l.text
        print(d)
        temp4.append(d)

    address=driver.find_elements(by='xpath',value= '//div//p//tr//td//a[@id="Hyperlink1"]')
    for m in address:
        e=m.text
        print(e)
        temp5.append(e)
    with open('Dallascad.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([i,temp1[-1], temp2[-1], temp3[-1], temp4[-1], temp5[-1]])
    all_data.append([temp1[-1], temp2[-1], temp3[-1], temp4[-1], temp5[-1]])

# all_data.append([temp1,temp2,temp3,temp4,temp5])
# print(all_data)
# with open('DCAD.csv', 'w') as f:
#     writer = csv.writer(f)
#     for flile in all_data:
#     # write a row to the csv file
#         for fl in flile:
#             writer.writerows(fl)
    
