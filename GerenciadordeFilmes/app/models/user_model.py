from werkzeug.security import generate_password_hash, check_password_hash

class User:
    # Agora armazenamos o hash das senhas em vez da senha pura
    USERS_DB = {
        "admin": generate_password_hash("123456"),
        "cinema_lover": generate_password_hash("filmes2026"),
        "critico": generate_password_hash("oscar2026")
    }

    def __init__(self, username):
        self.username = username

    @classmethod
    def authenticate(cls, username, password):
        if username in cls.USERS_DB:
            stored_hash = cls.USERS_DB[username]
            # Verifica se a senha informada confere com o hash armazenado
            if check_password_hash(stored_hash, password):
                return cls(username)
        return None