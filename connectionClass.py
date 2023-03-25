import mysql.connector as msql
import os


class ConnectionClass:
    def __init__(self, pseudo, password):
        db = msql.connect(database="hackathon_db", user="root", passwd="", host="localhost")
        dbcur = db.cursor()

        query = "select pseudo,password,id from user where pseudo = %s"
        dbcur.execute(query, (pseudo,))

        result = dbcur.fetchone()

        if result:
            if password == result[2]:
                print("Connecté")
                os.open(MainPage)
            else:
                print("Mot de passe incorrect")
        else:
            print("Utilisateur introuvable")

