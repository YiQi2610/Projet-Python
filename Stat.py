import re

from pythonprojet import lireficlog
objet=lireficlog("apache_logs")
def detect_mac(log):
    mac = 0
    for l in log:
        part = "".join(l['syst_agent'])      #transformation liste en string
        if 'Mac' in part:          # recherche Mac OS dans notre liste
            mac = mac + 1
    return mac
def detect_win(log):
    win = 0
    for l in log:
        part = "".join(l['syst_agent'])      #transformation liste en string
        if 'Windows' in part:  # recherche windows dans notre liste
            win = win + 1
    return win
def detect_linux(log):
    linux = 0
    for l in log:
        part = "".join(l['syst_agent'])      #transformation liste en string
        if 'Linux' in part:  # recherche linux dans notre liste
            linux = linux + 1
    return linux
def detect_ios(log):
    ios = 0
    for l in log:
        part = "".join(l['syst_agent'])      #transformation liste en string
        if 'iPhone' in part:  # recherche ios dans notre liste
            ios = ios + 1
    return ios
def detect_android(log):
    android = 0
    for l in log:
        part = "".join(l['syst_agent'])      #transformation liste en string
        if 'Android' in part:  # recherche android dans notre liste
            android = android + 1
    return android
Mac=detect_mac(objet)
Win=detect_win(objet)
linux=detect_linux(objet)
ios=detect_ios(objet)
android=detect_android(objet)
print("Mac: "+str(Mac))
print("Windows: "+str(Win))
print("Linux: "+str(linux))
print("IOS: "+str(ios))
print("Android: "+str(android))
