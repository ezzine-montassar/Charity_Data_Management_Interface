# create_db.py
import sqlite3

# Connexion (ou création) à la base de données
conn = sqlite3.connect('JCI_Data.db')
cursor = conn.cursor()

# Création de la table users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
''')

# Création de la table majeur
cursor.execute('''
CREATE TABLE IF NOT EXISTS majeur (
    id_majeur INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    sexe TEXT CHECK (sexe IN ('h', 'f')) NOT NULL,
    adresse TEXT NOT NULL,
    telephone TEXT NOT NULL,
    nombre_d_enfants INTEGER NOT NULL,
    statut_travail TEXT CHECK (statut_travail IN ('0', '1')) NOT NULL,
    handicap TEXT CHECK (handicap IN ('0', '1')) NOT NULL
);
''')

# Création de la table enfant
cursor.execute('''
CREATE TABLE IF NOT EXISTS enfant (
    id_enfant INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    sexe TEXT CHECK (sexe IN ('h', 'f')) NOT NULL,
    adresse TEXT NOT NULL,
    handicap TEXT CHECK (handicap IN ('0', '1')) NOT NULL,
    orphelin TEXT CHECK (orphelin IN ('0', '1', '2')) NOT NULL,
    id_parent INTEGER NOT NULL,
    FOREIGN KEY (id_parent) REFERENCES majeurs(id_majeur)
);
''')


# Commit et fermeture
conn.commit()
conn.close()
