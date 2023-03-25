# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:07:45 2023

@author: Blook
"""
import mysql.connector as msql
import os

import user

currentuser= None

class InscriptionClass:

    def __init__(self, name, firstname, pseudo, password, vpassword):
        if password == vpassword:
            query = "insert into user(name,firstname,pseudo,password) values(%s,%s,%s,%s)"
            values = name, firstname, pseudo, password
            db = msql.connect(database="hackathon_db", user="root", passwd="", host="localhost")
            dbcur = db.cursor()
            dbcur.execute(query, values)
            dbcur.execute("select id from user where name='%s'", name)
            id = dbcur.fetchone()
            global currentUser
            currentUser = user.User(id, name, firstname, pseudo, password)
            os.open(connectionpage)
