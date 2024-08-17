from bs4 import BeautifulSoup as bs
import pandas as pd
import os

d = {'Name': [], 'Price': []}

for file in os.listdir("data"):
    with open(f"data/{file}", 'r', encoding='utf-8') as f:
        html_doc = f.read()
    soup = bs(html_doc, 'html.parser')
    
    n = soup.find('h3')
    Name = n.get_text()
    
    price_div = soup.find('div', class_='multi--price-sale--U-S0jtj')
    Price = float(''.join(span.get_text() for span in price_div.find_all('span')).replace('$',''))

    d['Name'].append(Name)
    d['Price'].append(Price)

df = pd.DataFrame(data=d)
df.to_csv('data.csv')