import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



#Reading config.json file
with open("config.json","r") as config_file:
    config_data = json.load(config_file)

#Initialize the WebDriver
driver = webdriver.Chrome()

#Open a webpage
driver.get(config_data["Login_url"])

#find an element by its ID and interact with it
username = driver.find_element(By.NAME,"username")
username.send_keys(config_data["Username"])

password = driver.find_element(By.NAME,"password")
password.send_keys(config_data["Password"])

login_button = driver.find_element(By.XPATH,config_data["Login_button_xpath"])
login_button.click()

#create order
driver.get(config_data["Create_Order"])
time.sleep(0)

#township
try:
    driver.set_page_load_timeout(1)
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="vs1__combobox"]/div[1]/input'))
    )
    dropdown.send_keys(config_data["Township_name"])
    dropdown.send_keys(Keys.ENTER)
except TimeoutException:
    print("Getting township is reached out of its time")    

#latlong
latlong = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
latlong.send_keys("16.9987,98.8875")

#category
try:
    driver.set_page_load_timeout(1)
    category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="vs2__combobox"]/div[1]/input'))
    )
    category.send_keys(config_data["Category"])
    category.send_keys(Keys.ENTER)
except TimeoutException:
    print("Getting category is reached out of its time")       

#brandname
try:
    driver.set_page_load_timeout(1)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#vs3__combobox .vs__search"))
    )
    element.click()
    element.send_keys(config_data["Brand_name"])
    element.send_keys(Keys.ENTER)  
except TimeoutException:
    print("Getting brand name is reached out of its time")  

#Service_Plan
try:
    driver.set_page_load_timeout(1)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="vs5__combobox"]/div[1]/input'))
    )
    element.click()
    element.send_keys(config_data["Service_Plan"])
    element.send_keys(Keys.ENTER)  
except TimeoutException:
    print("Getting service plan is reached out of its time")     

#service_type    
try:
    driver.set_page_load_timeout(1)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[2]/div/div[7]/div/div[1]/input'))
    )
    element.click()
    element.send_keys(config_data["Service_Type"])
    element.send_keys(Keys.ENTER)  
except TimeoutException:
    print("Getting service type is reached out of its time")    

#Name
name = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[2]/div/div[9]/div/input')
name.send_keys(config_data["Name"])

#NRC
nrc = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[2]/div/div[10]/div/input')
nrc.send_keys(config_data["NRC"])

#Phone1 and Phone 2
phone1 = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[2]/div/div[11]/div/input')
phone1.send_keys(config_data["Phone1"])

phone2 = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[2]/div/div[12]/div/input')
phone2.send_keys(config_data["Phone2"])

#Address
address = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[2]/div/div[14]/div/input')
address.send_keys(config_data["Address"])

#Remark
remark = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div/form/div[1]/div/div/div[2]/div[2]/div/div[17]/div/textarea')
remark.send_keys(config_data["Remark"])

time.sleep(10)
driver.quit()




