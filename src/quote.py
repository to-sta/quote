import json
import requests as rq
from requests import HTTPError
from requests.adapters import HTTPAdapter

with open("config.json", "r") as config:
    cred = json.load(config)

TOKEN = cred["token"]
CHAT_ID = cred["chat_id"]


def send_telegram_msg(msg: str, token: str = TOKEN, chat_id: str = CHAT_ID) -> None:
    """send_telegram_msg

    Sends a telegram message via bot

    Parameters
    ----------
    msg: str
        message to be sent via telegram bot
    token: str
        telegram bot token
    chat_id: str
        telgram bot chat_id

    """
    url = (
        f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    )
    rq.get(url)


def random_quote() -> None:
    """random_qoute
    ------------

    Retrieves a random quote from the https://api.quotable.io and sends it via telegram.
    Link to the github page about the API https://github.com/lukePeavey/quotable#get-random-quote

    Parameters
    ----------
    token: str
        Telegram bot token

    chat_id: str
        Chat  ID from telegram bot

    """
    url = "https://api.quotable.io/random"
    with rq.Session() as s:
        s.mount("http://", HTTPAdapter(max_retries=5))
        try:
            response = s.get(url)
            response.raise_for_status
            response = response.json()
            msg = f"QUOTE OF THE DAY:\n\n{response['content']}\nby {response['author']}"
            send_telegram_msg(msg)
        except HTTPError as error:
            send_telegram_msg(
                f"The follwing error occured while trying to fetch a random qoute from {url}\n",
                error
            )
