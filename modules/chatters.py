import requests

def chatters(CHANNEL):
    request = requests.get("https://tmi.twitch.tv/group/user/" + CHANNEL + "/chatters")
#    print(request.text)
#    print(request.status_code)
    unsep1 = ((request.text).split('moderators": [')[1]).split("]")[0]
    m = unsep1.split(",")
    unsep2 = ((request.text).split('vips": [')[1]).split("]")[0]
    vip = unsep2.split(",")
    unsep3 = ((request.text).split('staff": [')[1]).split("]")[0]
    s = unsep3.split(",")
    unsep4 = ((request.text).split('admins": [')[1]).split("]")[0]
    a = unsep4.split(",")
    unsep5 = ((request.text).split('global_mods": [')[1]).split("]")[0]
    g = unsep5.split(",")
    unsep6 = ((request.text).split('viewers": [')[1]).split("]")[0]
    v = unsep6.split(",")
    chatters = ['"xalhs"']
    if m[0] == "":
        pass
    else:
        chatters =  chatters + m
    if vip[0]  == "":
        pass
    else:
        chatters = chatters + vip

    if  s[0]  == "":
        pass
    else:
        chatters = chatters +  s
    if a[0]  == "":
        pass
    else:
        chatters = chatters + a
    if g[0]  == "":
        pass
    else:
        chatters = chatters + g
    if v[0]  == "":
        pass
    else:
        chatters = chatters + v
#    if getViewers(CHANNEL)[0]  == "":
#        pass
#    else:
#        chatters = chatters + getViewers(CHANNEL)

#    chatters =  getModerators(CHANNEL) + getVIPs(CHANNEL) + getStaff(CHANNEL) + getAdmins(CHANNEL) + getGlobalmods(CHANNEL) + getViewers(CHANNEL)
    return chatters
