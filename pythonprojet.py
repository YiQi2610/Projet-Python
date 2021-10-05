import re
#Lire le fichier log et recuperer toutes les lignes dans une liste:
def lireficlog(fic_log):
    with open(fic_log, 'r') as ficlog:
        global objet
        objet = []
        for l in ficlog:
            objet.append(l)
    print("Objet:")
    print(objet)
lireficlog("apache_logspetit")

#Chercher les adresses ip:
def chercher_ip(listeobjet):
    j=0
    remote_ip = []
    for l in listeobjet:
        element=l
        dict_remoteip={}
        remote_ip.append(dict_remoteip)
        dict_remoteip['Objet'+str(j+1)] = re.findall('^[^ ]+', element)
        j=j+1
    print("Remote IP:")
    print(remote_ip)

chercher_ip(objet)


#Chercher les timestamps:
def chercher_timestamp(listeobjet):
    j = 0
    timestamp = []
    for l in listeobjet:
        element = l
        dict_timestamp = {}
        timestamp.append(dict_timestamp)
        dict_timestamp['Objet' + str(j + 1)] = re.findall('\[(.*)\]', element)
        j = j + 1
    print("Timestamp:")
    print(timestamp)
chercher_timestamp(objet)

#Chercher les requetes:
def chercher_request(listeobjet):
    j = 0
    request = []
    for l in listeobjet:
        element = l
        dict_request = {}
        request.append(dict_request)
        dict_request['Objet' + str(j + 1)] = re.findall('GET[^"]+', element)
        j = j + 1
    print("Requete:")
    print(request)
chercher_request(objet)

#Chercher les reponses:
def chercher_response(listeobjet):
    j = 0
    response = []
    for l in listeobjet:
        element = l
        dict_response = {}
        response.append(dict_response)
        dict_response['Objet' + str(j + 1)] = re.findall('http[^"]+', element)
        j = j + 1
    print("Reponse:")
    print(response)
chercher_response(objet)

#Chercher les code de reponse:
def chercher_answercode(listeobjet):
    j = 0
    answercode = []
    for l in listeobjet:
        element = l
        dict_answercode = {}
        answercode.append(dict_answercode)
        dict_answercode['Objet' + str(j + 1)] = re.findall('" ([0-9]+)', element)
        j = j + 1
    print("Code de reponse:")
    print(answercode)
chercher_answercode(objet)

#Chercher la taille d'octet:
def chercher_taille(listeobjet):
    j = 0
    taille = []
    for l in listeobjet:
        element = l
        dict_taille = {}
        taille.append(dict_taille)
        dict_taille['Objet' + str(j + 1)] = re.findall(' ([0-9]+) "', element)
        j = j + 1
    print("Taille d'octet:")
    print(taille)
chercher_taille(objet)

#Chercher le system d'argent:
def chercher_sys_agent(listeobjet):
    j = 0
    sys_agent = []
    for l in listeobjet:
        element = l
        dict_sys_agent = {}
        sys_agent.append(dict_sys_agent)
        dict_sys_agent['Objet' + str(j + 1)] = re.findall('" "(.*)', element)
        j = j + 1
    print("Systeme d'agent:")
    print(sys_agent)
chercher_sys_agent(objet)

