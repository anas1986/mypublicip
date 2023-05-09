import json
import urllib.request

def get_client_public_ip():
    try:
        # Send a GET request to ipify API
        response = urllib.request.urlopen('https://api.ipify.org?format=json')
        
        # Read the response and decode it
        data = response.read().decode('utf-8')
        
        # Parse the JSON response
        ip_address = json.loads(data)['ip']
        
        return ip_address
    except urllib.error.URLError:
        return None

# Call the function to get the client's public IP address
client_ip = get_client_public_ip()

if client_ip:
    print("Client Public IP Address:", client_ip)
else:
    print("Unable to retrieve the client's public IP address.")
