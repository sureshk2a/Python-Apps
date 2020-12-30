import json
import time
from datetime import datetime as dt
import logging as log

#File paths are not relative below

hostFile = "C:\Windows\System32\drivers\etc\hosts"
hostTemp = "E:\Workspace\Python-Apps\Website_Blocker\hosts"
redirect = "127.0.0.1"
data = json.load(open("E:\Workspace\Python-Apps\Website_Blocker\data.json"))
blockFrom = data["ToBlockFrom"]
blockTill = data["ToBlockTill"]

log.basicConfig(filename="E:\Workspace\Python-Apps\Website_Blocker\webBlocker_{0}.log".format(str(dt.now().date()).replace("-","_")),filemode="a",
              format='%(asctime)s,%(msecs)d %(name)s - %(levelname)s - %(message)s',datefmt='%H:%M:%S',level=log.DEBUG)

try:
    while True:
      if dt(dt.now().year, dt.now().month, dt.now().day, blockFrom) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, blockTill):
          log.warning("Working time, so blocking the sites - {0}".format(data["domain"]))
          with open(hostTemp, "r+") as file:
              content = file.read()
              for website in data["domain"]:
                  if website in content:
                      pass
                  else:
                      file.write(redirect + " " + website + "\n")
      else:
          log.info("Unblocking all sites cause it's non working hours, have fun!!")
          with open(hostTemp, "r+") as file:
              content = file.readlines()
              file.seek(0)
              for line in content:
                  if not any(website in line for website in data["domain"]):
                      file.write(line)
              file.truncate()
      time.sleep(5)
except Exception as e:
    log.exception(e.with_traceback())
