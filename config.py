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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BACh59sABTZv45bUPzTuzxIH2kE7hHyotEmOQa8ZywOJ-ON3t0N_b6YSjpQKKGb9nFw9-9TzzOnFQ9K9jGmU0XdvVTcLc4Rof7TXTIG3sxBSB286xYTo9gvdzFRM6i7Bv1BgnOJF-yRRIOU7NK_TyL9-4jp8ie5rWagok8d_ntc40xZ2YJVE4wWjEwuilMTTvkXju7VKg-Coj0XzGrmnJ2oqd0L5vwmmUBBtXG7cYR1mO18mBOAhcHei5aw68VpOIApg5pb-4SsWprhfE4s7mNAn6pHYBVg9g96r4XnsjrfiTrQ50pvbmXDb7FQe3_Vhb6WFj5TbJunzLw6zJTXnWOJgyBKxtgAAAAA_qos8AA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
