# my_twitter_bots/bots/config.py


import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    # Passing info to Tweepy
    auth = tweepy.OAuthHandler("lcD672yVkNra4cTVwinyc18qG", "ZEAn6FrsC2DUJFD5RgY1gMqXC3KmryfGOZgSfagOzqbAafayun")
    auth.set_access_token("1562535150969589762-VF6dOMr2b5Vm9BRKfNfp9xflvqqwg6", "ayAvJ6VIWT3oWXieKg1Ry2i7kC0uYZ6algM6XqgAoBgWE")
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Verify Connection
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Could not create API", exc_info=True)
        raise e
    logger.info("API successfully created")
    return api
