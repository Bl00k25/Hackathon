import mysql.connector as msql
import os


class ConnectionClass:
    def __init__(self, pseudo, password):
        db = msql.connect(database="hackathon_db", username="root", passwd="", host="localhost")
        dbcur = db.cursor()

        query = "select * from user where pseudo = %s"
        dbcur.execute(query, (pseudo,))

        result = dbcur.fetchone()

        if result:
            if password == result[2]:
                print("Connecté")
                os.open("MainpPage.py")
            else:
                print("Mot de passe incorrect")
        else:
            print("Utilisateur introuvable")
