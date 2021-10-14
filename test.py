import re
#Lire le fichier log, séparer toutes les informations pour chaque objet et les mettre dans une liste objet:
def lireficlog(fic_log):
    with open(fic_log, 'r') as ficlog:
        global objet
        objet = []
        i=0
        for l in ficlog:
            dictionnaire={}
            objet.append(dictionnaire)
            pattern='(^[^ ]+).+\[(.*)\] .+(GET[^"]+)" ([0-9]+) ([0-9]+) "(http[^"]+)"."(.*)"'
            param = re.search(pattern, l)
            print(param)
            dictionnaire['remote_ip'] = param.group(1)
            dictionnaire['time'] = param.group(2)
            dictionnaire['request'] = param.group(3)
            dictionnaire['referrer'] = param.group(4)
            dictionnaire['response'] = param.group(5)
            dictionnaire['bytes'] = param.group(6)
            dictionnaire['system_agent'] = param.group(7)
            return objet
lireficlog("apache_logs")
print(objet)