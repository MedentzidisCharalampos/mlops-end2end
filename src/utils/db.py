import sqlite3

def init_db():
    conn = sqlite3.connect("mlops.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            features TEXT,
            prediction INTEGER
        )
    """)
    conn.commit()
    conn.close()

def log_prediction(features, prediction):
    conn = sqlite3.connect("mlops.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO predictions (features, prediction) VALUES (?, ?)",
                (str(features), prediction))
    conn.commit()
    conn.close()