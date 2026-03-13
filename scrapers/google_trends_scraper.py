from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq()

trending = pytrends.daily_trending_searches(pn='US')

df = pd.DataFrame(trending)

print(df.to_string())
