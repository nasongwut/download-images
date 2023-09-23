
import json
import wget
import requests
import pandas as pd
url = "https://api.appsheet.com/api/v2/apps/b6b91898-0c90-4950-a376-d1406646c245/tables/made to order/Action"
headersAppsheet = {'Content-type': 'application/json',
                   'applicationAccessKey': 'V2-dQZZT-PI1pY-slgIk-mjVUr-Ktyg5-CU7VP-YqOqP-sVKST'}
payload = {
    "Action": "Find",
    "Properties": {
        "Locale": "en-US",
        "Location": "47.623098, -122.330184",
        "Timezone": "Pacific Standard Time",
        "UserSettings": {
            "Option 1": "value1",
            "Option 2": "value2"
        }
    },
    "Rows": [
    ]
}
print("Call Appsheet API")
callAPI = requests.post(url, data=json.dumps(payload), headers=headersAppsheet)

strRes = callAPI.text
res = json.loads(strRes)
data = {
    "รูปภาพ": [],
    "รหัสสินค้า": [],
    "ชื่องาน": [],
    "ชื่อบริษัท": [],
    "คิวอาร์โค๊ด": [],
}
for i in res:
    data['รหัสสินค้า'].append(i['รหัสสินค้า'])
    data['ชื่องาน'].append(i['ชื่องาน'])
    data['คิวอาร์โค๊ด'].append(i['คิวอาร์โค๊ด'])
    data['รูปภาพ'].append(i['imgUrl'])
    data['ชื่อบริษัท'].append(i['ชื่อบริษัท'])
    url = i['imgUrl']
    print("_____________________")
    print(url)
    lendata = len(url)
    lenurl = len
    if lendata > 123:
        print("Downloading ...")
        fileName = str(i['รหัสสินค้า'] + ".jpg")
        response = requests.get(url, timeout=10)
        print(response)
        # file = open(fileName, "wb")
        # file.write(response.content)
        # file.close()
# response = requests.get(url)
# fileName = str(i['รหัสสินค้า'] + ".jpg")
# filename = wget.download(url)


df = pd.DataFrame(data)
df.to_excel(r'./Cityart catalog.xlsx', index=False)
