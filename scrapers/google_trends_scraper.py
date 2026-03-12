from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)

trending_searches = pytrends.trending_searches(pn='united_states')

df = pd.DataFrame(trending_searches)

print(df.to_string())
