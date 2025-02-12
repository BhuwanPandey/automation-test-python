
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def slack_notify(message: str):
    """Send a notification to Slack."""
    slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not slack_webhook_url:
        return
    payload = {
        "text": message,
    }
    try:
        response = requests.post(slack_webhook_url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)

