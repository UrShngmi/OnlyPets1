import sqlite3
import json
import os
from passlib.hash import pbkdf2_sha256

class DatabaseManager:
    """
    Handles all database operations for the OnlyPets application.
    """
    def __init__(self, db_path='data/onlypets.db'):
        self.db_path = db_path
        self.data_dir = os.path.dirname(db_path)
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def init_db(self):
        """Initializes the database schema and populates with sample data if empty."""
        self._create_tables()
        self._populate_sample_data()

    def _create_tables(self):
        """Creates the necessary tables for the application."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                breed TEXT,
                age INTEGER,
                description TEXT,
                quick_facts TEXT,
                image_path TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL,
                image_path TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def _populate_sample_data(self):
        """Populates the database with sample data if it's empty."""
        self.cursor.execute("SELECT COUNT(*) FROM pets")
        if self.cursor.fetchone()[0] == 0:
            sample_pets = [
                ('Buddy', 'Golden Retriever', 2, 'A friendly and playful dog.', 'Loves fetch; Good with kids', 'assets/pets/dog1.jpg'),
                ('Lucy', 'Siamese', 1, 'A curious and vocal cat.', 'Very agile; Likes high places', 'assets/pets/cat1.jpg'),
                ('Max', 'German Shepherd', 3, 'Loyal and protective.', 'Highly intelligent; Needs exercise', 'assets/pets/dog2.jpg'),
                ('Misty', 'Persian', 4, 'A calm and affectionate cat.', 'Long fur; Enjoys naps', 'assets/pets/cat2.jpg'),
                ('Charlie', 'Beagle', 1, 'An energetic and happy dog.', 'Great sense of smell; Loves to explore', 'assets/pets/dog3.jpg'),
                ('Chloe', 'British Shorthair', 2, 'A sweet and gentle cat.', 'Plush coat; Independent', 'assets/pets/cat3.jpg'),
                ('Rocky', 'Boxer', 5, 'A powerful and energetic dog.', 'Playful; Good family dog', 'assets/pets/dog4.jpg'),
                ('Nala', 'Maine Coon', 2, 'A large and friendly cat.', 'Known as "gentle giants"; Fluffy tail', 'assets/pets/cat4.jpg'),
            ]
            self.cursor.executemany('INSERT INTO pets (name, breed, age, description, quick_facts, image_path) VALUES (?, ?, ?, ?, ?, ?)', sample_pets)

        self.cursor.execute("SELECT COUNT(*) FROM services")
        if self.cursor.fetchone()[0] == 0:
            sample_services = [
                ('Grooming', 'Full-service grooming including bath, haircut, and nail trim.', 50.00, 'assets/services/grooming.jpg'),
                ('Veterinary Checkup', 'Complete health checkup by a certified veterinarian.', 75.00, 'assets/services/vet.jpg'),
                ('Obedience Training', 'Basic obedience training classes for dogs.', 120.00, 'assets/services/training.jpg'),
                ('Pet Sitting', 'Day and overnight pet sitting services.', 40.00, 'assets/services/sitting.jpg'),
                ('Dental Cleaning', 'Professional dental cleaning for pets.', 90.00, 'assets/services/dental.jpg'),
            ]
            self.cursor.executemany('INSERT INTO services (name, description, price, image_path) VALUES (?, ?, ?, ?)', sample_services)

        self.conn.commit()

    def get_pets(self):
        """Fetches all pets from the database."""
        self.cursor.execute("SELECT * FROM pets")
        return self.cursor.fetchall()

    def get_services(self):
        """Fetches all services from the database."""
        self.cursor.execute("SELECT * FROM services")
        return self.cursor.fetchall()

    def add_user(self, username, password):
        """Adds a new user to the database with a hashed password."""
        password_hash = pbkdf2_sha256.hash(password)
        try:
            self.cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False # Username already exists

    def verify_user(self, username, password):
        """Verifies a user's credentials."""
        self.cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        result = self.cursor.fetchone()
        if result and pbkdf2_sha256.verify(password, result[0]):
            return True
        return False

    def __del__(self):
        self.conn.close()

class WishlistManager:
    """Manages the guest's wishlist using a JSON file."""
    def __init__(self, filepath='data/wishlist.json'):
        self.filepath = filepath
        self.wishlist = self._load_wishlist()

    def _load_wishlist(self):
        """Loads the wishlist from the JSON file."""
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_wishlist(self):
        """Saves the current wishlist to the JSON file."""
        with open(self.filepath, 'w') as f:
            json.dump(self.wishlist, f, indent=4)

    def add_to_wishlist(self, item_id):
        """Adds an item to the wishlist."""
        if item_id not in self.wishlist:
            self.wishlist.append(item_id)
            self._save_wishlist()

    def remove_from_wishlist(self, item_id):
        """Removes an item from the wishlist."""
        if item_id in self.wishlist:
            self.wishlist.remove(item_id)
            self._save_wishlist()

    def get_wishlist(self):
        """Returns the current wishlist."""
        return self.wishlist
