from projectpython2 import lireficlog,re,json
lireficlog("apache_logs")
with open('apache_json.json') as json_file:
    objet=json.load(json_file)
def detect_mac(log):
    mac = 0
    for l in log:
        if 'Mac' in l['system_agent']:          # recherche Mac OS dans notre liste
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
            if int(l['bytes']) >= int(10000):  # recherche de fichier supérieur à 10 000o dans notre liste
                grosfic = grosfic + 1
    return grosfic
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
        if part_seconde >= 28800 and part_seconde < 43200:  # recherche heures de 8h à 11h59
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
def detect_heure_supp(log):
    heure_supp = 0
    for l in log:
        part_time=re.search(':([^ ]+)',l['time'])
        part_time2=part_time.group(1)
        part_seconde=sum(x * int(t) for x, t in zip([3600, 60, 1], part_time2.split(":")))#conversion heures et minutes en secondes
        if part_seconde < 28800 or part_seconde > 61200:  # recherche heures différentes de 8h à 17h
            heure_supp = heure_supp + 1
    return heure_supp
def detect_adr_ip(log):
    listeadrip=[]
    for l in log:
        if l['remote_ip'] not in listeadrip:
            listeadrip.append(l['remote_ip']) #recherche des adresses IP differents
    return len(listeadrip)
def detect_ipcode403(log):
    liste_ip403=[]
    for l in log:
        if '403' in l['response']:#recherche des adresses IP qui a de code réponse 403
            if l['remote_ip'] not in liste_ip403:
                liste_ip403.append(l['remote_ip']) #si l'adresse ip n'existe pas encore dans la liste, il ajoute dans la liste
    return liste_ip403
def detect_ipcode404(log):
    dictip404={}
    for l in log :
        if '404' in l['response']:#recherche des adresses IP qui a de code réponse 404
            if l['remote_ip'] not in dictip404.keys():
                dictip404[l['remote_ip']] = 1
            else :
                dictip404[l['remote_ip']] = int(dictip404[l['remote_ip']]) + 1
    return dictip404
def detect_ipcode301(log):
    dictip301={}
    for l in log :
        if '301' in l['response']:#recherche des adresses IP qui a de code réponse 404
            if l['remote_ip'] not in dictip301.keys():
                dictip301[l['remote_ip']] = 1
            else :
                dictip301[l['remote_ip']] = int(dictip301[l['remote_ip']]) + 1
    return dictip301


#Utilisation des fonctions
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
moyenfichier=detect_moyenfichier(objet)
code200=detect_code200(objet)
code301=detect_code301(objet)
code403=detect_code403(objet)
code404=detect_code404(objet)
get=detect_get(objet)
post=detect_post(objet)
head=detect_head(objet)
options=detect_options(objet)
co_matin=detect_heure_travail_matin(objet)
co_aprem=detect_heure_travail_aprem(objet)
co_hors_travail=detect_heure_supp(objet)
adrip=detect_adr_ip(objet)
ip403=detect_ipcode403(objet)
ip404=detect_ipcode404(objet)
ip301=detect_ipcode301(objet)

#calcul pourcentage:
percent_hors_travail=(co_hors_travail*100)/(co_matin+co_aprem+co_hors_travail)
percent_aprem=(co_aprem*100)/(co_matin+co_aprem+co_hors_travail)
percent_matin=(co_matin*100)/(co_matin+co_aprem+co_hors_travail)
percent_200=(code200*100)/(code200+code301+code403+code404)
percent_301=(code301*100)/(code200+code301+code403+code404)
percent_403=(code403*100)/(code200+code301+code403+code404)
percent_404=(code404*100)/(code200+code301+code403+code404)
percent_Mac=(Mac*100)/(Mac+Win+linux)
percent_Win=(Win*100)/(Mac+Win+linux)
percent_linux=(linux*100)/(Mac+Win+linux)
percent_ios=(ios*100)/(ios+android)
percent_android=(android*100)/(ios+android)
percent_pc=((Mac+Win+linux)*100)/((Mac+Win+linux)+(ios+android))
percent_mobile=((ios+android)*100)/((Mac+Win+linux)+(ios+android))
percent_chrome=(chrome*100)/(chrome+firefox+safari)
percent_firefox=(firefox*100)/(chrome+firefox+safari)
percent_safari=(safari*100)/(chrome+firefox+safari)
percent_get=(get*100)/(get+head+post)
percent_post=(post*100)/(get+head+post)
percent_head=(head*100)/(get+head+post)
percent_options=(options*100)/(get+head+post+options)
percent_gros_fic=(grosfichier*100)/(grosfichier+petitfichier+moyenfichier)
percent_petit_fic=(petitfichier*100)/(grosfichier+petitfichier+moyenfichier)
percent_moyen_fic=(moyenfichier*100)/(grosfichier+petitfichier+moyenfichier)

#affichage:
print()
print("##################################################################################################")
print()

print("Mac: "+str(Mac)+" "+str(int(percent_Mac))+"%")
print("Windows: "+str(Win)+" "+str(int(percent_Win))+"%")
print("Linux: "+str(linux)+" "+str(int(percent_linux))+"%")
print("IOS: "+str(ios)+" "+str(int(percent_ios))+"%")
print("Android: "+str(android)+" "+str(int(percent_android))+"%")
print("Chrome: "+str(chrome)+" "+str(int(percent_chrome))+"%")
print("Safari: "+str(safari)+" "+str(int(percent_safari))+"%")
print("Firefox: "+str(firefox)+" "+str(int(percent_firefox))+"%")
print("Petit fichier(<=1000o): "+str(petitfichier)+" "+str(int(percent_petit_fic))+"%")
print("Moyen fichier(>1000o): "+str(moyenfichier)+" "+str(int(percent_moyen_fic))+"%")
print("Gros fichier(>=10 000o): "+str(grosfichier)+" "+str(int(percent_gros_fic))+"%")
print("Code 200: "+str(code200)+" "+str(int(percent_200))+"%")
print("Code 301: "+str(code301)+" "+str(int(percent_301))+"%")
print("Code 403: "+str(code403)+" "+str(int(percent_403))+"%")
print("Code 404: "+str(code404)+" "+str(int(percent_404))+"%")
print("Nombre de GET: "+str(get)+" "+str(int(percent_get))+"%")
print("Nombre de POST: "+str(post)+" "+str(int(percent_post))+"%")
print("Nombre de HEAD: "+str(head)+" "+str(int(percent_head))+"%")
print("Nombre de Options: "+str(options)+" "+str(int(percent_options))+"%")
print("Connexion de 8H à 11H59: "+str(co_matin)+" "+str(int(percent_matin))+"%")
print("Connexion de 12H à 17H: "+str(co_aprem)+" "+str(int(percent_aprem))+"%")
print("Connexion autres que de 12H à 17H: "+str(co_hors_travail)+" "+str(int(percent_hors_travail))+"%")
print("Nombre d'IP differents: "+str(adrip))
print("Les adresse IP qui a de code réponse 403:")
print(ip403)
print("Les adresse IP qui a de code réponse 404:")
print(ip404)
print("Les adresse IP qui a de code réponse 404 plus de 5 fois:")
for l in ip404:
    if(ip404[l] > 5):
        print(l + ' : ' + str(ip404[l]) +' fois')
print("Les adresse IP qui a de code réponse 301:")
print(ip301)
print("Les adresse IP qui a de code réponse 301 plus de 5 fois:")
for l in ip301:
    if(ip301[l] > 5):
        print(l + ' : ' + str(ip301[l]) +' fois')

print()
print("##################################################################################################")
print()

#affichage graphique
print()
print("##################################################################################################")
print()

print("Mac: "+str(Mac)+" "+str(int(percent_Mac))+"%")
print("Windows: "+str(Win)+" "+str(int(percent_Win))+"%")
print("Linux: "+str(linux)+" "+str(int(percent_linux))+"%")
print("IOS: "+str(ios)+" "+str(int(percent_ios))+"%")
print("Android: "+str(android)+" "+str(int(percent_android))+"%")
print("Chrome: "+str(chrome)+" "+str(int(percent_chrome))+"%")
print("Safari: "+str(safari)+" "+str(int(percent_safari))+"%")
print("Firefox: "+str(firefox)+" "+str(int(percent_firefox))+"%")
print("Petit fichier(<=1000o): "+str(petitfichier)+" "+str(int(percent_petit_fic))+"%")
print("Moyen fichier(>1000o): "+str(moyenfichier)+" "+str(int(percent_moyen_fic))+"%")
print("Gros fichier(>=10 000o): "+str(grosfichier)+" "+str(int(percent_gros_fic))+"%")
print("Code 200: "+str(code200)+" "+str(int(percent_200))+"%")
print("Code 301: "+str(code301)+" "+str(int(percent_301))+"%")
print("Code 403: "+str(code403)+" "+str(int(percent_403))+"%")
print("Code 404: "+str(code404)+" "+str(int(percent_404))+"%")
print("Nombre d'IP: "+str(adrip))
print("Nombre de GET: "+str(get)+" "+str(int(percent_get))+"%")
print("Nombre de POST: "+str(post)+" "+str(int(percent_post))+"%")
print("Nombre de HEAD: "+str(head)+" "+str(int(percent_head))+"%")
print("Nombre de Options: "+str(options)+" "+str(int(percent_options))+"%")
print("Connexion de 8H à 11H59: "+str(co_matin)+" "+str(int(percent_matin))+"%")
print("Connexion de 12H à 17H: "+str(co_aprem)+" "+str(int(percent_aprem))+"%")
print("Connexion autres que de 12H à 17H: "+str(co_hors_travail)+" "+str(int(percent_hors_travail))+"%")
print("Nombre d'IP differents: "+str(adrip))

print()
print("##################################################################################################")
print()

#affichage graphique
print("Nombre de connexion par rapport à l'heure en %: ")
print("8h-11h59:     ["+int(percent_matin)*"*"+"]"+" "+str(int(percent_matin))+"%")
print("12h-17h:      ["+int(percent_aprem)*"*"+"]"+" "+str(int(percent_aprem))+"%")
print("Hors 8h-17h : ["+int(percent_hors_travail)*"*"+"]"+" "+str(int(percent_hors_travail))+"%")
print()

print("Nombre de code d'erreur ou succés en %: ")
print("200:  ["+int(percent_200)*"*"+"]"+" "+str(int(percent_200))+"%")
print("301:  ["+int(percent_301)*"*"+"]"+" "+str(int(percent_301))+"%")
print("403:  ["+int(percent_403)*"*"+"]"+" "+str(int(percent_403))+"%")
print("404:  ["+int(percent_404)*"*"+"]"+" "+str(int(percent_404))+"%")
print()

print("Pourcentage OS PC utilisé: ")
print("Mas OS:   ["+int(percent_Mac)*"*"+"]"+" "+str(int(percent_Mac))+"%")
print("Windows:  ["+int(percent_Win)*"*"+"]"+" "+str(int(percent_Win))+"%")
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
print("Petit fichier (<=1000o):    ["+int(percent_petit_fic)*"*"+"]"+" "+str(int(percent_petit_fic))+"%")
print("Moyen fichier (>1000o):     ["+int(percent_moyen_fic)*"*"+"]"+" "+str(int(percent_moyen_fic))+"%")
print("Gros fichier (>=10 000o):   ["+int(percent_gros_fic)*"*"+"]"+" "+str(int(percent_gros_fic))+"%")
print()
