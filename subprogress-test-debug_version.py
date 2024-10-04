# a script what uses dig to check DNS Query time and uses grep to filter result
import subprocess
import os

with open("./DNS.list") as dns_list:
    for dns in dns_list:
        dig = f"dig @{dns} github.com"
        dig_subprocess = subprocess.Popen(
            dig.split(), stdout=subprocess.PIPE, text=True
        )
        grep_subprocess = subprocess.Popen(
            ["grep", """Query time:"""],
            stdin=dig_subprocess.stdout,
            stdout=subprocess.PIPE,
            text=True,
        )
        # grep_output,_ = grep_subprocess.communicate()
        # print(grep_output)
        sed_subprocess = subprocess.Popen(
            ["sed", """s/;; Query time:/-/g"""],
            stdin=grep_subprocess.stdout,
            stdout=subprocess.PIPE,
            text=True,
        )
        sed_outputs, _ = sed_subprocess.communicate()

# wirte result into file,incomplete
with open("./DNS-Checker-py.result", "w") as result:
    # To make sure that it can print one result for each DNS.
    sed_subprocess = subprocess.Popen(
        ["sed", "s/;; Query time: /Query time:/"], stdin=grep_subprocess.stdout
    )
    output = dig_subprocess.communicate()[0]
    print("grep", "';; Query time: '")
