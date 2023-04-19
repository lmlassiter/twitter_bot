# my_twitter_bots/bots/config.py


import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    # Passing info to Tweepy
    auth = tweepy.OAuthHandler("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    auth.set_access_token("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Verify Connection
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Could not create API", exc_info=True)
        raise e
    logger.info("API successfully created")
    return api
