import requests
import threading
from modules.Settings import NIGHTBOT_AUTH

Auth = NIGHTBOT_AUTH

def songrequest(search):
    body = {"q" : search}
    request = requests.post("https://api.nightbot.tv/1/song_requests/queue", headers={"Authorization":"Bearer " + Auth} ,  data = body)
    print(request.text)
    if "Video too long" in (request.text):
        return 1

    elif ("Video too short") in (request.text):
        return 2


    try:
        duration = ((request.text).split('","duration":')[1]).split(',"title')[0]
        title = ((request.text).split(',"title":"')[1]).split('","artist":"')[0]
        artist = ((request.text).split('","artist":"')[1]).split('","url"')[0]
        position = ((request.text).rsplit('"_position":', 1 )[1]).split('}}')[0]
        id = (request.json())["item"]["_id"]
    except:
        return 0
    class Song:
        def __init__(self):
            Song.dur = duration
            Song.name = title
            Song.artist = artist
            Song.pos = position
            Song.id = id
    print(duration)
    return Song()

def skipsong(title):
    #while (sskip == false):
    #    pass
    print(title)
    request = requests.get('https://api.nightbot.tv/1/song_requests/queue', headers = {"Authorization":"Bearer " + Auth})
    print(request.text)
    if ((request.text).split('"title":"')[1]).split('","artist":"')[0] == title:
        request = requests.post("https://api.nightbot.tv/1/song_requests/queue/skip", headers={"Authorization":"Bearer " + Auth})

def currentsong():
    request = requests.get("https://api.nightbot.tv/1/song_requests/queue" , headers={"Authorization":"Bearer " + Auth}).json()
    print(request)
    if request["_currentSong"] is None:
        return 0
    title = request["_currentSong"]["track"]["title"]
    print(title)
    artist = request["_currentSong"]["track"]["artist"]
    print(artist)
    url = request["_currentSong"]["track"]["url"]
    id = request["_currentSong"]["_id"]
    return[title, url , id]



def instaskipsong():
    request = requests.post("https://api.nightbot.tv/1/song_requests/queue/skip", headers={"Authorization":"Bearer " + Auth})


#songrequest("NaM or die")
