import string
from modules.Settings import CHANNEL #could be done better prob

def getUser(line):
    separete = line.split(";emote", 1)[0]
    #print(separete)
    user = separete.split("display-name=" , 1)[1]
#    separate = line.split(":", 2) old getuser commands
#    user = separate[1].split("!", 1)[0]
    return user

def getStatus(line):
    sep = (line.split("badges=")[1]).split(";display")[0]
    if ("broadcaster" in sep) or ("moderator" in sep):
        return True
    else:
        return False

def getBStatus(line):
    sep = (line.split("badges=")[1]).split(";display")[0]
    if ("broadcaster" in sep):
        return True
    else:
        return False

def getMessage(line):
    if line.startswith("meflag=True"):
        txt = (line.split("PRIVMSG #" + CHANNEL + " :", 1)[1]).split("ACTION" , 1)[1]
        message = "/me " + txt[:-2]
    else:
        txt = line.split("PRIVMSG #" + CHANNEL + " :", 1)[1]
        message = txt.rsplit("\r" , 1)[0]

#    txt = line.split(":", 2)[2]  old getmessage command
#    message = txt.rstrip("\r")
    return message

def getEmotes(line):
    temp = line.split("PRIVMSG")[0]
    temp2 = temp.split("display-name=")[1]
    #temp3 = temp2.split(";")[1]
    temp4 = temp2.split("emotes=")[1]
    temp5 = temp4.split(";flags")[0]
    first = temp5.split("/")
    emotes = ""
    for second in first:
        third = second.split(":")[0]
        count = second.count(",") + 1
        emotes = emotes + " " + third + " " + str(count) + " times"
    return emotes

def getPointRewards(line):
    try:
        temp = line.split('custom-reward-id=')[1]
        rewardsCode = temp.split(';display-name')[0]
        print(rewardsCode)

        if rewardsCode == "a13974c7-d13d-4334-96ae-e339979650d8":
            return 1
        if rewardsCode == "389e8a26-cbaa-411e-93b8-b3f03875a249":
            return 2
        if rewardsCode == "63c1db00-ba1d-464e-be8a-aa3084a57193":
            return 3
        if rewardsCode == "23e05424-ed89-4f4c-9716-cc12f1e69262":
            return 4
        if rewardsCode == "a8d6bee4-2c09-44a4-a48e-e2478091bd90"
            return 5
        if rewardsCode == "12c0ee6d-8e10-4e98-b39b-96eb3466be5f"
            return 6    


    except:
        return 0
