from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


driver = webdriver.Chrome()  
query = "laptop"
file = 0
for i in range(1,5):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=34VDZH1H46UCQ&sprefix=laptop%2Caps%2C593&ref=nb_sb_noss_2")


    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        data = elem.get_attribute("outerHTML")
        with open(f"data-html/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(data)
            file+=1
    time.sleep(random.randint(2,6))
driver.close()