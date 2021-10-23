import json,re,argparse,os
#Creer le parser
my_parser = argparse.ArgumentParser(description='Prendre un fichier de format apche et le transforme en format json')

#Ajouter des arguments
my_parser.add_argument('Path_Fichier_Apache', metavar='fic_apache', type=str, help='le fichier apache our convertir en format json')
my_parser.add_argument('Fichier_Json', metavar='fic_json', type=str, help='le nom de fichier json')

#Executer le parse_args() methode
args = my_parser.parse_args()
input_pathficapache = args.Path_Fichier_Apache
input_ficjson = args.Fichier_Json

if not os.path.isfile(input_pathficapache):
    print('Le chemin pour le fichier apache ne existe pas')
    sys.exit()

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
            pattern = '([^ ]+).+\[(.*)\] .+(GET[^"]+|HEAD[^"]+|POST[^"]+|OPTION[^"]+)" ([0-9]+|\-) ([0-9]+|\-) "(http[^"]+|\-)"."(.*)"'
            param = re.search(pattern, l)
            if param:
                dictionnaire['remote_ip'] = param.group(1)
                dictionnaire['time'] = param.group(2)
                dictionnaire['request'] = param.group(3)
                dictionnaire['response'] = param.group(4)
                dictionnaire['bytes'] = param.group(5)
                dictionnaire['referrer'] = param.group(6)
                dictionnaire['system_agent'] = param.group(7)
                objet.append(dictionnaire)
            else:
                erreur.append(l)
    jsonfile = open(input_ficjson, "w")
    json.dump(objet, jsonfile, indent=4, sort_keys=False)
    jsonfile.close()
    return objet

lireficlog(input_pathficapache)
print('Ligne où il y a une erreur:')
print(erreur)
