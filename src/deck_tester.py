'''Let's get some data to see if kev is an idiot'''

import requests as rq
import pandas as pd
import json as js
import time 

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



def get_cards():
    '''getting dataset of card from scry fall'''
    idents = {
    '': 'Colorless',
    'W':'White',
    'U':'Blue',
    'B': 'Black',
    'R': 'Red',
    'G':'Green',
    'B W':'Orzhov',
    'R W':'Boros',
    'G U':'Simic',
    'R U':'Izzet',
    'B G':'Golgari',
    'R U W':'Jeskai',
    'B R W':'Mardu',
    'B G W':'Abzan', 
    'B G U':'Sultai', 
    'G R U':'Temur'
    }
    s = rq.Session() #getting the bulk metadata
    response = s.get('https://api.scryfall.com/bulk-data')
    time.sleep(0.1)
    resp_json = response.json()
    download_json = [x for x in resp_json['data'] if x['type'] == "oracle_cards"][0]
    download_uri = download_json['download_uri']
    print(download_uri)
    data = s.get(download_uri).json()
    df=pd.DataFrame(data)
    # sels = ["name", "type_line", "colors", "mana_cost", "cmc", "oracle_text", "power", "toughness", "keywords", "loyalty", "rarity"]
    # df = df[sels]
    # df[['Super Type','Sub type']] = df['type_line'].apply(lambda x: pd.Series(str(x).split("—")))
    # df = df.drop(['type_line'], axis=1)
    # df.columns = df.columns.str.replace('_', ' ')
    # df.columns = df.columns.str.capitalize()
    # df = movecol(df, 
    #     cols_to_move=['Super type','Sub type'], 
    #     ref_col='Name',
    #     place='After')
    # df['Colors'] = df['Colors'].apply(lambda x: ' '.join(x))
    # df['Colors'] = df['Colors'].replace(idents)
    return(df)


