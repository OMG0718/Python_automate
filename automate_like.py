import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

with open('music-library-songs.csv','r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    service = Service(executable_path=r"path_to_your_chromedriver") 
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\Your_user_name\AppData\Local\Google\Chrome\User Data")
    driver = webdriver.Chrome(service=service, options=options)

    for line in csv_reader:
        url=line[0]  
        print(url)
        driver.get(url)   #open the url

        time.sleep(3) #in seconds
        xpath = '//*[@id="button-shape-like"]/button/yt-touch-feedback-shape/div/div[2]'
        like = driver.find_element("xpath",xpath)
        
        #find "like" button
        like.click()

        time.sleep(3)
    
    driver.quit()

