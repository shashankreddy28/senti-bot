# currently unused
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_twitter(message):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("X_API_KEY"),
        os.getenv("X_API_SECRET"),
        os.getenv("X_ACCESS_TOKEN"),
        os.getenv("X_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    api.send_direct_message(
        os.getenv("X_RECIEVER_USER_ID"),  # Replace with your user ID
        message
    )

    api.update_status(message)
