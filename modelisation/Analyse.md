## Gestion Ouvrage

### 1. Livre

**Champs** :

- ISBN --- PK
- Titre
- Résumé
- Date de publication
- Langue
- Nombre de pages

**Relations**

- Avec Editeur, un livre a un unique éditeur mais chaque éditeurs peut avoir plusieurs livres


### 2. Editeur

**Champs**

- Code éditeur ---- PK
- Raisons sociale
- Adresse
- Mail (déduit)
- Téléphone (déduit)


### 3. Auteur

**Champs**
- Code auteur ---- PK
- nom
- prénom
- nationnalité


### Analyse et améliorations

Table Titre :
- PK Titre, impossible (titres similaires). Soit on créé un id, soit le ISBN peut fonctionner. (critique)
- Champs manquant :
  - ISBN                 (Critique)
  - Nombre de pages      (annexe)
- Relation erronée avec Editeur, coté éditeur, il peut avoir plusieurs livres

Table Editeur

- La raison sociale n'est pas une bonne PK (Critique)
- Création d'un id, ou code éditeur comme PK (Critique)
- Préciser les champs coordonnées (moyenne)

Table Auteur

- PK Nom impossible, nom similaire. De même on devrait créer un id.


TODO : Table Catégorie ? Non mentionné pour le moment
TODO : Table Exemplaire ? Non mentionné pour le moment
#### Gestion des exemplaires

