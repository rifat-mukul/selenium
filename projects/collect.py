from bs4 import BeautifulSoup
import os
import pandas as pd


data = {"title":[], "price":[], "link":[]}


for file in os.listdir("data-html"):

    with open(f"data-html/{file}") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    t = soup.find("h2")
    title = t.get_text()

    p = soup.select_one(".a-price .a-offscreen")
    price = p.get_text(strip=True) if p else "N/A"

    l = soup.find("a", href=True)
    link = l["href"] if l else "N/A"

    # print(title)
    # print(price)
    # print(link)
    # print("================")
    data["title"].append(title)
    data["price"].append(price)
    data["link"].append(link)


df = pd.DataFrame(data)

# print(df)

df.to_csv("laptop_price.csv", index=False)
print("data write on csv file")


    # print(soup.prettify())