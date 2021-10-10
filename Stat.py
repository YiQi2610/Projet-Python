import re

from pythonprojet import lireficlog
objet=lireficlog("apache_logs")
def detect_mac(log):
    mac = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'Mac' in part:          # recherche Mac OS dans notre liste
            mac = mac + 1
    return mac
def detect_win(log):
    win = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'Windows' in part:  # recherche windows dans notre liste
            win = win + 1
    return win
def detect_linux(log):
    linux = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'Linux' in part:  # recherche linux dans notre liste
            linux = linux + 1
    return linux
def detect_ios(log):
    ios = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'iPhone' in part:  # recherche ios dans notre liste
            ios = ios + 1
    return ios
def detect_android(log):
    android = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'Android' in part:  # recherche android dans notre liste
            android = android + 1
    return android
def detect_chrome(log):
    chrome = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'Chrome' in part:  # recherche Chrome dans notre liste
            chrome = chrome + 1
    return chrome
def detect_safari(log):
    safari = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'Safari' in part:  # recherche Safari dans notre liste
            safari = safari + 1
    return safari
def detect_firefox(log):
    firefox = 0
    for l in log:
        part = "".join(l['system_agent'])      #transformation liste en string
        if 'Firefox' in part:  # recherche Firefox dans notre liste
            firefox = firefox + 1
    return firefox
def detect_petitfichier(log):
    petitfic = 0
    for l in log:
        part = "".join(l['bytes'])      #transformation liste en string
        if int(part) < 1000:  # recherche de fichier inférieur à 1000 dans notre liste
            petitfic =petitfic + 1
    return petitfic
def detect_grosfichier(log):
    grosfic = 0
    for l in log:
        part = "".join(l['bytes'])      #transformation liste en string
        print(part)
        if int(part) > 1000:  # recherche de fichier supérieur à 1000 dans notre liste
            grosfic = grosfic + 1
    return grosfic
def detect_code200(log):
    code200 = 0
    for l in log:
        part = "".join(l['response'])      #transformation liste en string
        if '200' in part:  # recherche de 200 dans notre liste
            code200 = code200 + 1
    return code200
def detect_code301(log):
    code301 = 0
    for l in log:
        part = "".join(l['response'])      #transformation liste en string
        if '301' in part:  # recherche de 301 dans notre liste
            code301 = code301 + 1
    return code301
def detect_code404(log):
    code404 = 0
    for l in log:
        part = "".join(l['response'])      #transformation liste en string
        if '404' in part:  # recherche de 404 dans notre liste
            code404 = code404 + 1
    return code404
def detect_ip(log):
    ip = 0
    for l in log:
        part = "".join(l['remote_ip'])      #transformation liste en string
        if l['remote_ip'] != part:  # recherche des IP dans notre liste
            ip = ip + 1
    return ip
def detect_get(log):
    get = 0
    for l in log:
        part = "".join(l['request'])      #transformation liste en string
        if 'GET' in part:  # recherche des GET dans notre liste
            get = get + 1
    return get
def detect_heure_travail(log): #pas fini /!\
    heure_travail = 0
    for l in log:
        part = "".join(l['request'])      #transformation liste en string
        if '08:00:00' in part:  # recherche des heures de travail dans notre liste
            heure_travail = heure_travail + 1
    return heure_travail

Mac=detect_mac(objet)
Win=detect_win(objet)
linux=detect_linux(objet)
ios=detect_ios(objet)
android=detect_android(objet)
chrome=detect_chrome(objet)
safari=detect_safari(objet)
firefox=detect_firefox(objet)
petitfichier=detect_petitfichier(objet)
grosfichier=detect_grosfichier(objet)
code200=detect_grosfichier(objet)
code301=detect_grosfichier(objet)
code404=detect_grosfichier(objet)
ip=detect_ip(objet)
get=detect_get(objet)

print("Mac: "+str(Mac))
print("Windows: "+str(Win))
print("Linux: "+str(linux))
print("IOS: "+str(ios))
print("Android: "+str(android))
print("Chrome: "+str(chrome))
print("Safari: "+str(safari))
print("Firefox: "+str(firefox))
print("Petit fichier: "+str(petitfichier))
print("Gros fichier: "+str(grosfichier))
print("Code 200: "+str(code200))
print("Code 301: "+str(code301))
print("Code 404: "+str(code404))
print("Nombre d'IP: "+str(ip))
print("Nombre de GET: "+str(get))
