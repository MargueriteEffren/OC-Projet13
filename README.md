## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Prérequis

- Compte CircleCI
- Compte DockerHub
- Docker: pour Windows: `https://docs.docker.com/desktop/install/windows-install/`

pour Mac : `https://docs.docker.com/desktop/install/mac-install/`
- Compte Heroku
- Heroku CLI
- Compte Sentry

### Description

Le travail de déploiement consiste en la mise en place d'une Intégration continue/Déploiement continu (CI/CD) suivant 3 étapes :
- run de tests du code via Pytest et Flake8,
- Conteneurisation du code, des fichiers de configuration, du fichier requirements.txt, dans une image Docker
- Déploiement de l'application sur Heroku en utilisant l'image Docker

Une fois déployée, l'application est surveillée grâce à Sentry:
`https://www.youtube.com/watch?v=4RCKQejULbw`

### Workflow

Cette CI/CD est mise en place grâce à CircleCI, dans le fichier spécifique config.yml, dont le workflow est :

```workflows:
  sample: 
    jobs:
      - build-and-test
      - containerize:
          requires:
            - build-and-test
          filters:
            branches:
              only: master
      - heroku_deploy:
         requires:
         - containerize
         filters:
           branches:
             only: master
```

Selon ce workflow:
- le code est testé à chaque push sur github, quelle que soit la branche du repository sur laquelle on travaille
- l'image Docker est créée uniquement lors des pushs sur la branche master, si et seulement si les tests sont au préalable validés
- les déploiements vers Heroku n'ont lieu que lors des pushs sur la branche master, si et seulement si les tests sont validés, si et seulement si la conteneurisation Docker a été correctement réalisée

### Workflow

Vu que l'application sera mise en production, il faut définir des variables d'environnement afin de la sécuriser.

- dans CircleCI: 

DOCKER_USERNAME: Nom d'utilisateur du compte Docker

DOCKER_PASSWORD: Mot de passe du compte Docker

HEROKU_API_KEY: clé API du compte Heroku

HEROKU_OC_LETTINGS: Nom de l'application dans Heroku

- dans Heroku:

SENTRY_DNS: DSN de Sentry


