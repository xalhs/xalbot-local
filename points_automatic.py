from modules.chatters import chatters
from modules.Settings import CHANNEL
import time
import os
import codecs
import shutil


amount = 50

T = True
while ( T == True):
    list = chatters(CHANNEL)
#    copyfile ("logsRECORDER.txt" , "copyRECORDER.txt")

    for names in list:
        name = names.split('"')[1]
        print(name)
        if os.path.isfile("var/points/" + name + ".txt"):
            from_file = open("var/points/" + name + ".txt")
            line = from_file.readline()
            print(line)
            line = int(line) + amount
            to_file = open("var/points/" + name + ".txt",mode="w")
            str_line = str(line)
            to_file.write(str_line)
            shutil.copyfileobj(from_file, to_file)
            from_file.close()
            to_file.close()
            from_file2 = open("var/TimeWatched/" + name + ".txt")
            line2 = from_file2.readline()
            line2 = int(line2) + 5
            to_file2 = open("var/TimeWatched/" + name + ".txt" , mode="w")
            str_line2 = str(line2)
            to_file2.write(str_line2)
            shutil.copyfileobj(from_file2 , to_file2)
            from_file2.close()
            to_file2.close()
        else:
            f = open("var/points/" + name + ".txt" , "w+")
            f.write(str(amount))
            f.close()
            f2 = open("var/TimeWatched/" + name + ".txt", "w+")
            f2.write("5")
            f2.close()
    time.sleep(300)

if False:
        from_file = open("var/points/" + CHANNEL + ".txt")
        line = from_file.readline()
        line = int(line) + amount
        to_file = open("var/points/"+ CHANNEL +".txt",mode="w")
        str_line = str(line)
        to_file.write(str_line)
        shutil.copyfileobj(from_file, to_file)
        from_file.close()
        to_file.close()
