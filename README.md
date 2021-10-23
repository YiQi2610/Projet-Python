# Projet-Python 
## Description 
* `main.py`: Lit un fichier de log au format apache et le convertir au format json.
* `Stat.py`: Détermine les données qui peuvent être intéressantes d’un point de vue commercial et d’un point de vue sécurité et fait des statistiques.
## Environnement
* Développement et test effectuée sur Linux, pas d'installation de bibliothèque externe.
* Python 3.7
* Mettre le fichier Apache dans le même dossier que le script 
## Installation
 1. Dans `main.py`, mettre le nom du fichier Apache dans: lireficlog("")
 2. Exécuter `main.py` 
 3. Exécuter `Stat.py` 

 Vous verrez dans la console python vos statistiques :)
## Requête 
```apache
83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
```
## Résultat json
```json
    {
        "remote_ip": "83.149.9.216",
        "time": "17/May/2015:10:05:03 +0000",
        "request": "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1",
        "response": "200",
        "bytes": "203023",
        "referrer": "http://semicomplete.com/presentations/logstash-monitorama-2013/",
        "system_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
    },

```
## Les Principales Statistiques
* Plage horaire de connexion
* Le nombre de requête fructueuse et les différents code erreurs
* Le pourcentage de system d'exploitation mobile ou fixe  
* Le pourcentage des différentes tailles de paquets
* Eventuelle adressse ip malvrillante
## Développeurs
* Tung Ker Chee
* Moreau Matthew

## Contact
Si vous rencontrez des problèmes:
* matthew.moreau@etu.univ-cotedazur.fr
* ker-chee.tung@etu.univ-cotedazur.fr
