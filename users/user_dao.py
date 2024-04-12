#import for test in my file init 
from users.user import User

#Import pour l'exterieur du package user 
from users.user import User

import database
class UserDAO:
    connexion=database.connect_db()
    cursor = connexion.cursor()

    @classmethod
    def get_one(cls, username, password):
        sql="SELECT * FROM user WHERE username=%s and password=%s"
        try:
            UserDAO.cursor.execute(sql, (username, password))
            user= UserDAO.cursor.fetchone()
            message ='success'
        except Exception as error:
            message='failure'
            user =()
        return (message, user)
    
    @classmethod
    def add(cls, user: User):
        sql = "INSERT INTO user(nom_complet, username, password) VALUES(%s, %s, %s)"
        try:
            UserDAO.cursor.execute(sql, (user.nom, nom_complet, ))