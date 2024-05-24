
import requests
import pandas as pd

url = "https://api.crofarm.com/otipy/products/v3"
ans = {"SKU" : [] , "id" : [] , "Uom" : [], "Max price" : [], "Discounted price" : []}

for x in range(1 , 3):
    for y in range(1,8):
        querystring = {"page":y,"cat_id":x,"sub_cat_id":"0","latitude":"28.4433481","longitude":"77.0560866"}
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data= response.json()
        for product in data['products']:
            ans['SKU'].append(product['prod_name'])
            ans['id'].append(product['prod_id'])
            ans['Uom'].append(product['in_kg'])
            ans['Max price'].append(product['max_price'])
            ans['Discounted price'].append(product['price'])

scrap = pd.DataFrame.from_dict(ans)
scrap.to_csv("otipy_scrap.csv" , header=True , index=False) 
