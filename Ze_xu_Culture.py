# Another:PILIHU(Spark)
# Date:2024-10-04
# Version:1.0.0
# Only use to take a part in the Ze Xu Culture programming competition
# This file in licensed under the CC BY-NC-ND license.
# NOTE: You mustn't use this programming work to take a part in Humen No.3 Middle School's computer programming competition.
# See GitHub https://github.com/PILIHU2022/Codes/blob/main/Ze_xu_Culture.py
import os

print(
    "该程序是用于将某文件夹备份到另外一个文件夹,若文件夹中已有文件,则将一整个文件夹复制到目标文件夹"
)

# Get directory to operate
source_directories = []
target_directories = []

get_source_directory = ""
while True:
    get_source_directory = input(
        "请输入你想要操作的文件夹(仅一个,路径无须在后面加`/`, 退出请输入`!q`):"
    )
    if get_source_directory == "!q":
        break
    get_target_directory = input("请输入你想要操作的目标文件夹(仅一个):")
    source_directories.append(get_source_directory)
    target_directories.append(get_target_directory)


def __move_directory():
    for source_directory, target_directory in zip(
        source_directories, target_directories
    ):
        # Copy the full folder to target directory
        os.system(f"rsync -a -r --delete {source_directory}/* {target_directory}")
        # Copy each file in the source directory
        # os.system(f"rsync -a -r --delete {source_directory} {target_directory}")


def __print_ze_xu_information():
    print(
        """
您的操作正在执行, 在执行的时候我们一起来学习关于则徐文化吧!\n
首先, 我们来了解一下林则徐吧\n
林则徐（1785年－1850年），是清朝末期著名的政治家、军事家和民族英雄，以其在1839年主持禁烟和销烟的行动而闻名，被誉为中国近代史的开端人物之一。\n
然后, 我们再来了解一下林则徐虎门销烟:
    """
    )


def __print_information_of_Humen_gunsmoke():
    some_information_of_Humen_gunsmoke = [
        "1839年，林则徐到达广州，开始强力打击鸦片贸易。他采取了一系列严厉措施，包括下令所有外国商人上缴鸦片。由于其铁腕手段，英美商人迫于压力最终交出了大量鸦片。",
        "虎门销烟: 1839年6月3日，林则徐在广东虎门海滩上公开销毁缴获的2.37万箱（约118万斤）鸦片。这一行动历时23天，林则徐亲自监督，鸦片被投入石灰和盐水中溶解，随后流入大海。这一举动不仅象征着中国抵抗鸦片侵害的决心，也成为清政府禁烟行动的历史性标志。",
    ]
    for each_information_of_Humen_gunsmoke in some_information_of_Humen_gunsmoke:
        print(f"{each_information_of_Humen_gunsmoke}\n")


def __print_poem_of_ze_xu():
    some_poem_of_ze_xu = [
        "苟利国家生死以，岂因祸福避趋之。",
        "海纳百川，有容乃大；壁立千仞，无欲则刚。",
    ]
    for each_poem_of_ze_xu in some_poem_of_ze_xu:
        print(f"{each_poem_of_ze_xu}\n")


__print_ze_xu_information()
__print_information_of_Humen_gunsmoke()
print("最后, 我们来领略一下林则徐所写的名言警句:\n")
__print_poem_of_ze_xu()
print("任务执行完毕, 退出可能需要时间, 请耐心等待")
__move_directory()
print("感谢使用!")
