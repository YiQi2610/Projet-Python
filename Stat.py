import re,json,argparse,os,sys
#Creer le parser
my_parser = argparse.ArgumentParser(description='Prendre un fichier json et analyse pour afficher les statistiques')

#Ajouter des arguments
my_parser.add_argument('Path_Fichier_Json', metavar='fic_json', type=str, help='le chemin de fichier json')

#Executer le parse_args() methode
args = my_parser.parse_args()
input_pathficjson = args.Path_Fichier_Json

if not os.path.isfile(input_pathficjson):
    print('Le chemin pour le fichier json ne existe pas')
    sys.exit()
    
with open(input_pathficjson) as json_file:
    objet=json.load(json_file)
def detect_mac(log):
    mac = 0
    for l in log:
        if 'Mac' in l['system_agent']:          # recherche mac OS dans notre liste
            mac = mac + 1
    return mac
def detect_win(log):
    win = 0
    for l in log:
        if 'Windows' in l['system_agent']:  # recherche windows dans notre liste
            win = win + 1
    return win
def detect_linux(log):
    linux = 0
    for l in log:
        if 'Linux' in l['system_agent']:  # recherche linux dans notre liste
            linux = linux + 1
    return linux
def detect_ios(log):
    ios = 0
    for l in log:
        if 'iPhone' in l['system_agent']:  # recherche ios dans notre liste
            ios = ios + 1
    return ios
def detect_android(log):
    android = 0
    for l in log:
        if 'Android' in l['system_agent']:  # recherche android dans notre liste
            android = android + 1
    return android
def detect_chrome(log):
    chrome = 0
    for l in log:
        if 'Chrome' in l['system_agent']:  # recherche Chrome dans notre liste
            chrome = chrome + 1
    return chrome
def detect_safari(log):
    safari = 0
    for l in log:
        if 'Safari' in l['system_agent']:  # recherche Safari dans notre liste
            safari = safari + 1
    return safari
def detect_firefox(log):
    firefox = 0
    for l in log:
        if 'Firefox' in l['system_agent']:  # recherche Firefox dans notre liste
            firefox = firefox + 1
    return firefox
def detect_petitfichier(log):
    petitfic = 0
    for l in log:
        if l['bytes'] != '-':
            if int(l['bytes']) <= int(1000):  # recherche de fichier inférieur à 1000o dans notre liste
                petitfic =petitfic + 1
    return petitfic
def detect_moyenfichier(log):
    moyenfic = 0
    for l in log:
        if l['bytes'] != '-':
            if int(l['bytes']) < int(10000) and int(l['bytes']) > int(1000):  # recherche de fichier supérieur à 1000o dans notre liste
                moyenfic = moyenfic + 1
    return moyenfic
def detect_grosfichier(log):
    grosfic = 0
    for l in log:
        if l['bytes'] != '-':
            if int(l['bytes']) < int(100000) and int(l['bytes']) > int(10000):  # recherche de fichier supérieur à 10 000o dans notre liste
                grosfic = grosfic + 1
    return grosfic
def detect_tresgrosfichier(log):
    tresgrosfic = 0
    for l in log:
        if l['bytes'] != '-':
            if int(l['bytes']) >= int(100000):  # recherche de fichier supérieur à 100 000o dans notre liste
                tresgrosfic = tresgrosfic + 1
    return tresgrosfic
def detect_code200(log):
    code200 = 0
    for l in log:
        if '200' in l['response']:  # recherche de 200 dans notre liste
            code200 = code200 + 1
    return code200
def detect_code301(log):
    code301 = 0
    for l in log:
        if '301' in l['response']:  # recherche de 301 dans notre liste
            code301 = code301 + 1
    return code301
def detect_code403(log):
    code403 = 0
    for l in log:
        if '403' in l['response']:  # recherche de 403 dans notre liste
            code403 = code403 + 1
    return code403
def detect_code404(log):
    code404 = 0
    for l in log:
        if '404' in l['response']:  # recherche de 404 dans notre liste
            code404 = code404 + 1
    return code404
def detect_code500(log):
    code500 = 0
    for l in log:
        if '500' in l['response']:  # recherche de 500 dans notre liste
            code500 = code500 + 1
    return code500
def detect_code206(log):
    code206 = 0
    for l in log:
        if '206' in l['response']:  # recherche de 206 dans notre liste
            code206 = code206 + 1
    return code206
def detect_code416(log):
    code416 = 0
    for l in log:
        if '416' in l['response']:  # recherche de 416 dans notre liste
            code416 = code416 + 1
    return code416
def detect_get(log):
    get = 0
    for l in log:
        if 'GET' in l['request']:  # recherche des GET dans notre liste
            get = get + 1
    return get
def detect_post(log):
    post = 0
    for l in log:
        if 'POST' in l['request']:  # recherche des POST dans notre liste
            post = post + 1
    return post
def detect_head(log):
    head = 0
    for l in log:
        if 'HEAD' in l['request']:  # recherche des HEAD dans notre liste
            head = head + 1
    return head
def detect_options(log):
    options = 0
    for l in log:
        if 'OPTIONS' in l['request']:  # recherche des OPTIONS dans notre liste
            options= options + 1
    return options
def detect_heure_travail_matin(log):
    heure_travail_matin = 0
    for l in log:
        part_time=re.search(':([^ ]+)',l['time'])
        part_time2=part_time.group(1)
        part_seconde=sum(x * int(t) for x, t in zip([3600, 60, 1], part_time2.split(":")))#conversion heures et minutes en secondes
        if part_seconde >= 28800 and part_seconde <= 43200:  # recherche heures de 8h à 12h
            heure_travail_matin = heure_travail_matin + 1
    return heure_travail_matin
def detect_heure_travail_aprem(log):
    heure_travail_aprem = 0
    for l in log:
        part_time=re.search(':([^ ]+)',l['time'])
        part_time2=part_time.group(1)
        part_seconde=sum(x * int(t) for x, t in zip([3600, 60, 1], part_time2.split(":")))#conversion heures et minutes en secondes
        if part_seconde >= 43200 and part_seconde <= 61200:  # recherche heures de 12h à 17h
            heure_travail_aprem = heure_travail_aprem + 1
    return heure_travail_aprem
def detect_heure_soir(log):
    heure_soir = 0
    for l in log:
        part_time=re.search(':([^ ]+)',l['time'])
        part_time2=part_time.group(1)
        part_seconde=sum(x * int(t) for x, t in zip([3600, 60, 1], part_time2.split(":")))#conversion heures et minutes en secondes
        if part_seconde >= 61200:  # recherche heures différentes de 17h à 0h
            heure_soir = heure_soir + 1
    return heure_soir
def detect_heure_minuitplus(log):
    heure_minuitplus = 0
    for l in log:
        part_time=re.search(':([^ ]+)',l['time'])
        part_time2=part_time.group(1)
        part_seconde=sum(x * int(t) for x, t in zip([3600, 60, 1], part_time2.split(":")))#conversion heures et minutes en secondes
        if part_seconde <= 28800:  # recherche heures différentes de 0h à 8h
            heure_minuitplus = heure_minuitplus + 1
    return heure_minuitplus
def detect_adr_ip(log):
    listeadrip=[]
    for l in log:
        if l['remote_ip'] not in listeadrip:
            listeadrip.append(l['remote_ip']) #recherche des adresses IP differentes
    return len(listeadrip)
def detect_ipcode403(log):
    liste_ip403=[]
    for l in log:
        if '403' in l['response']:#recherche des adresses IP qui ont le code de réponse 403
            if l['remote_ip'] not in liste_ip403:
                liste_ip403.append(l['remote_ip']) #si l'adresse ip n'existe pas encore dans la liste, il l'ajoute dans la liste
    return liste_ip403
def detect_ipcode404(log):
    dictip404={}
    for l in log :
        if '404' in l['response']:#recherche des adresses IP qui ont le code de réponse 404
            if l['remote_ip'] not in dictip404.keys():
                dictip404[l['remote_ip']] = 1
            else :
                dictip404[l['remote_ip']] = int(dictip404[l['remote_ip']]) + 1
    return dictip404
def detect_ipcode301(log):
    dictip301={}
    for l in log :
        if '301' in l['response']:#recherche des adresses IP qui ont le code de réponse 301
            if l['remote_ip'] not in dictip301.keys():
                dictip301[l['remote_ip']] = 1
            else :
                dictip301[l['remote_ip']] = int(dictip301[l['remote_ip']]) + 1
    return dictip301
def detect_ipcode500(log):
    dictip500={}
    for l in log :
        if '500' in l['response']:#recherche des adresses IP qui ont le code de réponse 500
            if l['remote_ip'] not in dictip500.keys():
                dictip500[l['remote_ip']] = 1
            else :
                dictip500[l['remote_ip']] = int(dictip500[l['remote_ip']]) + 1
    return dictip500
def detect_ipcode206(log):
    dictip206={}
    for l in log :
        if '206' in l['response']:#recherche des adresses IP qui ont le code de réponse 206
            if l['remote_ip'] not in dictip206.keys():
                dictip206[l['remote_ip']] = 1
            else :
                dictip206[l['remote_ip']] = int(dictip206[l['remote_ip']]) + 1
    return dictip206
def detect_ipcode416(log):
    dictip416={}
    for l in log :
        if '416' in l['response']:#recherche des adresses IP qui oont le code de réponse 416
            if l['remote_ip'] not in dictip416.keys():
                dictip416[l['remote_ip']] = 1
            else :
                dictip416[l['remote_ip']] = int(dictip416[l['remote_ip']]) + 1
    return dictip416
def detect_adripfrequent(log):
    dictipfrequent = {}
    for l in log:
            if l['remote_ip'] not in dictipfrequent.keys(): #recherche des adresses IP qui ont envoyé beaucoup de requêtes
                dictipfrequent[l['remote_ip']] = 1
            else:
                dictipfrequent[l['remote_ip']] = int(dictipfrequent[l['remote_ip']]) + 1
    return dictipfrequent
def detect_jour(log):
    dict_co_jour = {}
    for l in log:
        part_time=re.search('([^:]+)',l['time'])
        part_time2=part_time.group(1)
        if part_time2 not in dict_co_jour.keys(): # recherche des nombre de connexions par jour
            dict_co_jour[part_time2] = 1
        else:
            dict_co_jour[part_time2]=int(dict_co_jour[part_time2]) + 1
    return dict_co_jour

#Utilisation des fonctions
mac=detect_mac(objet)
win=detect_win(objet)
linux=detect_linux(objet)
ios=detect_ios(objet)
android=detect_android(objet)
chrome=detect_chrome(objet)
safari=detect_safari(objet)
firefox=detect_firefox(objet)
petitfichier=detect_petitfichier(objet)
grosfichier=detect_grosfichier(objet)
moyenfichier=detect_moyenfichier(objet)
tresgrosfichier=detect_tresgrosfichier(objet)
code200=detect_code200(objet)
code301=detect_code301(objet)
code403=detect_code403(objet)
code404=detect_code404(objet)
code500=detect_code500(objet)
code416=detect_code416(objet)
code206=detect_code206(objet)
get=detect_get(objet)
post=detect_post(objet)
head=detect_head(objet)
options=detect_options(objet)
co_matin=detect_heure_travail_matin(objet)
co_aprem=detect_heure_travail_aprem(objet)
co_soir=detect_heure_soir(objet)
co_minuitplus=detect_heure_minuitplus(objet)
adrip=detect_adr_ip(objet)
ip403=detect_ipcode403(objet)
ip404=detect_ipcode404(objet)
ip301=detect_ipcode301(objet)
ip416=detect_ipcode416(objet)
ip206=detect_ipcode206(objet)
ip500=detect_ipcode500(objet)
ipfrequent=detect_adripfrequent(objet)
co_jour=detect_jour(objet)

#calcul pourcentage:
percent_minuitplus=(co_minuitplus*100)/(co_matin+co_aprem+co_soir+co_minuitplus)
percent_soir=(co_soir*100)/(co_matin+co_aprem+co_soir+co_minuitplus)
percent_aprem=(co_aprem*100)/(co_matin+co_aprem+co_soir+co_minuitplus)
percent_matin=(co_matin*100)/(co_matin+co_aprem+co_soir+co_minuitplus)
percent_200=(code200*100)/(code200+code301+code403+code404+code206+code416+code500)
percent_301=(code301*100)/(code200+code301+code403+code404+code206+code416+code500)
percent_403=(code403*100)/(code200+code301+code403+code404+code206+code416+code500)
percent_404=(code404*100)/(code200+code301+code403+code404+code206+code416+code500)
percent_206=(code206*100)/(code200+code301+code403+code404+code206+code416+code500)
percent_416=(code416*100)/(code200+code301+code403+code404+code206+code416+code500)
percent_500=(code500*100)/(code200+code301+code403+code404+code206+code416+code500)
percent_mac=(mac*100)/(mac+win+linux)
percent_win=(win*100)/(mac+win+linux)
percent_linux=(linux*100)/(mac+win+linux)
percent_ios=(ios*100)/(ios+android)
percent_android=(android*100)/(ios+android)
percent_pc=((mac+win+linux)*100)/((mac+win+linux)+(ios+android))
percent_mobile=((ios+android)*100)/((mac+win+linux)+(ios+android))
percent_chrome=(chrome*100)/(chrome+firefox+safari)
percent_firefox=(firefox*100)/(chrome+firefox+safari)
percent_safari=(safari*100)/(chrome+firefox+safari)
percent_get=(get*100)/(get+head+post)
percent_post=(post*100)/(get+head+post)
percent_head=(head*100)/(get+head+post)
percent_options=(options*100)/(get+head+post+options)
percent_gros_fic=(grosfichier*100)/(grosfichier+petitfichier+moyenfichier+tresgrosfichier)
percent_petit_fic=(petitfichier*100)/(grosfichier+petitfichier+moyenfichier+tresgrosfichier)
percent_moyen_fic=(moyenfichier*100)/(grosfichier+petitfichier+moyenfichier+tresgrosfichier)
percent_tresgros_fic=(tresgrosfichier*100)/(grosfichier+petitfichier+moyenfichier+tresgrosfichier)
connexion_total=0
for i in co_jour:
    connexion_total=connexion_total+co_jour[i]
    dict_percent_co_jour={}
for i in co_jour:
    dict_percent_co_jour[i]= (co_jour[i] * 100) / connexion_total

#affichage:
print()
print("##################################################################################################")
print()

print("###### Nombre des différents OS PC utilisé ######")
print("mac: "+str(mac)+" "+str(int(percent_mac))+"%")
print("windows: "+str(win)+" "+str(int(percent_win))+"%")
print("Linux: "+str(linux)+" "+str(int(percent_linux))+"%")
print()
print("###### Nombre des différents OS Mobile utilisé ######")
print("IOS: "+str(ios)+" "+str(int(percent_ios))+"%")
print("Android: "+str(android)+" "+str(int(percent_android))+"%")
print()
print("###### Nombre des différents web agent utilisé (pas exacte) ######")
print("Chrome: "+str(chrome)+" "+str(int(percent_chrome))+"%")
print("Safari: "+str(safari)+" "+str(int(percent_safari))+"%")
print("Firefox: "+str(firefox)+" "+str(int(percent_firefox))+"%")
print()
print("###### Taille des paquets transité ######")
print("Petit fichier(<=1000o): "+str(petitfichier)+" "+str(int(percent_petit_fic))+"%")
print("Moyen fichier(>1000o et <10 000o): "+str(moyenfichier)+" "+str(int(percent_moyen_fic))+"%")
print("Gros fichier(>10 000o et <100 000o): "+str(grosfichier)+" "+str(int(percent_gros_fic))+"%")
print("Très gros fichier(>=100 000o): "+str(tresgrosfichier)+" "+str(int(percent_tresgros_fic))+"%")
print()
print("###### Nombre de code d'erreur et de succés ######")
print("Code 200: "+str(code200)+" "+str(int(percent_200))+"%")
print("Code 301: "+str(code301)+" "+str(int(percent_301))+"%")
print("Code 403: "+str(code403)+" "+str(int(percent_403))+"%")
print("Code 404: "+str(code404)+" "+str(int(percent_404))+"%")
print("Code 416: "+str(code416)+" "+str(int(percent_416))+"%")
print("Code 500: "+str(code500)+" "+str(int(percent_500))+"%")
print("Code 206: "+str(code206)+" "+str(int(percent_206))+"%")
print()
print("###### Nombre d'en-tête HTML rencontré ######")
print("Nombre de GET: "+str(get)+" "+str(int(percent_get))+"%")
print("Nombre de POST: "+str(post)+" "+str(int(percent_post))+"%")
print("Nombre de HEAD: "+str(head)+" "+str(int(percent_head))+"%")
print("Nombre de Options: "+str(options)+" "+str(int(percent_options))+"%")
print()
print("###### Nombre de connexion par plage horaire ######")
print("Connexion de 8H à 12H:  "+str(co_matin)+" "+str(int(percent_matin))+"%")
print("Connexion de 12H à 17H: "+str(co_aprem)+" "+str(int(percent_aprem))+"%")
print("Connexion de 17h à 0h:  "+str(co_soir)+" "+str(int(percent_soir))+"%")
print("Connexion de 0h à 8h:   "+str(co_minuitplus)+" "+str(int(percent_minuitplus))+"%")
print()
print("Nombre d'IP differentes: "+str(adrip))
print()
print("Connexion par jour: ")
for i in co_jour:
    print(i+" : " + str(co_jour[i]) +' ' + str(int(dict_percent_co_jour[i])) + "%")
print()

print()
print("######################## Adresses IP associée à un code d'erreur ####################################")
print()

print("Les adresses IP qui ont le code de réponse 403 et combien de fois:")
print(ip403)
print()
print("Les adresses IP qui ont le code de réponse 404 et combien de fois:")
print(ip404)
print()
print("Les adresses IP qui ont le code de réponse 301 et combien de fois:")
print(ip301)
print()
print("Les adresses IP qui ont le code de réponse 416 et combien de fois:")
print(ip416)
print()
print("Les adresses IP qui ont le code de réponse 206 et combien de fois:")
print(ip206)
print()
print("Les adresses IP qui ont le code de réponse 500 et combien de fois:")
print(ip500)

print()
print("######################## Adresses IP récurentent #####################################################")
print()

print("Les adresses IP qui ont envoyé des requêtes plus de 100 fois:")
for l in ipfrequent:
    if(ipfrequent[l] > 100):
        print(l + ' : ' + str(ipfrequent[l]) +' fois')

print()
print("######################## Menace potentielle #########################################################")
print()

print("Les adresses IP qui ont le code de réponse 404 plus de 5 fois:")
for l in ip404:
    if(ip404[l] > 5):
        print(l + ' : ' + str(ip404[l]) +' fois')
print()

print("Les adresses IP qui ont le code de réponse 301 plus de 5 fois:")
for l in ip301:
    if(ip301[l] > 5):
        print(l + ' : ' + str(ip301[l]) +' fois')

        
print()
print("######################## Affichage graphique #########################################################")
print()

#affichage graphique
print("Nombre de connexion par rapport à l'heure en %: ")
print("8h-12H:     ["+int(percent_matin)*"*"+"]"+" "+str(int(percent_matin))+"%")
print("12h-17h:    ["+int(percent_aprem)*"*"+"]"+" "+str(int(percent_aprem))+"%")
print("17h-0h :    ["+int(percent_soir)*"*"+"]"+" "+str(int(percent_soir))+"%")
print("0h-8h :     ["+int(percent_minuitplus)*"*"+"]"+" "+str(int(percent_minuitplus))+"%")
print()

print("Nombre de code d'erreur ou succés en %: ")
print("200:  ["+int(percent_200)*"*"+"]"+" "+str(int(percent_200))+"%")
print("301:  ["+int(percent_301)*"*"+"]"+" "+str(int(percent_301))+"%")
print("403:  ["+int(percent_403)*"*"+"]"+" "+str(int(percent_403))+"%")
print("404:  ["+int(percent_404)*"*"+"]"+" "+str(int(percent_404))+"%")
print("416:  ["+int(percent_416)*"*"+"]"+" "+str(int(percent_416))+"%")
print("500:  ["+int(percent_500)*"*"+"]"+" "+str(int(percent_500))+"%")
print("206:  ["+int(percent_206)*"*"+"]"+" "+str(int(percent_206))+"%")
print()

print("Pourcentage OS PC utilisé: ")
print("Mas OS:   ["+int(percent_mac)*"*"+"]"+" "+str(int(percent_mac))+"%")
print("windows:  ["+int(percent_win)*"*"+"]"+" "+str(int(percent_win))+"%")
print("Linux:    ["+int(percent_linux)*"*"+"]"+" "+str(int(percent_linux))+"%")
print()

print("Pourcentage OS Mobile utilisé: ")
print("IOS:      ["+int(percent_ios)*"*"+"]"+" "+str(int(percent_ios))+"%")
print("Android:  ["+int(percent_android)*"*"+"]"+" "+str(int(percent_android))+"%")
print()

print("Pourcentage équipement utilisé: ")
print("PC:       ["+int(percent_pc)*"*"+"]"+" "+str(int(percent_pc))+"%")
print("Mobile:   ["+int(percent_mobile)*"*"+"]"+" "+str(int(percent_mobile))+"%")
print()

print("Pourcentage navigateur utilisé (pas précis): ")
print("Chrome:   ["+int(percent_chrome)*"*"+"]"+" "+str(int(percent_chrome))+"%")
print("Firefox:  ["+int(percent_firefox)*"*"+"]"+" "+str(int(percent_firefox))+"%")
print("Safari:   ["+int(percent_safari)*"*"+"]"+" "+str(int(percent_safari))+"%")
print()

print("Pourcentage en-tête HTML utilisée: ")
print("GET:      ["+int(percent_get)*"*"+"]"+" "+str(int(percent_get))+"%")
print("POST:     ["+int(percent_post)*"*"+"]"+" "+str(int(percent_post))+"%")
print("HEAD:     ["+int(percent_head)*"*"+"]"+" "+str(int(percent_head))+"%")
print("OPTIONS:  ["+int(percent_options)*"*"+"]"+" "+str(int(percent_options))+"%")
print()

print("Pourcentage taille de fichier utilisée: ")
print("Petit fichier (<=1000o):              ["+int(percent_petit_fic)*"*"+"]"+" "+str(int(percent_petit_fic))+"%")
print("Moyen fichier (>1000o & <10 000o):    ["+int(percent_moyen_fic)*"*"+"]"+" "+str(int(percent_moyen_fic))+"%")
print("Gros fichier (>10 000o & <100 000o):  ["+int(percent_gros_fic)*"*"+"]"+" "+str(int(percent_gros_fic))+"%")
print("Très gros fichier (>=100 000o):       ["+int(percent_tresgros_fic)*"*"+"]"+" "+str(int(percent_tresgros_fic))+"%")
print()

print("Nombre de connexions par jour: ")
for i in co_jour:
    print(i+" : [" + int(dict_percent_co_jour[i]) * "*" + "]" + " " + str(int(dict_percent_co_jour[i])) + "%")
