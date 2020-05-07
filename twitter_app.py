import twitter
import sys
import threading

# use parent dir as relative root
sys.path.append("..")

# import config
from config import CONFIG

TWEET_ID = CONFIG["tweet_id"]

# frequency of checking retweets
FETCH_INTERVAL = 15.0

# auth app with twitter details
api = twitter.Api(
    consumer_key=CONFIG["consumer_key"],
    consumer_secret=CONFIG["consumer_secret"],
    access_token_key=CONFIG["access_token_key"],
    access_token_secret=CONFIG["access_token_secret"],
)

# recursive (multi threaded, really) function for adding new retweets
def get_rts():
    # in FETCH_INTERVAL time, call this function again
    threading.Timer(FETCH_INTERVAL, get_rts).start()

    # get retweets of the giveaway tweet
    retweets = api.GetRetweets(TWEET_ID, count=100)

    # open current entries file in r mode, starting at beginning
    file = open(f"../entries_{TWEET_ID}.txt", "r+")

    # convert file into list of ids
    done_ids = [i.split(",")[2] for i in file]

    # close file
    file.close()

    # open in append mode, starting the end of the file
    file = open(f"../entries_{TWEET_ID}.txt", "a+")

    # for all of the last 100 retweets
    for st in retweets:
        # get id of retweeter
        idx = st.user.id

        # if their id is already stored, skip to the next retweeter
        if str(idx) in done_ids:
            continue

        # extract user info
        usr = st.user.name
        name = st.user.screen_name

        # add the new retweet entry to the list
        file.write(f"{usr},{name},{idx},\n")

    # close file
    file.close()


# ensure the file exists when running new giveaway for the first time
file_chk = open(f"../entries_{TWEET_ID}.txt", "a+")
file_chk.close()

# start loop
get_rts()
