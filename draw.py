import twitter
import sys
import threading
import random

# use parent dir as relative root
sys.path.append("..")

# import config
from config import CONFIG

TWEET_ID = CONFIG["tweet_id"]
HOST_ID = CONFIG["host_user_id"]

# auth app with twitter details
api = twitter.Api(
    consumer_key=CONFIG["consumer_key"],
    consumer_secret=CONFIG["consumer_secret"],
    access_token_key=CONFIG["access_token_key"],
    access_token_secret=CONFIG["access_token_secret"],
)

# get all followers ids of host account
followers = api.GetFollowerIDs(user_id=HOST_ID, stringify_ids=True)

# open list of entries
file = open(f"../entries_{TWEET_ID}.txt", "r+")

# filter out entries that dont follow the host
valid_ids = [i.split(",")[:2] for i in file if str(i.split(",")[2]) in followers]

# print results
print(f"\n\nTotal entries that followed and retweeted:\n\n{valid_ids}\n\n")

print(f"Total eligible entries: {len(valid_ids)}\n\n")

# use the choice function to randomly select an entry from the list
print(f"Winner: {random.choice(valid_ids)}\n\n")

print(f"Made with @droux_aq3d's retweet picker: https://github.com/artemscript/twitterBot\n\n")

print(f"tweet: https://twitter.com/{HOST_ID}/status/{TWEET_ID}\n\n")
