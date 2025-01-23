import requests
from urllib.parse import urlencode

apikey = 'd84b4096520939849a05f473c95b715e'
sendername = 'SEMAPHORE'  # Replace with a valid sender name

def send_message(message, number):
    print('Sending Message...')
    
    params = {
        'apikey': apikey,
        'sendername': sendername,
        'message': message,
        'number': number
    }
    
    url = f"https://semaphore.co/api/v4/messages?{urlencode(params)}"
    response = requests.post(url)
    
    if response.status_code == 200:
        print('Message Sent Successfully!')
        print(f"Response: {response.json()}")
    else:
        print(f"Failed to send message. HTTP Status: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == '__main__':
    message = "I just sent my first message with Semaphore"
    number = "09471039981"
    send_message(message, number)
