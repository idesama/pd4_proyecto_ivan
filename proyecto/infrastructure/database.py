"""Script para crear la base de datos de Fichajes con datos iniciales."""
import sqlite3
import os
from enum import Enum


class Database:

    class ENVIRONMENT(Enum):
        TEST = 0
        PRODUCTION = 1

    # TODO Pasar esto a un archivo de configuración json y cargarlo 
    PATH_PRODUCTION = './DB_PRO'
    PATH_TEST = './DB_TEST'

    def __init__(self, enviroment:ENVIRONMENT):
        self.enviroment = enviroment
        self.path_db = self.PATH_PRODUCTION
        if self.enviroment == self.ENVIRONMENT.TEST:
            self.path_db == self.PATH_PRODUCTION
  

    def db_exist(self)->bool:
        return os.path.exists(self.path_db)


    def execute_wrapper(self, query:str, data:tuple)->list[tuple]:
        if self.db_exist():
            try:
                with sqlite3.connect(self.path_db) as conn:
        
                    sql_blacklist = [
                        'CREATE',
                        'DROP',
                        'DELETE',
                        'OR 1=1'
                        '--'
                    ]

                    # filtro para blacklist
                    for blacky in sql_blacklist:
                        if blacky in query.strip().upper():
                            raise Exception
   
                    cursor = conn.cursor()       
                    cursor.execute(query, data)
                
                    if query.strip().upper().startswith("SELECT"):
                       return cursor.fetchall()

                    conn.commit()
                    return [(cursor.rowcount,)]
                    
            except Exception as ex:
                print(ex)
        else:
            print('La base de datos no existe.')


    def db_up(self):
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
                