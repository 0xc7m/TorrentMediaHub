# -*- coding: utf-8 -*-
#!/usr/bin/python3

import json
import os
import sys
import urllib.request
from urllib.parse import quote

# send text to telegram bot
def sendtext(bot_message, token=os.environ.get('TELEGRAM_TOKEN'), chat_id=os.environ.get('TELEGRAM_CHAT_ID')):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={quote(bot_message)}"
    response = urllib.request.urlopen(url)
    return response

def human_readable_size(size, decimal_places=1):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

def main():
    first_argv = int(sys.argv[1])
    size = human_readable_size(int(sys.argv[4]))
    if first_argv == 0:
        message = f"*Torrent* added %s %s Size: *%s*." %(sys.argv[2],sys.argv[3],size)
        sendtext(message)
    elif first_argv == 1:
        message = f"*Completed* torrent %s %s Size: *%s*."%(sys.argv[2],sys.argv[3],size)
        sendtext(message)

if __name__ == "__main__":
    main()