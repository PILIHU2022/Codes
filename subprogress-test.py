# a script what uses dig to check DNS Query time and uses grep to filter result
import subprocess,os
# os.system("touch DNS-Checker-py.result")

with open('./DNS.list') as dns_list:
    for dns in dns_list:
        dig = f'dig @{dns} github.com'
        dig_subprocess = subprocess.Popen(
            dig.split(),
            stdout=subprocess.PIPE,
            text=True
            )
        # grep_subprocess = subprocess.Popen(grep.split(), stdin=dig_subprocess.stdout, stdout=subprocess.PIPE)
        grep_subprocess = subprocess.Popen(
            ['grep', '''Query time:'''],
            stdin=dig_subprocess.stdout,
            stdout=subprocess.PIPE,
            text=True
        )
        grep_output,_ = grep_subprocess.communicate()
        print(grep_output)
# wirte result into file,incomplete
with open('./DNS-Checker-py.result') as result:
    with open('./DNS.list') as dns_list_w:
        for dns_w in dns_list_w:
            print(dns_w)
            # result.write(grep_subprocess)
        # sed_subprocess = subprocess.Popen(['sed','s/;; Query time: /Query time:/'], stdin=grep_subprocess.stdout)
        # output = dig_subprocess.communicate()[0]
        # print('grep','\';; Query time: \'')
