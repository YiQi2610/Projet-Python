def lireficlog(fic_log):
    with open(fic_log, 'r') as ficlog:
        import re
        objet = []
        i = 0
        for l in ficlog:
            dictionnaire= {}
            objet.append(dictionnaire)
            dictionnaire['remote_ip'] = re.findall('^[^ ]+', l)
            dictionnaire['timestamp'] = re.findall('\[.*\]',l)
            dictionnaire['request'] = re.findall('GET[^"]+', l)
            dictionnaire['answer'] = re.findall('http[^"]+', l)
            dictionnaire['answercode'] = re.findall('" [^ ]+', l)
            dictionnaire['systagent'] = re.findall('[^"]+$', l)
            print(dictionnaire)


lireficlog("apache_logspetit")
