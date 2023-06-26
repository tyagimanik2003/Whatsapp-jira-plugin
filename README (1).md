# Project Name

## Description

This project is a Flask application that integrates with Jira and Twilio to create Jira issues from incoming WhatsApp messages. It allows you to automatically create Jira issues by sending messages to a specific WhatsApp number.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:

```shell
git clone <repository_url>
```

2. Install the required dependencies using pip:

```shell
pip install -r requirements.txt
```

3. Set up the necessary API credentials:

- Jira API credentials:
  - Replace the `JIRA_API_URL` variable in the code with the URL of your Jira API.
  - Replace the `JIRA_AUTH_TOKEN` variable in the code with your Jira authentication token.

- Twilio API credentials:
  - Replace the `TWILIO_ACCOUNT_SID` variable in the code with your Twilio account SID.
  - Replace the `TWILIO_AUTH_TOKEN` variable in the code with your Twilio authentication token.
  - Replace the `TWILIO_PHONE_NUMBER` variable in the code with your Twilio phone number.

4. Start the Flask application:

```shell
python app.py
```

## Usage

Once the application is running, you can interact with it using the following endpoints:

- `/home`: Displays a simple "Hello World" message.

- `/whatsapp` (POST): Receives incoming WhatsApp messages and creates a Jira issue based on the message content.
  - Example request:
    ```shell
    POST /whatsapp
    Body:
    message=<your_message>&From=<sender_number>
    ```
    - Replace `<your_message>` with the content of your WhatsApp message.
    - Replace `<sender_number>` with the sender's phone number.

## How It Works

1. When the Flask application receives a POST request to the `/whatsapp` endpoint with a message and sender number, it triggers the `whatsapp` function.

2. The `whatsapp` function extracts the message content and sender number from the request data.

3. It calls the `create_jira_issue` function, passing the message content as the issue summary and description.

4. The `create_jira_issue` function sends a POST request to the Jira API to create a new issue using the provided credentials and the message content.

5. If the issue is created successfully (status code 201), the `create_jira_issue` function returns the key of the created issue. Otherwise, it returns `None`.

6. Based on the response from `create_jira_issue`, the `whatsapp` function generates a response message indicating whether the Jira issue was created successfully or not.

7. The response message is returned as the HTTP response to the POST request.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).