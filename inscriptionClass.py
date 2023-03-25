# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:07:45 2023

@author: Blook
"""
import mysql.connector as msql


class InscriptionClass:
    name = nameField.get()
    firstname = firstnameField.get()
    pseudo = pseudoField.get()
    password = passwordField.get()
    vpassword = vpasswordField.get()

    db = msql.connect(database="hackathon_db", username="root", passwd="", host="localhost")
    dbcur = db.cursor()

    def __init__(self, name, firstname, pseudo, password, vpassword):
        if (password == vpassword):
            query = "insert into user(id,name,firstname,pseudo,password) values(%s,%s,%s,%s,%s)"
            values = name, firstname, pseudo, password
            db = msql.connect(database="hackathon_db", username="root", passwd="", host="localhost")
            dbcur = db.cursor()
            dbcur.execute(query, values)
