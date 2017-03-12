import pandas as pd
from pandas import DataFrame,Series


#data = pd.read_csv('D:\Programs\Python\Data\pydata-book-master\ch06\ex5.csv')

#data.to_csv('D:\Programs\Python\Data\pydata-book-master\ch06\out.csv')
'''
import requests
import json
url = 'https://www.baidu.com/s?wd=pandas%20python'
resp = requests.get(url)
data = json.loads(resp.text)
'''

import re
text = "foo  bar\t baz  \tqux"
sp = re.split('\s+',text)

print sp