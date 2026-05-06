"""Script para crear la base de datos de Fichajes con datos iniciales."""
import sqlite3
import os
from enum import Enum


# TODO Movelo a otro lado
class ENVIRONMENT(Enum):
    TEST = 0
    PRODUCTION = 1


class DB_sqlite:

    # TODO Pasar esto a un archivo de configuración json y cargarlo 
    PATH_PRODUCTION = './DB_PRO'
    PATH_TEST = './DB_TEST'


    def __init__(self, enviroment:ENVIRONMENT):
        self.enviroment = enviroment
        self.path_db = self.PATH_PRODUCTION
        if self.enviroment == ENVIRONMENT.TEST:
            self.path_db == self.PATH_PRODUCTION
  

    def db_exist(self)->bool:
        return os.path.exists(self.path_db)


    def get_conn(self):
        if self.db_exist():
            return sqlite3.connect(self.path_db).cursor()
        # TODO devolver excepcion personalizada


    def execute_crud(self, query:str):
        if not self.db_exist():
            try:
                with sqlite3.connect(self.path_db) as conn:
        
                    sql_blacklist = [
                        'CREATE',
                        'DROP',
                        'DELETE',
                        'OR 1=1'
                        '--'
                    ]

                    for blacky in sql_blacklist:
                        if blacky in query.strip().upper():
                            raise Exception

        
                    conn.row_factory = sqlite3.Row
                    cursor = conn.cursor()       
                    cursor.execute(query)
                
                    if query.strip().upper().startswith("SELECT"):
                       return cursor.fetchall()

                    conn.commit()
                    
            except Exception as ex:
                print(ex)

    def init_db(self):
        if not self.db_exist():
            try:
                with sqlite3.connect(self.path_db) as conn:
                    cursor = conn.cursor()
                    cursor.execute("PRAGMA foreign_keys = ON")
                    cursor.executescript("""              

                    CREATE TABLE IF NOT EXISTS users (
                        id TEXT PRIMARY KEY,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        rol INTEGER NOT NULL,
                        active INTEGER NOT NULL DEFAULT 1
                    );

                    CREATE TABLE IF NOT EXISTS clocks (
                        id TEXT PRIMARY KEY,
                        id_user TEXT NOT NULL,
                        date TEXT NOT NULL,
                        type INTEGER NOT NULL,
                        FOREIGN KEY (id_user) REFERENCES users(id)
                    );

                    CREATE INDEX IF NOT EXISTS idx_clocks_user ON clocks(id_user);
                    CREATE INDEX IF NOT EXISTS idx_clocks_date ON clocks(date);
                    """)

                    # Usuario admin por defecto (coincide con tu db.py actual)
                    cursor.execute(
                        """INSERT INTO users (id, username, password, rol, active)
                           VALUES (?, ?, ?, ?, ?)""",
                        ("6d976e5f-85ab-4bce-8c0f-aa9270eaa308", "admin", "1234", 1, 1),
                    )
                    conn.commit()
                    conn.close()
                    print("Base de datos creada en: fichajes.db")
            # TODO crear excepciones personalizadas
            except sqlite3.Error as e:
                print(f"Error de SQLite: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
                