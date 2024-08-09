import os
print('Would you like to install a program to check which DNS works well(must,y or n)?')
domain = input('Input a domain to check the DNS(e.g:github.com)')
# os.system('sudo pacman -S bind')
with open('./DNS-List.json') as file_object:
    for dns in file_object:
        print(dns)
        command = f'dig @{dns} {domain} | grep \'Query time\' | sed \'s/;;Query time://\' | sed \'s/^/ Query time:/g\' >> DNS-Checker.result | bash'
        # print(command)
        os.system(command)
