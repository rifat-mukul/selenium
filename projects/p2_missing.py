from bs4 import BeautifulSoup
import os

for file in os.listdir('headlines-html'):
    with open(f"headlines-html/{file}") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    h2_tag = soup.find("h2", class_="card-title")
    h3_tag = soup.find("h3", class_="card-title")

    if not h2_tag and not h3_tag:
        print(f"❌ No h2 or h3 card-title in {file}")
