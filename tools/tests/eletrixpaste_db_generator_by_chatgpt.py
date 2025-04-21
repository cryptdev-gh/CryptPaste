import sqlite3
from faker import Faker
import uuid

# Générer des données fictives
fake = Faker()

# Chemin vers la base de données SQLite
db_path = 'test_database.db'

# Connexion à la base de données SQLite
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Création de la table
c.execute('''
    CREATE TABLE IF NOT EXISTS pastes (
        id TEXT PRIMARY KEY,
        text TEXT,
        ip_address TEXT
    )
''')

# Fonction pour générer des données aléatoires
def generate_fake_data():
    paste_id = str(uuid.uuid4())  # Utilisation de UUID pour garantir un identifiant unique
    text = fake.text(max_nb_chars=200)  # Texte aléatoire
    ip_address = fake.ipv4()  # Adresse IP aléatoire
    return paste_id, text, ip_address

# Insérer 150 lignes de données fictives
for _ in range(150):
    paste_id, text, ip_address = generate_fake_data()
    c.execute('''
        INSERT INTO pastes (id, text, ip_address)
        VALUES (?, ?, ?)
    ''', (paste_id, text, ip_address))

# Sauvegarder les changements et fermer la connexion
conn.commit()
conn.close()

print("Base de données générée avec 150 entrées.")
