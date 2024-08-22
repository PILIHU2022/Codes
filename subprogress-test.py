import subprocess

# command1 = "ls -l /home/PILIHU/Codes/"
# command2 = "grep .py
grep = 'grep \'Query time\''
sed = 'sed \'s/;;Query time:/Query time:/\''
with open('./DNS.list') as dns_list:
    for dns in dns_list:
        dig = f'dig @{dns} github.com'
        dig_subprocess = subprocess.Popen(dig.split(), stdout=subprocess.PIPE)
        grep_subprocess = subprocess.Popen(grep.split(), stdin=process1.stdout, stdout=subprocess.PIPE)
        sed_subprocess = subprocess.Popen(sed.split())
        output = process2.communicate()[0]
        print(output.decode("utf-8"))
