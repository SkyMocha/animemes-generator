from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

api = PushshiftAPI()

start_epoch=int(dt.datetime(2019, 1, 1).timestamp())

gen = api.search_submissions(after=start_epoch,
                            subreddit='animemes',
                            filter=['title'],
                            score = ">500",
                            limit=15000)

df = pd.DataFrame([thing.d_ for thing in gen])

df = df[["title"]]

df.to_csv ('./animemes.csv', index=False, header=False)

print (df)