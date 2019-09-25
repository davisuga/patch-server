import requests 
import datetime
import getpass
import os
import sys
from socket import gethostname
from os import stat
hostname = gethostname()

url = 'http://0.0.0.0:5000/uploads/patch.sh'

def update(last_update, username, patch_log):
    payload = {'last_update': last_update, 'hostname':hostname, 'os':sys.platform}
    response = requests.post(url, data=payload)
    content=response.content
    with open('./update.sh', 'wb') as s:
        s.write(content)
    #print(response.json())
    if response.status_code != 200:
        pass
        #patch_log.write(str(response.status_code)+'\n')
    elif response.status_code == 200:
        patch_log.write(str(datetime.datetime.now())+'\n') 

def verify_update():
    username = getpass.getuser()
   
    try:
        with open('patch_log.txt', 'r') as patch_log:
            last_update = patch_log.readlines()[-1]
    except:
        pass
        
        

    with open('patch_log.txt', 'a') as patch_log:
        try:
            last_update = patch_log.readlines()[-1]
        except:
            pass
        if stat("patch_log.txt").st_size > 0:
            date, schedule = last_update.split(' ')
            year, month, day = date.split('-')
            hour, minute, sec = schedule.split(':')
            [year, month, day, hour, minute]=[int(i) for i in [year, month, day, hour, minute]]
            last_update_datetime = datetime.datetime(year, month, day, hour, minute)
        
            update_diff = datetime.datetime.now() - last_update_datetime
        
            if update_diff.seconds/60 >=1:
                update(last_update, username, patch_log)
                print('update')
        else:
            update(None, username, patch_log)
            print('updateb')
    os.system('bash update.sh')
verify_update()