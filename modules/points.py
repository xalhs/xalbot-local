import random
import os
import codecs
import shutil
import time
from modules.Settings import CHANNEL

def points(name):
    if os.path.isfile("var/points/" + name + ".txt"):
        f= codecs.open("var/points/" + name + ".txt", "r" , "utf-8")
        s = f.readline()
        f.close()
        return int(s)
    else:
        return 0

def Roulette(name , amount):
    p = points(name)
    if p < amount and amount > 0 :
        return 0
    else:
        s = random.random()
        print("s= " + str(s))
        if s < 0.5:

            from_file = open("var/points/" + name + ".txt")
            line = from_file.readline()
            line = int(line) - amount
            to_file = open("var/points/" + name + ".txt",mode="w")
            str_line = str(line)
            to_file.write(str_line)
            shutil.copyfileobj(from_file, to_file)
            from_file.close()
            to_file.close()
            f= codecs.open("var/Roulette/" + name + ".txt", "a+" , "utf-8")
            f.write(((time.ctime(time.time())).split(" ", 1)[1]).rsplit(" " , 1)[0]  + " roulette: -" + str(amount) +  "\r\n")
            f.close()
            return -1
        else:
            from_file = open("var/points/" + name + ".txt")
            line = from_file.readline()
            line = int(line) + amount
            to_file = open("var/points/" + name + ".txt",mode="w")
            str_line = str(line)
            to_file.write(str_line)
            shutil.copyfileobj(from_file, to_file)
            from_file.close()
            to_file.close()
            f= codecs.open("var/Roulette/" + name + ".txt", "a+" , "utf-8")
            f.write(((time.ctime(time.time())).split(" ", 1)[1]).rsplit(" " , 1)[0] + " roulette: +" + str(amount) +  "\r\n")
            f.close()
            return 1

def PointsIncrease(name, amount):
    from_file = open("var/points/" + name + ".txt")
    line = from_file.readline()
    line = int(line) + amount
    to_file = open("var/points/" + name + ".txt",mode="w")
    str_line = str(line)
    to_file.write(str_line)
    shutil.copyfileobj(from_file, to_file)
    from_file.close()
    to_file.close()

def PointsDecrease(name, amount):
    from_file = open("var/points/" + name + ".txt")
    line = from_file.readline()
    line = int(line) - amount
    to_file = open("var/points/" + name + ".txt",mode="w")
    str_line = str(line)
    to_file.write(str_line)
    shutil.copyfileobj(from_file, to_file)
    from_file.close()
    to_file.close()

#def givePoints(user1, user2, amount):
