from loader import SlackDataLoader

print("mondays assignment work")
print("-----------------------------")

slack_data = SlackDataLoader('./data/anonymized')

users = slack_data.get_users()
channels = slack_data.get_channels()

print(channels)
