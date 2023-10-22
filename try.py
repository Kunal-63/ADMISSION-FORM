import vonage
client = vonage.Client(key="3153fb65", secret="hHxkHKQILNhDkC7c")
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "917984981242",
        "text": "Hello",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")