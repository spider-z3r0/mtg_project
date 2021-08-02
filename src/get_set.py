import requests as rq
import pandas as pd
import json as js

from requests.api import get


# def get_set():
#     url = "https://api.scryfall.com/cards/search?q=set:ktk"
#     s = rq.Session()
#     response = s.post(url)
#     orderList = []
#     resp_json = response.json()
#     orderList.append(resp_json["data"])
#     while resp_json.get('has_more') == True:
#         response = s.get(resp_json['next_page'])
#         resp_json = response.json()
#         orderList.append(resp_json["data"])
#     return orderList

# ktk = get_set()

def get_set(url):
    s = rq.Session()
    response = s.get(str(url))
    orderList = []
    resp_json = response.json()
    orderList.append(resp_json["data"])
    while resp_json.get('has_more'):
        response = s.get(resp_json['next_page'])
        resp_json = response.json()
        orderList.append(resp_json["data"])
        return orderList

a = get_set("https://api.scryfall.com/cards/search?q=set:ktk")

b = a[0]+a[1]




df=pd.DataFrame(b)
sels = ["name", "type_line", "mana_cost", "cmc", "oracle_text", "power", "toughness", "keywords", "loyalty", "rarity"]
df = df[sels]
df[['Super Type','Sub type']] = df['type_line'].apply(lambda x: pd.Series(str(x).split("—")))
df = df.drop(['type_line'], axis=1)
df.columns = df.columns.str.replace('_', ' ')
df.columns = df.columns.str.capitalize()

def movecol(df, cols_to_move=[], ref_col='', place='After'):
    
    cols = df.columns.tolist()
    if place == 'After':
        seg1 = cols[:list(cols).index(ref_col) + 1]
        seg2 = cols_to_move
    if place == 'Before':
        seg1 = cols[:list(cols).index(ref_col)]
        seg2 = cols_to_move + [ref_col]
    
    seg1 = [i for i in seg1 if i not in seg2]
    seg3 = [i for i in cols if i not in seg1 + seg2]
    
    return(df[seg1 + seg2 + seg3])


df = movecol(df, 
            cols_to_move=['Super type','Sub type'], 
            ref_col='Name',
            place='After')

df.to_csv('data\\ktk.csv')
print(df.head())
print(len(df))
