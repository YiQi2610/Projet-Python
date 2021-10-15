import json
import re
#Lire le fichier log, séparer toutes les informations pour chaque objet et les mettre dans une liste objet:
def lireficlog(fic_log):
    with open(fic_log, 'r') as ficlog:
        global objet
        global erreur
        objet = []
        erreur = []
        i = 0
        for l in ficlog:
            dictionnaire = {}
            pattern = '([^ ]+).+\[(.*)\] .+(GET[^"]+|HEAD[^"]+||POST[^"]+)" ([0-9]+|\-) ([0-9]+|\-) "(http[^"]+|\-)"."(.*)"'
            param = re.search(pattern, l)
            if param:
                dictionnaire['remote_ip'] = param.group(1)
                dictionnaire['time'] = param.group(2)
                dictionnaire['request'] = param.group(3)
                dictionnaire['referrer'] = param.group(4)
                dictionnaire['response'] = param.group(5)
                dictionnaire['bytes'] = param.group(6)
                dictionnaire['system_agent'] = param.group(7)
                objet.append(dictionnaire)
            else:
                erreur.append(l)
    jsonfile = open("apache_json.json", "w")
    json.dump(objet, jsonfile, indent=4, sort_keys=False)
    jsonfile.close()
    return objet

lireficlog("apache_logs")
print('Ligne où il y a une erreur:')
print(erreur)
