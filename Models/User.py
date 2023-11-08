from flask_bcrypt import Bcrypt  

class User():
    def __init__(self, name, nickname, password, bcrypt_util: Bcrypt):
        self.name = name
        self.nickname = nickname
        self.password_hash = bcrypt_util.generate_password_hash(password)