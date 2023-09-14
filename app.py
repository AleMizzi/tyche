import os
import cs50
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
import blinker
import click
import itsdangerous
import jinja2
import werkzeug
from flask_session import Session
import tkinter
from tkinter import messagebox
import csv
import pytz #librerie necessarie
import requests #librerie necessarie
from helpers import apology, login_required, sendEmail, getFormat
import mysql.connector
from mysql.connector import Error


import pandas as pd
import pyodbc as odbc
from datetime import datetime




#DATABASE

db = SQL("sqlite:///database.db")
dbUtenti = SQL("sqlite:///utenti.db")
    
    
#CREAZIONE TABLE    
dbUtenti.execute("CREATE TABLE IF NOT EXISTS prenotazioni (nome, cognome, numtelefono, orario, numpersone, email)")


app = Flask (__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("storia.html")

@app.route("/storia")
def storia():
    return render_template("storia.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/pagprenota")
def pagprenotazione():
    return render_template("prenotazione.html")

@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/prenota", methods=["GET","POST"])
def prenota():
    if request.method == "GET":
        return redirect("/")

    elif request.method == "POST":
        #LE VARIABILI HANNO UNA LETTERA IN MENO RISPETTO A QUELLE DELL'HTML
        
        nom = request.form.get("nome") 

        
        cognom = request.form.get("cognome")

        
        numtelefon = request.form.get("numtelefono")

        
        orari = request.form.get("orario")
        

        emai = request.form.get("email")

    
        numperson = request.form.get("numpersone")
        
          
        dbUtenti.execute("INSERT INTO prenotazioni (nome, cognome, numtelefono, orario, numpersone, email) VALUES (?, ?, ?, ?, ?, ?)", nom, cognom, numtelefon, orari, numperson, emai)
       
        #il num delle persone non è segnato
        
        
        with open("prenotazioni.csv", "w", newline="") as f:
            writer = csv.writer(f)

            rows = dbUtenti.execute("SELECT * FROM prenotazioni")

            writer.writerow([rows])
           
        
        
        
        
        
        
        
        
        
        
        
        
        return render_template("prenotazioneeff.html")
        