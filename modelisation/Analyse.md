## Tables

Un livre est identifié par son ISBN et caractérisé par son titre, son résumé, sa date de publication, sa langue et son nombre de pages. Chaque livre est publié par un unique éditeur, identifié par son code éditeur et possédant une raison sociale, une adresse et des coordonnées de contact. Un livre peut être écrit par plusieurs auteurs, et un auteur (identifié par un code auteur) peut avoir écrit plusieurs livres. Pour chaque auteur, on conserve son nom, son prénom et sa nationalité.

#### 1. Livre

**Champs** :

- ISBN
- Titre
- Résumé
- Date de publication
- Langue
- Nombre de pages

**Relations**

- Avec Editeur, un livre a un unique éditeur mais chaque éditeurs peut avoir plusieurs livres

- **Analyse et améliorations**:

- PK Titre, impossible. Soit on créé un id, soit le ISBN peut fonctionner.
- Champs manquant :
  - ISBN (crucial)
  - Nombre de pages (annexe)
- Relation erronée avec Editeur, coté éditeur, il peut avoir plusieurs livres

#### 2. Editeur

**Champs**

- Code éditeur
- Raisons sociale
- Adresse
- Mail
- Téléphone ...
