from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Orange:
    driver = webdriver.Firefox()
    def fill_form(self,url):
        # Get the Data
        username = "Admin"
        password = "admin123"
        
        
        # Get the XPATH / ID / Class
        username_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        password_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        login_button_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        
        try:
            # open the webpage
            self.driver.get(url)
            time.sleep(3)

            #find the XPATH of the HTML element present on the webpage
            username_xpath=self.driver.find_element(by=By.XPATH, value=username_xpath)
            password_xpath=self.driver.find_element(by=By.XPATH, value=password_xpath)
            login_button_xpath=self.driver.find_element(by=By.XPATH, value=login_button_xpath)


            # fill the HTML form
            username_xpath.send_keys(username)
            password_xpath.send_keys(password)
            time.sleep(3)

            # click on the Submit button
            login_button_xpath.click()
            time.sleep(5)
        except: 
            print (" Error : XPATH not foun ! ")
            

O = Orange()
url = 'https://opensource-demo.orangehrmlive.com/'

O.fill_form(url)

