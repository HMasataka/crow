import requests
from logging import getLogger


logger = getLogger(__name__)


def req():
    response = requests.get("https://oshi-connect.com/")

    try:
        response.raise_for_status()
    except requests.RequestException as e:
        if e.response is not None:
            logger.exception("response error", e.response.text)
        else:
            logger.exception("response error")
    else:
        logger.exception("unexpected error")

    print(response.text)
