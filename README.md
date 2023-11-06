# Projet 10

API-SoftDesk est une API RESTful permettant de remonter et suivre des problèmes 
techniques pour les trois plateformes (site web, applications Android et iOS).

L'application permet aux utilisateurs de créer divers projets, 
d'ajouter des utilisateurs (contributeurs) à des projets spécifiques, 
de créer des problèmes au sein des projets et d'attribuer des libellés 
à ces problèmes en fonction de leurs priorités, de balises, etc.

Pour plus de détails sur le fonctionnement de cette API, se référer à sa 
[documentation](https://documenter.getpostman.com/view/29787301/2s9YXfc47N) (Postman).


## Initialisation du projet

### Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.
###### • Récupération du projet

```
git clone https://github.com/samichelly/P10__API-Rest_SoftDesk.git
```

###### • Activer l'environnement virtuel

```
cd P10__API-Rest_SoftDesk 
python -m venv env 
env\Scripts\activate
```

###### • Installer les paquets requis

```
pip install -r requirements.txt
```


### MacOS et Linux :
Dans le terminal, naviguer vers le dossier souhaité.
###### • Récupération du projet
```
git clone https://github.com/samichelly/P10__API-Rest_SoftDesk.git
```

###### • Activer l'environnement virtuel
```
cd P10__API-Rest_SoftDesk 
python3 -m venv env 
source env/bin/activate
```

###### • Installer les paquets requis
```
pip install -r requirements.txt
```

## Utilisation

#### Faire les migrations (si nécessaire) :

```
python manage.py migrate
```

#### Lancer le serveur Django :

```
python manage.py runserver
```

Il est possible de naviguer dans l'API avec différents outils :

- la plateforme [Postman](https://www.postman.com/) ;
- l'interface intégrée Django REST framework à l'adresse http://127.0.0.1:8000/ (adresse par défaut, cf. documentation pour les points de terminaisons).

## Informations

#### Liste des utilisateurs existants :

| *ID* | *Identifiant* | *Mot de passe* |
|------|---------------|----------------|
| 2    | user_1        | password890    |
| 3    | user_2        | password890    |
| 4    | New_user_test | password890    |
| 10   | user_10       | password890    |
