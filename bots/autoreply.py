# my_twitter_bot/bots/autoreply.py

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Getting Mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id  is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Replying to {tweet.user.name}")

            api.update_status(
                status="Don't talk to me, I am a bot",
                in_reply_to_status_id=tweet.id
            )
    return new_since_id



def main():
    api = create_api()
    since_id = 1
    while True:
            since_id = check_mentions(api, ["who","what"], since_id)
            logger.info("Waiting for mentions...")
            time.sleep(10)

if __name__ == "__main__":
    main()


