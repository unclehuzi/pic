from pathlib import Path

p = Path("folderPath") # e.g. /content/posts/
FileList=list(p.glob("**/*.md")) 

def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串

    Reference: https://blog.csdn.net/qq_30068487/article/details/90297814
    
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)


o_s = "https://gitee.com/unclehuzi/picture/raw/master/img"
n_s = "https://raw.githubusercontent.com/unclehuzi/pic/master/img"

for file in FileList:
    alter(file, o_s, n_s)