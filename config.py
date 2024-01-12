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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BACh59sAlu2SC62_HfIvtW1sB7pKfXjR-pGHlYrvUpR5jsSsqlLGyt5pHsD_nSbsAq8G8Hc-0Y3EgM4nogbHn4F7Y8rHq64sa8BSrPcbc0ZLTjpRSaoVFnGT_wdBLWAMGqwZsXYbGT_PwAP4B1viay0vMU-NlbnB-brZoLc_4VtlLHeC6_2B7uF8hJ3RfjwTAHZxWYFYZ3qFi1X72dAF5nLVwYRkG-6ofDIDVVq90P9BxfFFoIZHH-Hw3ZEocFtbouzkqxPyikyMZ2rbH1q1pujdlrn76W25Ph8iHvkk3eBjdTdJ3eOqQrq4t8peufQVuVQ9E5ft9BtcVLl9mJdXK2ktZg9iHQAAAAA_qos8AA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
