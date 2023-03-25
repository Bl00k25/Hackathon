import mysql.connector as msql
from globalVar import currentUser

class whichOne :
    def __init__(self):
        db = msql.connect(database="hackathon_db", user="root", passwd="", host="localhost")
        dbcur = db.cursor()
        query = "select game_owned from user where id=%d"
        value = currentUser.id
        dbcur.execute(query, value)
        gameOwned = dbcur.fetchone()

        values = int(gameOwned.split(","))

        for value in values:
            dbcur.execute("SELECT GROUP_CONCAT(id) FROM game")
            result = dbcur.fetchone()[0]
            gameID = [int(value) for value in result.split(",")]

            for number in gameID :
                if value == number :
                    dbcur.execute("select name from game where id = number")
                    res=dbcur.fetchone()
                    folder = "D:/Hackathon/Game/" + res
                    if folder != None :
                        #Bouton Jouer
                    else :
                        #Bouton Installer
                else :
                    #Bouton acheter

