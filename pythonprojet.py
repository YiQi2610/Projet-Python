import re
#Lire le fichier log, séparer toutes les informations pour chque objet et les mettre dans une liste objet:
def lireficlog(fic_log):
    with open(fic_log, 'r') as ficlog:
        global objet
        objet = []
        i=0
        for l in ficlog:
            dictionnaire={}
            objet.append(dictionnaire)
            dictionnaire['remote_ip'] = re.findall('^[^ ]+', l)
            dictionnaire['time'] = re.findall('\[(.*)\]', l)
            dictionnaire['request'] = re.findall('GET[^"]+', l)
            dictionnaire['referrer'] = re.findall('http[^"]+', l)
            dictionnaire['response'] = re.findall('" ([0-9]+)', l)
            dictionnaire['bytes'] = re.findall(' ([0-9]+) "', l)
            dictionnaire['system_agent'] = re.findall('" "(.*)', l)

    return objet
lireficlog("apache_logs")
print(objet)

