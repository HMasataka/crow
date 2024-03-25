import time
import requests


def req():
    response = requests.get("https://note.lapras.com/")
    response.raise_for_status()

    print(response.text)
