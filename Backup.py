# This is a backup script to copy some config files or folders to make sure that you backuped.
# Written in Python by PILIHU with Baidu Wenyanyixin AI
import os 
import subprocess 
import time 
# 源路径
home_source_pathes = ('/home/PILIHU/.config/nvim','/home/PILIHU/.config/dunst','/home/PILIHU/.config/hypr','/home/PILIHU/.config/ranger','/home/PILIHU/.zprofile','/home/PILIHU/.zshrc','/home/PILIHU/.zprofile','/home/PILIHU/.config/zsh.d')
etc_source_pathes = ('/etc/clash-meta','/etc/doas.conf','/etc/pacman.conf','/etc/paru.conf')

# 目标文件夹(若打算上传到GitHub需有git版本控制)
home_target_path = '/Back_up/My-Config/config'
etc_target_path = '/Back_up/My-Config/etc'

# 需要复制的文件(default=*)
# files = '*'

# 复制home的文件:home_source_pathes
while 1+1 == 2:
    for home_source_path in home_source_pathes:
        # 复制源路径中的所有文件，包括文件夹
        subprocess.run(['cp','-r',home_source_path,home_target_path])
        os.system("notify-send '已将文件复制到/Back_up/My-Config/config文件夹,详情见~/Backup.py'")
    time.sleep(1800)

# 复制etc的文件:etc_source_pathes
while 2+2 == 4:
    for etc_source_path in etc_source_pathes:
        # 复制原路径中的所有文件，包括文件夹
        subprocess.run(['cp','-r',etc_source_path,etc_target_path])
        os.system("notify-send '已将文件复制到/Back_up/My-Config/etc文件夹,详情见~/Backup.py'")
    time.sleep(1800)
