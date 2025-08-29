## Remarques générales

Je vois beaucoup de problèmes sur les PK qui sont cruciales.
Pour rappel, elles doivent être dans chaque table, elles doivent être unique de manière stricte.
Pour résoudre le problème, en suivant de bonnes pratiques on pourrait utiliser des uuid pour chaque table
On peut aussi dans certains cas utiliser des champs nécessaires comme l'ISBN dont on sait qu'il sera unique de façon sûre.
J'ai opté pour le choix d'uuid uniforme sur toutes les tables entité.

J'ai parfois changé l'ordre des champs, en essayant de les mettre en ordre d'importance.

J'ai mis pour chaque section du document initial ma vision sur :
- les tables
- les relations
- mon analyse et propositions d'améliorations
  - code couleur sur l'importance des changements/apports: 
    - 🔴 : Critique
    - 🟠 : Moyenne
    - 🟢 : Annexe


## Gestion Ouvrage

### 1. Livre

**Champs** :

- ISBN --- PK
- Titre
- Résumé
- Date de publication
- Langue
- Nombre de pages

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
- nationalité


### Relations

`Editeur` - `Livre` : 1 to Many
- Un livre a un unique éditeur 
- Un éditeur peut éditer plusieurs livres
- Csq : Champ FK `editor_id` dans `Livre`

`Auteur` - `Livre` : Many to Many
- Un livre peut avoir plusieurs auteurs 
- Un auteur peut écrire plusieurs livres (0 si livre enlever des données ?)
- Csq : Table de liaison avec FK des id des deux tables

### Analyse et améliorations

Table `Titre` :
- Modifier PK Titre 🔴
  - impossible (titres similaires)
  - Soit on créé un id, soit le ISBN peut fonctionner. 
- Champs manquant :
  - Créer ISBN                 🔴
  - Créer Nombre de pages      🟢
- Relation erronée avec Editeur 🔴
  - coté éditeur, il peut avoir plusieurs livres

Table `Editeur`

- La raison sociale n'est pas une bonne PK    🔴
- Création d'un id, ou code éditeur comme PK  🔴
- Préciser les champs coordonnées             🟠

Table `Auteur`

- Modifier PK                                  🔴
  - Nom impossible, nom similaire.
  - De même on devrait créer un id.


TODO : Table Catégorie ? Non mentionné pour le moment  
TODO : Table Exemplaire ? Non mentionné pour le moment  

## Gestion des exemplaires

### Exemplaires

**Champs**
- code barre PK
- état (NE, BO, US, RE)
- date acquisition
- prix

### Emplacements

Champs
 - uuid PK
 - étage
 - section

### Relations
`Livre` - `Exemplaire` : 1 to Many
 - un exemplaire correspond à un seul livre
 - un livre possède de 0 à plusieurs exemplaires

`Exemplaire` - `Emplacement` : 1 to Many
 - un emplacement peut accueillir de 0 à plusieurs exemplaires
 - un exemplaire ne peut être qu'à un emplacement

### Analyse et améliorations

- 🔴 Ajouter PK dans `Exemplaire`
- 🔴 Ajouter Code barre
- 🔴 Modifier la liaison `Livre` - `Exemplaire`
  - 0 à plusieurs coté `Exemplaire`
- 🔴 Modifier la liaison `Exemplaire` - `Emplacement`
  - unique coté `Emplacement`



