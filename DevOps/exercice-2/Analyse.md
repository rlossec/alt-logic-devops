# Devops - Exercice 2

## Consignes

### **Contexte Entreprise :**

*"L'équipe veut un Nextcloud pour partager des fichiers en interne. J'ai suivi un tuto mais ça affiche 'Internal Server Error' et la base de données semble pas accessible."*

### **Tâches à accomplir :**

1. Identifier pourquoi Nextcloud affiche "Internal Server Error"
2. Intégrer Redis comme cache pour Nextcloud
3. Mettre en place les health checks appropriés
4. Tester l'accès à Nextcloud et la création d'un utilisateur admin

## Travaux

Les trois containers se lancent normalement
Aucun message d'erreur dans les logs, mais un hint : `Hint: You can specify NEXTCLOUD_ADMIN_USER and NEXTCLOUD_ADMIN_PASSWORD ...`

Yml : Le nom des variable d'environnement de Nextcloud sont similaires à celle de postgres ?

Doc des DockerHub :
- [NextCloud](https://hub.docker.com/_/nextcloud/)
- [Postgres](https://hub.docker.com/_/postgres)

NextCloud pour PostgreSQL:
```
POSTGRES_DB Name of the database using postgres.
POSTGRES_USER Username for the database using postgres.
POSTGRES_PASSWORD Password for the database user using postgres.
POSTGRES_HOST Hostname of the database server using postgres.
```

Probable inversion des variables entre postgres et NextCloud ?

Vérifications :
Mais j'ignore ou est le message d'erreur donc ?

Allons voir la doc Redis pour relier le cache :
- [Redis](https://hub.docker.com/_/redis)