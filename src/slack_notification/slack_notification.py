from .singleton_base import Singleton
import json
import requests

SLACK_API = "https://hooks.slack.com/services/"


class SlackNotification(Singleton):
    __print_banner = False

    def __init__(self, channel, api=SLACK_API, timeout=10, print_banner=False) -> None:
        self._channel = channel
        self._api = api
        self._webhook = self._api + self._channel
        self._timeout = timeout

    def notify(self, message):
        message = self.format(message)
        response = requests.post(
            self._webhook, json.dumps(message).encode("utf-8"), timeout=self._timeout
        )
        return response

    def format(self, message):
        message = {"text": str(message)}
        return message
