# WordPress + MySQL + phpMyAdmin avec Docker Compose

Ce projet fournit un environnement complet pour lancer **WordPress**, **MySQL** et **phpMyAdmin** à l’aide de **Docker Compose**.

---

## Services

- **WordPress**  
  - Image : `wordpress:latest`  
  - URL : [http://localhost:8080](http://localhost:8080)  
  - Documentation : [hub.docker.com/_/wordpress](https://hub.docker.com/_/wordpress)

- **MySQL**  
  - Image : `mysql:8.0`  
  - Port : `3306` (accessible en local, non exposé publiquement en prod)  
  - Documentation : [hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)

- **phpMyAdmin**  
  - Image : `phpmyadmin/phpmyadmin`  
  - URL : [http://localhost:8081](http://localhost:8081)  
  - Documentation : [hub.docker.com/_/phpmyadmin](https://hub.docker.com/_/phpmyadmin)

---

## Démarrage

Cloner le repo et se placer à la racine du projet.

Vérifier les fichiers .env dans chaque sous-dossier (cf Configuration).

Lancer les conteneurs : `docker compose up -d`  
Vérifier l’état des services : `docker compose ps`

Utilisation

- Accéder à WordPress : http://localhost:8080
- Accéder à phpMyAdmin : http://localhost:8081

Arrêter et nettoyer : `docker compose down -v`

---

## Configuration

Afin de configurer, les variables d'environnement, on retrouve un fichier .env par container :
```
│── docker-compose.yml
│── wordpress/
│   └── .env
│── mysql/
│   └── .env
│── phpmyadmin/
│   └── .env
```

🔹 Exemple de contenu des .env

wordpress/.env
```
WORDPRESS_DB_HOST=mysql
WORDPRESS_DB_USER=wordpress
WORDPRESS_DB_PASSWORD=wordpress
WORDPRESS_DB_NAME=wordpress
```

mysql/.env
```
MYSQL_DATABASE=wordpress
MYSQL_USER=wordpress
MYSQL_PASSWORD=wordpress
MYSQL_ROOT_PASSWORD=rootpass
```

phpmyadmin/.env
```
PMA_HOST=mysql
PMA_USER=wordpress
PMA_PASSWORD=wordpress
```
