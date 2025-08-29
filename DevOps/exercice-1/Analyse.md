# Devops - Exercice 1

## 1. Consignes

### **Contexte Entreprise :**

*"Le marketing veut un WordPress pour le blog corporate. J'ai trouvé un docker-compose mais MySQL ne démarre pas et WordPress affiche des erreurs de connexion."*

### **Tâches à accomplir :**

1. Identifier pourquoi MySQL ne démarre pas                               ✅
2. Corriger les problèmes de connexion WordPress ↔ MySQL                  ✅
3. Sécuriser la configuration (mots de passe, réseau)                       .env pour pouvoir communiquer le code ?
4. Tester l'accès à WordPress (port 8080) et PhpMyAdmin (port 8081)       ✅

## 2. Travaux

### Problème détecté

Au lancement : 
  - terminal : RAS les 3 containers sont montés
  - logs : `work-mysql-1` : 

```log 
Database is uninitialized and password option is not specified

You need to specify one of the following as an environment variable:
- MYSQL_ROOT_PASSWORD
- MYSQL_ALLOW_EMPTY_PASSWORD
- MYSQL_RANDOM_ROOT_PASSWORD
```


### Infos utiles

Containers :
- phpmyadmin - phpmyadmin/phpmyadmin - `http://localhost:8081/` [Doc image Docker](https://hub.docker.com/_/mysql)
- wordpress - wordpress:latest -`http://localhost:8080/` [Doc image Docker](https://hub.docker.com/_/wordpress)
- mysql - mysql:8.0 - `http://localhost:3306/` 



### Solution envisagée
- Etape 1 : Il y a déjà des variables définies dans le docker-compose, on y ajoute ces dernières.

- Etape 2 : La doc du Docker hub indique que seul MYSQL_ROOT_PASSWORD semble obligatoire pour notre problème

- Etape 3 : on externalise les variables dans un .env


Résultats :
Pour wordpress : Lancement d'une installation Wordpress -> Semble fonctionner  
Pour phpamind : 3 bdd, 1 vide, deux avec des tables mais vide ?


## 3. Doc envisagée
