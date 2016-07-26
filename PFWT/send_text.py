
#Send a SMS message

from twilio.rest import TwilioRestClient

account_sid = "None"# Your Accounr SID from www.twilio.com/console
auth_token = "{{}}" # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.message.create(body="Hello from Python",
	to="+8441231231", 	# Replace with your phone number
	from_="+8441231231")# Replace with your Twilio number

print(message.sid)