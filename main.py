import json,re,argparse,os,sys
#Creer le parser
my_parser = argparse.ArgumentParser(description='Prendre un fichier au format apache et le transformer en format json')

#Ajouter des arguments
my_parser.add_argument('Path_Fichier_Apache', metavar='fic_apache', type=str, help='le fichier apache pour convertir en format json')
my_parser.add_argument('Fichier_Json', metavar='fic_json', type=str, help='le nom du fichier json')

#Executer le parse_args() methode
args = my_parser.parse_args()
input_pathficapache = args.Path_Fichier_Apache#recuperer le chemin du fichier apache
input_ficjson = args.Fichier_Json#recuperer le nom du fichier json

#Si le chemin n'existe pas, le code n'est pas effectué
if not os.path.isfile(input_pathficapache):
    print('Le chemin pour le fichier apache ne existe pas')
    sys.exit()

#Lire le fichier log, séparer toutes les informations pour chaque objet et les mettre dans une liste:
def lireficlog(fic_log):
    with open(fic_log, 'r') as ficlog:
        global objet
        global erreur
        objet = []
        erreur = []
        i = 0
        nombre_de_ligne=0
        for l in ficlog:#parcourir toutes les lignes du fichier et creer un dictionnaire pour chaque ligne
            dictionnaire = {}
            pattern = '([^ ]+).+\[(.*)\] .+(GET[^"]+|HEAD[^"]+|POST[^"]+|OPTION[^"]+)" ([0-9]+|\-) ([0-9]+|\-) "(http[^"]+|\-)"."(.*)"' #recuperer toutes les informations en utilisant l'expression régulière
            param = re.search(pattern, l)
            if param:#recuperer les données et les mettre dans le dictionnaire
                dictionnaire['remote_ip'] = param.group(1)
                dictionnaire['time'] = param.group(2)
                dictionnaire['request'] = param.group(3)
                dictionnaire['response'] = param.group(4)
                dictionnaire['bytes'] = param.group(5)
                dictionnaire['referrer'] = param.group(6)
                dictionnaire['system_agent'] = param.group(7)
                nombre_de_ligne=nombre_de_ligne+1
                objet.append(dictionnaire)
            else:
                nombre_de_ligne=nombre_de_ligne+1
                dictionnaire_erreur = {}
                dictionnaire_erreur['ligne']=l#si il n'y a pas d'objet qui correspond au pattern, la ligne est ajoutée dans la liste erreur
                dictionnaire_erreur['nombre de ligne']=nombre_de_ligne
                erreur.append(dictionnaire_erreur)
    jsonfile = open(input_ficjson + '.json', "w")
    json.dump(objet, jsonfile, indent=4, sort_keys=False)#mettre notre liste dans un fichier json
    jsonfile.close()

lireficlog(input_pathficapache)
print('Ligne où il y a une erreur:')#afficher la ligne qui correspond pas au pattern
print(erreur)
