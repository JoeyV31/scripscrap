from instabot import Bot
import time
from random import randint

bot = Bot()

# Login to Instagram
bot.login(username="testfol", password="password123")

# Get the user ID of the account you want to copy followers from
user_to_copy = "username_to_copy"  # The username of the account you want to copy followers from
user_id = bot.get_user_id_from_username(user_to_copy)

# Get the list of followers
followers = bot.get_user_followers(user_id)

# Follow each follower
for follower in followers:
    bot.follow(follower)


for follower in followers:
    bot.follow(follower)
    time.sleep(randint(30, 60))  # Wait between 30 to 60 seconds before following the next account

