from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()

url = "https://www.tbsnews.net/economy/bazaar"

driver.get(url)

# time.sleep(random.randint(2,6))

last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(0,20):

    driver.execute_script("window.scroll(0, document.body.scrollHeight)")
    time.sleep(random.randint(2,6))

    new_height = driver.execute_script("return document.body.scrollHeight")

    # if new_height == last_height:
    #     break
    # last_height = new_height

headlines = driver.find_elements(By.CLASS_NAME, "card-title")

print(f"{len(headlines)} elements are found")


i = 1
for title in headlines:
    data = title.get_attribute("outerHTML")
    with open(f"headlines-html/title_{i}.html", "w", encoding="utf-8") as f:
        f.write(data)
        i+=1


driver.quit()