from loader import SlackDataLoader
from utils import slack_parser
from utils import get_top_20_user
from utils import draw_avg_reply_count
import pandas as pd

print("mondays assignment work")
print("-----------------------------")

slack_data = SlackDataLoader('./data/anonymized')

users = slack_data.get_users()
channels = slack_data.get_channels()

data_week8 = slack_parser('./data/anonymized/all-week8/')
data_week9 = slack_parser('./data/anonymized/all-week9/')

data = pd.concat([data-week8, data_week9])

get_top_20_user(data)
draw_avg_reply_count(data)