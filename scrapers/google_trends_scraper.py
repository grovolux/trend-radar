from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq()

trending_searches = pytrends.trending_searches()

df = pd.DataFrame(trending_searches)

print(df)
