import json
import urllib.request
import os

def lambda_handler(event, context):
    issue_link = event['issue']['html_url']
    message = {
        'text': f"Issue Created: {issue_link}"
    }
    message_json = json.dumps(message).encode('utf-8')
    webhook_url = os.environ.get('SLACK_URL')
    req = urllib.request.Request(webhook_url, data=message_json, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print("Message sent successfully to Slack:", response_body)
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to Slack successfully')
    }
