# Charity_Data_Management_Interface

## 🎯 Description

Ce projet a été développé dans le cadre du programme **PACTE** (Projet d’Apprentissage à la Communication et au Travail en Équipe), visant à renforcer les compétences techniques et collaboratives des étudiants au sein de la préstigieuse école d'ingénieurs 'SUP'COM'.

L’**interface Charity_Data_Management_Interface** a été conçue pour faciliter la **gestion des données liées aux initiatives caritatives** (Données des personnes en situation de précarité).

## 👥 Équipe

- Projet réalisé par l’équipe **n°20 - Heart Warming**
- Créé pour répondre aux besoins de l’organisation locale **JCI Rafraf** (Junior Chamber International - Rafraf)
- Contexte : Projet PACTE 13ème édition en assurant un impact durable. 

## 🛠️ Technologies utilisées

- **Frontend** : HTML, CSS, JavaScript  
- **Backend** : Python (Flask)  
- **Base de données** : SQLite  

## 💡 Objectifs du projet

- Optimiser la gestion des données liées aux actions caritatives
- Créer une solution numérique réutilisable pour de futures initiatives

## 🔍 Fonctionnalités principales

- Consultation, insertion, modification et suppression des données
- Interface simple et intuitive adaptée aux besoins d’associations

## 🔄 Perspectives d'évolution

- Partage de l’interface entre plusieurs organisations locales de la région pour assurer une collaboration bénéfique

## 📝 Remarques

Ce projet représente un premier pas vers la **numérisation des opérations caritatives locales** et témoigne de l'engagement des étudiants à répondre à des besoins concrets par la technologie.
Ce projet est un prototype pouvant être adapté en fonction des besoins spécifiques de chaque organisation.


## ⚙️ Installation et mise en route

### 1. Cloner le dépôt

1.  Ouvrez l'interpréteur de commande 'cmd'
2.  Exécuter cette commande:    git clone https://github.com/ezzine-montassar/Charity_Data_Management_Interface
3.  cd Charity_Data_Management_Interface
4.  pip install -r requirements.txt
5.  Editez le fichier create_db.py pour l'adapter à vos exigences (Nom de la base, noms des tables, etc).
6.  Créez la base de données:  python create_db.py
7.  Ouvrez le fichier app.py en mode édition afin d’adapter l’adresse IP du serveur Flask ainsi que les noms de la base de données et des tables selon vos besoins.
8.  Modifiez également les fichiers HTML si des changements sont apportés à la structure de la base (par exemple, la création de nouvelles tables).
9.  Pour créer un nouvel utilisateur root, décommentez les lignes nécessaires dans le fichier login.html.
10.  Lancez le serveur:  python app.py
11.  Accédez à l’interface via l’adresse IP attribuée, en utilisant le port 5000 (ex. : http://192.168.1.1:5000).
