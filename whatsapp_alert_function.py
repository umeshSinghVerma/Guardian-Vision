import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

def whatsapp():
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='This is a message from vigilance squad, Something mischievous is happening🤔 at the location you specified to us.',
        from_='whatsapp:' + os.getenv('TWILIO_NUMBER'),
        to='whatsapp:' + os.getenv('TARGET_NUMBER')
    )

    print(message.sid)
