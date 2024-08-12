import subprocess
print('Would you like to install a program to check which DNS works well(must,y or n)?')
domain = input('Input a domain to check the DNS(e.g:github.com)')
# os.system('sudo pacman -S bind')
with open('./DNS-List.json') as file_object:
    for dns in file_object:
        dig_first = subprocess.Popen(['dig', '@{}'.format(dns),domain], stdout=subprocess.PIPE)
        grep_second = subprocess.Popen(['grep', 'Query time'], stdin=dig_first.stdout, stdout=subprocess.PIPE)
        sed_third = subprocess.Popen(['sed', 's/;;Query time://'], stdin=grep_second.stdout, stdout=subprocess.PIPE)
        sed_fourth = subprocess.Popen(['sed', 's/^/ Query time:/g'], stdin=sed_third.stdout, stdout=subprocess.PIPE)
        output, _ = sed_fourth.communicate()
        print(output)
