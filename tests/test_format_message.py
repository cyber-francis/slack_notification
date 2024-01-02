from src.slack_notification.slack_notification import SlackNotification

slack = SlackNotification("FAKE_CHANNEL")


def test_format_str():
    formated_message = slack.format("TEST_MESSAGE")
    assert formated_message == {"text": "TEST_MESSAGE"}


def test_format_dict():
    formated_message = slack.format({"KEY": "VALUE"})
    assert formated_message == {"text": "{'KEY': 'VALUE'}"}
