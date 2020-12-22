import socket
from modules.Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():

    s = socket.socket()
    s.connect((HOST,PORT))
    a1 = "PASS " + PASS + "\r\n"
    s.sendall(a1.encode("utf-8"))
    a2 = "NICK " + IDENT + "\r\n"
    s.sendall(a2.encode("utf-8"))
    a3 = "JOIN #" + CHANNEL + "\r\n"
    s.sendall(a3.encode("utf-8"))
    print("socket connected")
    return s

def sendMessage(s, message):
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message #PRIVMSG #xalhs :Hello
        a4 = messageTemp + "\r\n"
        s.sendall(a4.encode("utf-8"))
        print("Sent: " + messageTemp)
