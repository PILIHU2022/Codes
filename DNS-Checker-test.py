import subprocess

# 定义 DNS 服务器地址和域名
domain = 'github.com'

with open('./DNS.list') as file_object:
    for dns in file_object:
        # 使用 subprocess.Popen 来创建子进程
        p1 = subprocess.Popen(['dig', '@{}'.format(dns), domain], stdout=subprocess.PIPE)
        
        # 使用管道连接命令
        p2 = subprocess.Popen(['grep', 'Query time'], stdin=p1.stdout, stdout=subprocess.PIPE)
        
        # 继续使用管道连接命令
        p3 = subprocess.Popen(['sed', 's/;;Query time://'], stdin=p2.stdout, stdout=subprocess.PIPE)
        
        # 最后一次使用管道连接命令
        p4 = subprocess.Popen(['sed', 's/^/ Query time:/g'], stdin=p3.stdout, stdout=subprocess.PIPE)
        
        # 获取最终输出
        output, _ = p4.communicate()

# 将输出追加到文件
with open('./DNS-Checker.result', 'a') as file:
    file.write(output.decode().strip() + '\n')

# 检查返回码
if p4.returncode != 0:
    print("An error occurred while executing the commands.")
else:
    print("Commands executed successfully.")
