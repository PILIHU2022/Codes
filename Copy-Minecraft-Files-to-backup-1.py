import os
import time
# localtime= time.strftime('%H:%M', time.localtime())
localhour = time.strftime('%H', time.localtime())
src_dir = '/home/PILIHU/.minecraft/versions/1.20.4/'
target_dir = '~/Minecraft'
get_current_pid = os.getpid()
check_dir = os.listdir('/home/PILIHU/.minecraft/versions/1.20.4/saves/')
while True:
    if len(check_dir) == 0:
        break
    if localhour >= '12':
        os.system(f'kill {get_current_pid}')
    os.system(f"rsync -a -r --quiet --delete {src_dir}* {target_dir}")
    os.system('notify-send \'Finished copy Minecraft files\'')
    # os.system(f'cd {backup_location} && git add . && git commit -S -m "Normal backup" && git push main')
    time.sleep(1800)
