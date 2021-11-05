#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import os

#Input the keyword you want to download
print("Input search query: ")
query = input()
print("Input folder name: ")
folder_name = input()


#Opens up web driver and goes to Google Images
path = './Driver/'

#Make a directory to save your photos 
os.mkdir(f'{path}/{folder_name}')

driver = webdriver.Chrome(path + 'chromedriver')
driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

#Search on web driver
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys(query)
box.send_keys(Keys.ENTER)


#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1, 1000):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(f"{path}/{folder_name}/{i + 828}.png")
    except:
        pass