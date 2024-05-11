# Import necessary modules from Telethon
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest

# Import configparser for handling configuration files
import configparser
import os, sys
import csv
import traceback
import time
import random

# ANSI color codes for text formatting


# Read configuration data from config file
cpass = configparser.RawConfigParser()
cpass.read('config.data')

# Initialize Telegram client with API credentials
try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    print("[!] run python setup.py first bebe\n")
    sys.exit(1)

# Connect to Telegram server
client.connect()

# Authorize the user if not already authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    client.sign_in(phone, input('[+] Enter the code: '))

os.system('clear')

# Read input file containing user data
input_file = sys.argv[1]
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)  # Skip header row
    for row in rows:
        user = {}
        user['First Name'] = row[0]
        user['id'] = int(row[12])  # Extract user ID from specific column in CSV file
        users.append(user)

# Retrieve chats and groups
chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash=0
         ))
chats.extend(result.chats)

# Filter and collect megagroups
for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

# Display available groups to choose from
i = 0
for group in groups:
    print('[' + str(i) + ']' + ' - ' + group.title)
    i += 1

# Prompt user to choose a group to add members
print('[+] Choose a group to add members')
g_index = input("[+] Enter a Number : ")
target_group = groups[int(g_index)]

# Create target group entity
target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

# Prompt user to select add member mode
print("[1] add member by user ID\n[2] add member by username ")
mode = int(input("Input : "))
n = 0

# Iterate over users and add them to the selected group
for user in users:
    n += 1
    if n % 50 == 0:
        time.sleep(1)
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['First Name'] == "":
                continue
            user_to_add = client.get_input_entity(user['First Name'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("[!] Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("[+] Waiting for 5-10 Seconds...")
        time.sleep(random.randrange(5, 10))
    except PeerFloodError:
        print("[!] Getting Flood Error from telegram. \n[!] Script is stopping now. \n[!] Please try again after some time.")
    except UserPrivacyRestrictedError:
        print("[!] The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print("[!] Unexpected Error")
        continue
