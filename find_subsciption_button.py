import csv
import time
#pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


with open('your_csv_file.csv','r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    service = Service(executable_path=r"path_to_your_chromedriver")  #make sure your chrome version is same as your driver version
    options = webdriver.ChromeOptions()
    #Please login your chrome account before run this code
    options.add_argument(r"user-data-dir=C:\Users\Your_user_name\AppData\Local\Google\Chrome\User Data") #here need to change to your one
    driver = webdriver.Chrome(service=service, options=options)

    for line in csv_reader:
        url=line[1]  #based on the row on your csv file
        print(url)
        driver.get(url)  #open the url

        time.sleep(3)    #in seconds
        """If the action you want to do have ads, maybe u can longer the time sleep to 30seconds"""
        
        xpath = '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-flexible-actions-view-model/div/yt-subscribe-button-view-model/yt-animated-action/div[1]/div[2]/button/yt-touch-feedback-shape/div/div[2]'
        #you can copy any xpath for your usage
        subscribe = driver.find_element("xpath",xpath)
        
        #find "subscribe" button
        subscribe.click()

        time.sleep(3)    #in seconds
