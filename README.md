# Slack-Notification
A simple way to send slack notification

## Install
```
pip install -i slack-notification
```

## Usage
```python
from slack_notification.slack_notification import SlackNotification

CHANNEL = "YOUR_CHANNEL" #example TXXXXXXXXXX/BXXXXXXXX/NXXXXXXXXXX"
slack = SlackNotification(CHANNEL)
message = "YOUR_MESSAGE"
response = slack.notify(message)
```
