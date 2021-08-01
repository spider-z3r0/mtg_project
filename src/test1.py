import requests as rq
import pandas as pd
import json as js




# r1 = rq.get("https://api.scryfall.com/bulk-data")
# js1 = r1.json()
# print(type(js1))
# for i in range(len(js1['data'])):
#     a = js1['data'][i]['name']
#     print(f'{i}. Name: {a}')


# r2 = rq.get("https://api.scryfall.com/cards/named?fuzzy=narset+parter+of_veils")
# js2 = r2.json()
# # print(type(js2))
# # print(js2)

# # for i in range(len(js2)):
# #     for k,v in js2.items():
# #         print(f'{1}.{k} : {v}\n')

# vs = ["name", "set_name", "mana_cost", "type_line","oracle_text",]

# for i in vs:
#     print(f'{i}: {js2[i]}')


r3 = rq.get("https://api.scryfall.com/cards/search?q=narset")
js3 = r3.json()
# print(type(js2))
print(js3)

# for i in range(len(js2)):
#     for k,v in js2.items():
#         print(f'{1}.{k} : {v}\n')

# vs = ["name", "set_name", "mana_cost", "type_line","oracle_text",]

# for i in vs:
#     print(f'{i}: {js2[i]}')