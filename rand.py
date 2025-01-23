import requests
import pandas as pd

# Replace with your actual Semaphore API key
API_KEY = 'd84b4096520939849a05f473c95b715e'

def retrieve_messages(api_key, limit=100, page=1, start_date=None, end_date=None, network=None, status=None):
    """
    Retrieve outgoing SMS messages from Semaphore.
    """
    url = 'https://api.semaphore.co/api/v4/messages'
    params = {
        'apikey': api_key,
        'limit': limit,
        'page': page,
        'startDate': start_date,
        'endDate': end_date,
        'network': network,
        'status': status
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def save_messages_to_excel(messages, filename='semaphore_messages.xlsx'):
    """
    Save the list of messages to an Excel file.
    """
    if messages:
        df = pd.DataFrame(messages)
        df.to_excel(filename, index=False)
        print(f"Messages saved to {filename}")
    else:
        print("No messages to save.")

if __name__ == "__main__":
    # Retrieve messages
    messages = retrieve_messages(API_KEY, limit=100, page=1)
    
    # Save messages to Excel
    save_messages_to_excel(messages)
