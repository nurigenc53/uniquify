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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BACh59sATJCsj4XxYecCnFesRSMXQ00LsecVXnhnW-dLFd77dzWJ8xGt-f9H2bRimrw03tD4zdyRfbARksC0vnK7W8whMfoPYsGZhtGI62X3mldPIoB6BQvgkIt5tjSQBgwuU4ubMpYVC9IxVqGjIK85qTcvzayH3E8FLCJfUbH_iIf8kGsarFHwKiraqMtq5E426N-5myQNvmWtYjlcjhB2ujon7lHtyQwDgBKAzOu6icd8TqrjZcqLF8zbYYzzRlH590fIAYvjJuml91XoxAhBL9MeHBxvT149yUuIG63SK8b1QtdyRAgF1nBVRuljCF2iFzHQ7Pkb1g9lzFgosXM01SDYnwAAAAA_qos8AA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
