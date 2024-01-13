#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5543398151:AAHw2shLPOTICVIKB7Qv9RsEBb0q_7NOXVQ")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "10610651"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "7b0c7355c1b140db1eafb476469e5402")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1068141372").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BACh59sANwu0SB3sCCuDNWr60n3hE0THVkAo0T-3ClX8pPlsgNQazllgy1ZeAWicPMf--5kwcBPAJWuTZdCRUiPOOjJPupEzU8cGKifV6DfhBDOAB3h20kN5HENIR5Fghltr2LHK-bAZsUDJlbxdj8EikLQjlWW_xO1vyhcKdf5IG9ZeySB978heLy5gdyVYIvcEwmWMhbcRtNffVAPGIscd59X9pTYbOovbHh7tCxCCMceiR9DebxgR36fJFCa2YPjaU1HtB577nlQ-OFhzK8g3o7o51MPYD5HAqahIshXMQg0vgbvJ6vWnzQgTYGjOMpJHoDgetHjVwmwjI84S7Q0OM4yY1wAAAAFKaYsHAQ")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
