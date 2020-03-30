import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# See documentation on defining a message payload.
message = messaging.Message(
    notification=messaging.Notification(
        title='Alerta de Caida',
        body='Alguien se ha caido en la habitacion 1',
    ),
    topic='falls',
)

# Send a message to the device corresponding to the topic
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
