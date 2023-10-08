import os

from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)


#Home Page route
@app.route("/")
def home():
	return render_template("base.html")

#DB test route
@app.route('/list')
def list():
	con = sqlite3.connect("database.db")
	con.row_factory = sqlite3.Row

	cur = con.cursor()
	cur.execute("SELECT id, * FROM ITEMS")

	rows = cur.fetchall()
	con.close()

	return render_template("list.html", rows = rows)

@app.route("/map")
def map():
	return render_template("map.html")