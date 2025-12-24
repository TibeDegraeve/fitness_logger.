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
def add_exercise(name, muscle_group):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO exercises (name, muscle_group) VALUES (?, ?)', 
                           (name, muscle_group))
            conn.commit()
            print(f"Succes: Oefening '{name}' is toegevoegd.")
        except sqlite3.IntegrityError:
            print(f"Let op: De oefening '{name}' bestaat al.")
        finally:
            conn.close()

def add_log(exercise_name, weight, reps, date):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM exercises WHERE name = ?', (exercise_name,))
        result = cursor.fetchone()
        
        if result:
            exercise_id = result['id']
            cursor.execute('''
                INSERT INTO logs (exercise_id, weight, reps, date) 
                VALUES (?, ?, ?, ?)
            ''', (exercise_id, weight, reps, date))
            conn.commit()
            print(f"Opgeslagen: {exercise_name} {reps}x{weight}kg op {date}")
        else:
            print(f"Fout: Oefening '{exercise_name}' onbekend. Voeg die eerst toe!")
        
        conn.close()

if __name__ == "__main__":
    # 1. Ervoor zorgen dat je tabellen bestaan
    create_tables()
    
    # 2. Oefeningen toevoegen
    print("--- Oefeningen toevoegen ---")
    add_exercise("Squat", "Benen")
    add_exercise("Bench Press", "Borst")
    
    # 3 Sets loggen (oefening, gewicht, reps, datum)
    print("\n--- Sets loggen ---")
    add_log("Squat", 100, 5, "2024-01-01")
    add_log("Bench Press", 60, 8, "2024-01-01")
    
    # 4 Foute oefening
    print("\n--- Fout test  ---")
    add_log("Onbestaande Oefening", 100, 10, "2024-01-01")