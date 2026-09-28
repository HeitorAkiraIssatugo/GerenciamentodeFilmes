from flask import current_app
from app.database import get_db_connection
from werkzeug.security import check_password_hash

class User:
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    @classmethod
    def authenticate(cls, username, password):
        # Abre a conexão usando a configuração atual do Flask
        conn = get_db_connection(current_app.config)
        cursor = conn.cursor()
        
        # Consulta SQL pura com parâmetros seguros contra SQL Injection
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        
        # Fecha a conexão explicitamente após o uso
        conn.close()
        
        if row and check_password_hash(row['password_hash'], password):
            return cls(row['id'], row['username'], row['password_hash'])
        return None