import requests
import pandas as pd
ids = [ "659ce2045214fb3d43ec574a",
    "659cfaed5214fb3d43ec5c36",
    "65587fe06d8f3e14bef887e1",
    "65587fff6d8f3e14bef887e2",
    "659cf1105214fb3d43ec5aa9",
    "6311b39a1458f15168b7b09f",
    "639078a117527429064c9e0e",
    "6311b3e81458f15168b7b0a2",
    "659542b15ac5ad2f1086e648",
    "655889526d8f3e14bef8891c"
]
url = "https://api.vegease.in/egreen/api/v1/near-store/products-new"
headers = {"accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "api_key": "123456",
    "origin": "https://vegease.in",
    "platform": "3",
    "priority": "u=1, i",
    "referer": "https://vegease.in/",
    "sec-ch-ua-mobile": "?1",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "timezone": "480",
    "authorization": "Basic ZWdyZWVuOmVncmVlbkAxMjM=",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"}
ans = {"SKU" : [] , "id" : [] , "Uom" : [], "Max price" : [], "Discounted price" : []}
for id in ids:
   querystring = {"categoryId":id}
   response = requests.request("GET", url, headers=headers, params=querystring)
   data = response.json()
   for i in data['data']['productData']:
            ans['SKU'].append(i['productName'])
            ans['id'].append(i['productId'])
            ans['Uom'].append(str(i['packagingSize'][0]['packSize']) + ' ' + i['packagingSize'][0]['unit'] )
            if(i['packagingSize'][0]['unit'] == "Gm"):
                  ans['Max price'].append(i['price']/(1000/i['packagingSize'][0]['packSize']))
                  ans['Discounted price'].append(i['offerPrice']/(1000/i['packagingSize'][0]['packSize']))
            else:           
              ans['Max price'].append(i['price'])
              ans['Discounted price'].append(i['offerPrice'])
            
temp = pd.DataFrame(ans)
scrap = temp.drop_duplicates(subset=['id', 'SKU'])
scrap.to_csv("vegease_scrap.csv" , header=True , index=False) 

