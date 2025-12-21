import sqlite3
from settings import DB_PATH

def get_db_connection():
    """Maakt verbinding met de SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Fout bij verbinden met database: {e}")
        return None

def create_tables():
    """Maakt de tabellen aan voor Oefeningen en Logs."""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                muscle_group TEXT
            )
        ''')
        
       
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                exercise_id INTEGER,
                weight REAL,
                reps INTEGER,
                date TEXT,
                FOREIGN KEY (exercise_id) REFERENCES exercises (id)
            )
        ''')
        
        conn.commit()
        conn.close()
        print("Succes: Tabellen zijn aangemaakt in de database.")

if __name__ == "__main__":
    create_tables()