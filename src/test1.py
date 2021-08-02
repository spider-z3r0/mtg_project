import requests as rq
import pandas as pd
import json as js



r4 = rq.get("https://api.scryfall.com/cards/search?order=color&q=set%3Aktk&page?4")
if r4.status_code == 200:
    print('Gotit!')
    js4= r4.json()

    df = pd.DataFrame(js4['data'])
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
    print(len(df))



