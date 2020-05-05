import twitter
import sys
import threading

sys.path.append("..")

from config import CONFIG

TWEET_ID = CONFIG["tweet_id"]
FETCH_INTERVAL = 15.0  # basically the minimum limit for user auth api requests

api = twitter.Api(
    consumer_key=CONFIG["consumer_key"],
    consumer_secret=CONFIG["consumer_secret"],
    access_token_key=CONFIG["access_token_key"],
    access_token_secret=CONFIG["access_token_secret"],
)


def get_rts():
    threading.Timer(FETCH_INTERVAL, get_rts).start()
    retweets = api.GetRetweets(TWEET_ID, count=100)

    file = open(f"../entries_{TWEET_ID}.txt", "r+")
    done_ids = [i.split(",")[2] for i in file]
    print(done_ids)
    file.close()

    file = open(f"../entries_{TWEET_ID}.txt", "a+")
    for st in retweets:
        idx = st.user.id
        if str(idx) in done_ids:
            continue

        usr = st.user.name
        name = st.user.screen_name
        file.write(f"{usr},{name},{idx},\n")

    file.close()


file_chk = open(f"../entries_{TWEET_ID}.txt", "a+")
file_chk.close()

get_rts()
