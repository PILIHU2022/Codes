import os

fit_filesname = []
fit_content = []


def check_dir():
    while True:
        directory = input("What directory do you want to find keyword(绝对路径):")
        if os.path.isdir(directory):
            break
        else:
            print("Error dir! Reinput!")
    global files_in_dir
    files_in_dir = os.listdir(directory)


def get_keyword():
    global keyword
    global filename
    keyword = input("Input what keyword you want to find:")
    filename = input("Input the file what you want to find or .lua:")


def filter_files():
    for filesname_in_dir in files_in_dir:
        if filename in filesname_in_dir:
            fit_filesname.append(filesname_in_dir)


def find_keyword():
    for filename_in_dir in fit_filesname:
        fit_content.clear()
        with open(filename_in_dir) as file_object:
            print(f"---{filename_in_dir}---")
            for lines in file_object:
                if keyword in lines:
                    fit_content.append(lines)
            if len(fit_content) == 0:
                print("Not fit content!")
            else:
                for line in fit_content:
                    print(line.strip())


check_dir()
get_keyword()
filter_files()
find_keyword()
