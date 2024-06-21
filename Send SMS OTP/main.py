from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()

phone_number = os.getenv('TWILIO_PHONE_NUMBER')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
verification = client.verify \
    .v2 \
    .services('VA22be8445fab7a619ddc7ba919f745310') \
    .verifications \
    .create(to='+919106930717', channel='sms')

print(verification.sid)