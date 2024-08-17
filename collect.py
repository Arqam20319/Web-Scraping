from bs4 import BeautifulSoup
import pandas as pd
import os

d = {'Name':[], 'Price':[], 'Sold':[]}

for file in os.listdir("data"):
    with open(f"data/{file}", 'r', encoding='utf-8') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    n = soup.find('h3')
    Name = n.get_text()
    
    price_div = soup.find('div', class_='multi--price-sale--U-S0jtj')
    Price = float(''.join(span.get_text() for span in price_div.find_all('span')).replace('$',''))
    
    Sold = soup.find('span', class_='multi--trade--Ktbl2jB')
    if Sold:
        span_text = Sold.get_text(strip=True)
    print("Extracted text:", span_text)
    #Sold = s.get_text()
    #print(Sold)
    
    d['Name'].append(Name)
    d['Price'].append(Price)
    d['Sold'].append(span_text)

df = pd.DataFrame(data=d)
df.to_csv('data.csv')