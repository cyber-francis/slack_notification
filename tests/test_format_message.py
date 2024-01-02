from src.slack_notification.slack_notification import SlackNotification


def test_format_str():
    slack = SlackNotification("FAKE_CHANNEL")
    formated_message = slack.format("TEST_MESSAGE")
    assert formated_message == {"text": "TEST_MESSAGE"}


def test_format_dict():
    slack = SlackNotification("FAKE_CHANNEL")
    formated_message = slack.format({"KEY": "VALUE"})
    assert formated_message == {"text": "{'KEY': 'VALUE'}"}
    formated_message = slack.format
