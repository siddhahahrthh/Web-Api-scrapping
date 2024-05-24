import requests
import cloudscraper
import pandas as pd

ans = {"SKU" : [] , "UOM" : [] , "id" : [] , "product_id" : [], "Max price" : [], "Discounted price" : []}
cat = ["veggies" , "fruits"]
num = 1
for x in cat:
    url = f"https://pluckk.in/_next/data/358/{x}.json"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    data = response.json()

    data2 = data['pageProps']['allProductDetails']
    for product in data2:
        for y in product['skus']:
             ans['SKU'].append(product['name'])
             ans['UOM'].append(y['size'])
             ans['id'].append(y['id'])
             ans['product_id'].append(y['product_id'])
             ans['Max price'].append(y['warehouses'][0]['mrp'])
             ans['Discounted price'].append(y['warehouses'][0]['price']) 

scrap = pd.DataFrame(ans)
scrap.to_csv("pluckk.csv" , header=True , index=False)         