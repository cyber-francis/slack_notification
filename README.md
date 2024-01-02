# Slack-Notification
A simple way to send slack notification

## Install
```
pip install -i https://test.pypi.org/simple/ slack-notification
```

## Usage
```python
from slack_notification.slack_notification import SlackNotification

CHANNEL = "YOUR_CHANNEL" #example T06C3XXXXXX/B06CURXXXX/NU9qdi16r5IdXXXXXXX"
slack = SlackNotification(CHANNEL)
message = {"text": "test"}
response = slack.notify(message)
```
