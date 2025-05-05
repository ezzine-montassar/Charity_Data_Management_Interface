from flask import Flask, render_template, request, flash, jsonify, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
#clé secréte
app.secret_key = 's3cr3tP@ssw0rd_JCI2025'

def get_db_connection():
    conn = sqlite3.connect('JCI_Data.db')
    conn.row_factory = sqlite3.Row  # Pour accéder avec des clés
    return conn



@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["username"] = user["username"]
            return redirect(url_for("index"))
        else:
            flash("Nom d'utilisateur ou mot de passe incorrect")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if not username or not password:
            flash("Veuillez remplir tous les champs.")
            return redirect(url_for("signup"))

        with sqlite3.connect("JCI_Data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash("Ce nom d'utilisateur existe déjà.")
                return redirect(url_for("signup"))

            hashed_pw = generate_password_hash(password)
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
            conn.commit()
            flash("Compte créé avec succès.")
            return redirect(url_for("login"))

    # ⬇️ Ce bloc est IMPORTANT pour les requêtes GET (affichage du formulaire)
    return render_template("signup.html")


@app.route("/index")
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    else:
        conn = get_db_connection()
        enfants = conn.execute('SELECT * FROM enfant').fetchall()
        majeurs = conn.execute('SELECT * FROM majeur').fetchall()
        conn.close()
    return render_template("index.html", enfants=enfants, majeurs=majeurs, username=session["username"])

@app.route("/logout" ,methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))





@app.route('/supprimer', methods=['POST'])
def supprimer():
    type_suppression = request.form.get('type-suppression')
    identifiant = request.form.get('ID_Suppression')

    # Choisir la table et la colonne ID selon le type
    if type_suppression == 'enfant':
        table = 'enfant'
        id_col = 'id_enfant'
    else:
        table = 'majeur'
        id_col = 'id_majeur'

    conn = get_db_connection()
    cursor = conn.cursor()

    # Vérifie d'abord si l'ID existe
    cursor.execute(f"SELECT * FROM {table} WHERE {id_col} = ?", (identifiant,))
    row = cursor.fetchone()

    if row:
        cursor.execute(f"DELETE FROM {table} WHERE {id_col} = ?", (identifiant,))
        conn.commit()

    conn.close()
    return redirect(url_for('index'))



@app.route('/ajout/majeur', methods=['POST'])
def ajout_majeur():
    nom = request.form.get('nommajeurAjout')
    prenom = request.form.get('prenommajeurAjout')
    sexe = request.form.get('sexemajeurAjout')
    adresse = request.form.get('adressemajeurAjout')
    telephone = request.form.get('telephonemajeurAjout')
    nombre_enfants = request.form.get('nombre_d_enfantsmajeurAjout')
    statut_travail = request.form.get('statut_travailmajeurAjout')
    handicap = request.form.get('handicapmajeurAjout')

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Récupérer tous les ID existants dans la table
    cursor.execute("SELECT id_majeur FROM majeur ORDER BY id_majeur")
    existing_ids = [row['id_majeur'] for row in cursor.fetchall()]

     # 2. Trouver le plus petit ID manquant
    new_id = 1
    for eid in existing_ids:
        if eid == new_id:
            new_id += 1
        else:
            break  # On a trouvé un trou

      # 3. Insertion avec l’ID manquant

    cursor.execute("""
	INSERT INTO majeur (id_majeur,nom, prenom, sexe, adresse, telephone, nombre_d_enfants, statut_travail, handicap)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", (new_id, nom, prenom, sexe, adresse, telephone, nombre_enfants, statut_travail,handicap))
    conn.commit()
    conn.close()
    print(f"Majeur ajouté : {nom} {prenom} ({sexe}), {adresse}, {telephone}, enfants: {nombre_enfants}, statut travail: {statut_travail}, Handicap: {handicap}")
    return redirect(url_for('index'))


@app.route('/ajout/enfant', methods=['POST'])
def ajout_enfant():
    nom = request.form.get('nomenfantAjout')
    prenom = request.form.get('prenomenfantAjout')
    sexe = request.form.get('sexeenfantAjout')
    adresse = request.form.get('adresseenfantAjout')
    handicap = request.form.get('handicapenfantAjout')
    orphelin = request.form.get('orphelinenfantAjout')
    id_parent = request.form.get('id_parentenfantAjout')

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Récupérer tous les ID existants dans la table
    cursor.execute("SELECT id_enfant FROM enfant ORDER BY id_enfant")
    existing_ids = [row['id_enfant'] for row in cursor.fetchall()]

    # 2. Trouver le plus petit ID manquant
    new_id = 1
    for eid in existing_ids:
        if eid == new_id:
            new_id += 1
        else:
            break  # On a trouvé un trou

    # 3. Insertion avec l’ID manquant
    cursor.execute("""
        INSERT INTO enfant (id_enfant, nom, prenom, sexe, adresse, handicap, orphelin, id_parent)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (new_id, nom, prenom, sexe, adresse, handicap, orphelin, id_parent))

    conn.commit()
    conn.close()

    print(f"Enfant ajouté avec ID {new_id} : {nom} {prenom}")
    return redirect(url_for('index'))



@app.route('/modification/majeur', methods=['POST'])
def modifier_majeur():
    id_majeur = request.form.get("IDmajeurModification")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "nom": "nommajeurModification",
        "prenom": "prenommajeurModification",
        "sexe": "sexemajeurModification",
        "adresse": "adressemajeurModification",
        "telephone": "telephonemajeurModification",
        "nombre_d_enfants": "nombre_d_enfantsmajeurModification",
        "statut_travail": "statut_travailmajeurModification",
        "handicap": "handicapmajeurModification"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(id_majeur)  # ID à la fin pour le WHERE

    query = f"UPDATE majeur SET {', '.join(updates)} WHERE id_majeur = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))  # ou renvoie un message/JSON selon ton besoin



@app.route('/modification/enfant', methods=['POST'])
def modifier_enfant():
    id_enfant = request.form.get("IDenfantModification")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "nom": "nomenfantModification",
        "prenom": "prenomenfantModification",
        "sexe": "sexeenfantModification",
        "adresse": "adresseenfantModification",
	    "handicap": "handicapenfantModification",
        "orphelin": "orphelinenfantModification",
        "id_parent": "id_parentenfantModification",
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(id_enfant)  # ID à la fin pour le WHERE

    query = f"UPDATE enfant SET {', '.join(updates)} WHERE id_enfant = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='192.168.139.142', port=5000, debug=True)

