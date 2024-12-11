import sys
import json
import struct
from stem.control import Controller

# Function to send a response to the extension
def send_message(message):
    message = json.dumps(message)
    sys.stdout.write(struct.pack('I', len(message)))
    sys.stdout.write(message)
    sys.stdout.flush()

# Function to read messages from the extension
def read_message():
    raw_length = sys.stdin.read(4)
    if not raw_length:
        return None
    message_length = struct.unpack('I', raw_length)[0]
    message = sys.stdin.read(message_length)
    return json.loads(message)

# Function to change Tor IP
def change_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_password')  # Set your Tor control password here
            controller.signal("NEWNYM")
            send_message({"success": True, "message": "IP changed successfully"})
    except Exception as e:
        send_message({"success": False, "message": str(e)})

# Main script loop
if __name__ == "__main__":
    while True:
        incoming_message = read_message()
        if incoming_message and incoming_message.get("command") == "change_ip":
            change_tor_ip()
