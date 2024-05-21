import os
import plistlib
from datetime import datetime
import uuid
import hashlib
from colorama import Fore, init


def generate_uuid_from_str(s):
    return str(uuid.UUID(hashlib.md5(s.encode('utf-8')).hexdigest()))


#Color 
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
fs = Fore.RESET

#Clear_Terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


#Banner Print
print(f"""{fg}
 ░▒▓██████▓▒░░▒▓███████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ FREE v1.0     
      
                                {fc}[+] IPHONE Proile Creator
                                {fm}[+] Dev : X0P4SH4 & AIGPTCODE
                               \033[1;31m [+] t.me/LearnExploit{fs}{fr}                           
""")

# دریافت ورودی‌ها از کاربر
payload_uuid = input("Enter Payload UUID (leave empty or enter 'd' for auto-generation): ")
payload_identifier = input("Enter Payload Identifier (leave empty or enter 'd' for auto-generation): ")
proxy_server = input("Enter Proxy Server (leave empty for none): ")
proxy_server_port = input("Enter Proxy Server Port (leave empty for none): ")
authentication_type = input("Enter Authentication Type (CHAP or PAP): ")
name = input("Enter APPName:((e.g): mcinet or mtnirancell or RighTel): ")

# بررسی ورودی‌ها و تعیین مقادیر پیش‌فرض
if not payload_uuid or payload_uuid.lower() == 'd':
    payload_uuid = str(uuid.uuid4())

if not payload_identifier or payload_identifier.lower() == 'd':
    payload_identifier = generate_uuid_from_str(proxy_server + proxy_server_port)

# تنظیم مقدار AuthenticationType بر اساس انتخاب کاربر
if authentication_type.upper() == 'CHAP':
    authentication_type_value = 'CHAP'
elif authentication_type.upper() == 'PAP':
    authentication_type_value = 'PAP'
else:
    print("Invalid Authentication Type. Please enter either 'CHAP' or 'PAP'.")
    exit()

# اضافه کردن مقادیر proxy_server و proxy_server_port به دیکشنری پیکربندی
config = {
    'ConsentText': {
        'default': 'tele : LearnExploit'
    },
    'PayloadContent': [
        {
            'APNs': [
                {
                    'AllowedProtocolMask': 1,
                    'AllowedProtocolMaskInDomesticRoaming': 1,
                    'AllowedProtocolMaskInRoaming': 1,
                    'AuthenticationType': authentication_type_value,
                    'DefaultProtocolMask': 1,
                    'EnableXLAT464': True,
                    'Name': name,
                    'ProxyServer': proxy_server if proxy_server else '',
                    'ProxyServerPort': int(proxy_server_port) if proxy_server_port else ''
                }
            ],
            'PayloadDisplayName': 'Cellular',
            'PayloadIdentifier': payload_identifier,
            'PayloadType': 'com.apple.cellular',
            'PayloadUUID': payload_uuid,
            'PayloadVersion': 1
        }
    ],
    'PayloadDescription': f'{name}',
    'PayloadDisplayName': 't.me/LearnExploit | t.me/BypassNetwork',
    'PayloadIdentifier': payload_identifier,
    'PayloadOrganization': 'Subscribe us',
    'PayloadRemovalDisallowed': False,
    'PayloadType': 'Configuration',
    'PayloadUUID': payload_uuid,
    'PayloadVersion': 1,
    'RemovalDate': datetime(2028, 5, 22, 15, 37, 24)
}

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'config.mobileconfig')

# نوشتن فایل plist
with open('config.mobileconfig', 'wb') as f:
    plistlib.dump(config, f)

print(f"{fg}mobile configuration file created successfully!{fr}")
