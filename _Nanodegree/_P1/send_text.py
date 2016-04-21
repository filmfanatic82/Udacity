from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4c750386429bd5fec73d594ecdcd22b8"
auth_token  = "80e2525fc3205f0411309ac00d333151"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is Ron Burgandy?",
    to="+12012812438",    # Replace with your phone number
    from_="+19082900867") # Replace with your Twilio number
print message.sid
