from bs4 import BeautifulSoup
import os
import pandas as pd

data = {'title':[], 'link':[]}

for file in os.listdir('headlines-html'):

    with open(f"headlines-html/{file}") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    headlines = soup.find_all(['h2', 'h3'], class_="card-title")

    for tag in headlines:
        a = tag.find("a", href=True)

        data['title'].append(a.get_text())
        data['link'].append(f"https://www.tbsnews.net{a['href']}")

df = pd.DataFrame(data)

df.to_csv("headlines.csv", index=False)

print("data write to the csv file")
