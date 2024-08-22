import subprocess
print('Would you like to install a program to check which DNS works well(must,y or n)?')
# domain = input('Input a domain to check the DNS(e.g:github.com)')
domain = 'github.com'
# os.system('sudo pacman -S bind')
with open('./DNS.list') as file_object:
    for dns in file_object:
        # print(dns)
        # subprocess.run(['dig',f'@{dns}',f'{domain}','|','grep','\'Query time\''])
        print('dig',f'@{dns}',f'{domain}','|','grep','\'Query time\'')
        # command = f'dig @{dns} {domain} | grep \'Query time\' | sed \'s/;;Query time://\' | sed \'s/^/ Query time:/g\' >> DNS-Checker.result | bash'
        # print(command)
        # os.system(command)
        # dig_first = subprocess.Popen(['dig', '@{}'.format(dns),domain], stdout=subprocess.PIPE)
        # grep_second = subprocess.Popen(['grep', 'Query time'], stdin=dig_first.stdout, stdout=subprocess.PIPE)
        # sed_third = subprocess.Popen(['sed', 's/;;Query time://'], stdin=grep_second.stdout, stdout=subprocess.PIPE)
        # sed_fourth = subprocess.Popen(['sed', 's/^/ Query time:/g'], stdin=sed_third.stdout, stdout=subprocess.PIPE)
        # output, _ = sed_fourth.communicate()
        # print(output)
