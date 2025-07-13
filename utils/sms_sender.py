import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Load Twilio credentials
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone = os.getenv("TWILIO_PHONE")

# DEMO_MODE defaults to True (safer for deployment)
DEMO_MODE = os.getenv("DEMO_MODE", "True").lower() == "true"

# Load recipient numbers from a text file
def load_recipients(file_path="data/recipients.txt"):
    with open(file_path, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]
    return numbers

# Send SMS to list of phone numbers
def send_sms(body, to_numbers):
    if DEMO_MODE:
        print("\n📩 [DEMO MODE ENABLED] Simulating SMS...\n")
        for number in to_numbers:
            print(f"📤 To {number}:\n{body}\n")
    else:
        client = Client(account_sid, auth_token)
        for number in to_numbers:
            try:
                message = client.messages.create(
                    body=body,
                    from_=from_phone,
                    to=number
                )
                print(f"✅ SMS sent to {number}: {message.sid}")
            except Exception as e:
                print(f"❌ Failed to send SMS to {number}: {e}")


# if __name__ == "__main__":
#     recipients = load_recipients("data/recipients.txt")

#     alert_msg = (
#         "⚠️ Alert: Heavy rainfall detected.\n"
#         "Secure inventory. Stay alert.\n"
#     )

#     send_sms(alert_msg, recipients)
