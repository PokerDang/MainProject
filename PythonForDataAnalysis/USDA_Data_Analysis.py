import json
import pandas as pd
from pandas import DataFrame,Series
db = json.load(open('D:/Programs/Python/Data/pydata-book-master/ch07/foods-2011-10-03.json'))

'''
nutrients = DataFrame(db[0]['nutrients'])
info_keys = ['description','group','id','manufacturer']
info = DataFrame(db,columns=info_keys)
'''

nutrients = []

for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
nutrients = pd.concat(nutrients,ignore_index=True)
