# Unlimitled Retweet Picker for less than 5000 follower accs

By [@droux_aq3d](https://twitter.com/droux_aq3d)

## 1. Prerequisites

1. python3 + pip3
2. VPS, server, or computer that's on 24/7 (lol?)
3. Twitter dev account and a twitter app (all easy & free) [apply for access](https://developer.twitter.com/en/apply-for-access)

## 2. Setup

1. Create a `parent` directory to house this app. Name irrelevant.
2. Create a `config.py` file that contains a python `dict` called `CONFIG`, with keys `consumer_key`, `consumer_secret`, `access_token_key`, `access_token_secret`, `tweet_id`, `host_user_id`.
3. The tweet id is in the link of your giveaway tweet. (non yet I assume)
4. You can find your host user id [here](https://tweeterid.com/)
5. Your 4 app keys are in the tokens tab of your twitter app's page.
6. git clone or download and extract this repo inside your `parent` folder. You will now have `parent/twitterBot`.
7. cd to `parent/twitterBot` and `pip3 install -r requirements.txt`. If you want to use a virtual env go ahead. If you don't know what that is, don't wory.

## 3a. Running for the first time 
1. Post a test tweet and retweet it youself. 
2. Copy its id from the end of the tweet url/link.
3. Put the tweet id in the `config.py` file.
4. Inside `parent/twitterBot` run `python3 twitter_app.py`.
5. Check it generates an `entries_<tweet_id>.txt` file in the `parent` folder. After 30 seconds or less it should have your retweet entry in there.

## 3b. Running normally
1. Post a giveaway tweet
2. Copy its id from the end of the tweet url/link.
3. Put the tweet id in the `config.py` folder.
4. Inside the `parent/twitterBot` folder run `python3 twitter_app.py`.
5. Note: I strongly recommend you use a backend running tool. I personally use `pm2` and I run it with: `pm2 run twitter_app.py --interpreter=python3`.

## 4. Drawing a Winner
Inside the `parent/twitterBot` folder;
1. Stop the giveaway bot, if you wish. I use `pm2 stop twitter_app.py`. Really depends on how you run it.
2. Run: `python3 draw.py`
