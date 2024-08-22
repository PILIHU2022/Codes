# import subprocess
import os
with open('./DNS.list') as file_object:
    for dns in file_object:
        os.system(f"bash -c dig @{dns} github.com | grep ';; Query time:' >> 1")
        # print(f"dig @{dns}github.com | grep ';; Query time:'")
        # command = f'dig @{dns} github.com | grep \'Query time\' | sed \'s/;;Query time: /Query time:/\''
        # result = subprocess.run(command, capture_output=True, text=True, shell=True)
        # print(result.stdout) 
