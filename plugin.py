import flask
import requests
from twilio.rest import Client
import json

app = flask.Flask(__name__)

# Replace with your Jira API credentials
JIRA_API_URL = ''
JIRA_AUTH_TOKEN = ''

# Replace with your Twilio API credentials
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = ''

def create_jira_issue(summary, description):
    url = ''
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json'
    }

    payload=json.dumps(   
        {
        'fields': {
            'project': {
                'key': 'NEW'  # Replace 'PROJECT_KEY' with your Jira project key
            },
            'summary': summary,
            'description': description,
            'issuetype': {
                'name': 'Task'  # Replace 'Task' with the desired issue type
            }
        }
    }
    )
    
    auth = ('',JIRA_AUTH_TOKEN)
    
    response = requests.post(url, headers=headers,data=payload, auth=auth)
    print(response.text)
    if response.status_code == 201:
        return response.json()['key']  # Returns the key of the created issue
    else:
        return None

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    data = flask.request.form
    message = data['Body']
    senderId = data['From'].split('+')[1]
    
    # Create Jira issue
    issue_key = create_jira_issue(summary='WhatsApp Message', description=message)
    
    if issue_key:
        response_message = f"Jira issue created: {issue_key}"
    else:
        response_message = "Failed to create Jira issue"
    
    return response_message

if __name__ == "__main__":
    app.run(port=5000,debug=True)
