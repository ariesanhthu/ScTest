import os

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import sqlite3

app = Flask(__name__)


#============= DANH SACH GIA =============
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

#============= HOME PAGE =============
@app.route("/")
@app.route('/home')
def home_page():
    return render_template("home.html")
#============= END HOME PAGE =============


#============= LOGIN PAGE =============
@app.route("/DangNhap")
def DangNhap():
    return render_template("DangNhap.html")

#============= ĐẶT LỊCH =============
@app.route("/DatLich")
def DatLich():
    return render_template("DatLich.html")
#============= TÌM NGƯỜI BÁN =============
@app.route("/TimNguoiBan")
def TimNguoiBan():
    return render_template("TimNguoiBan.html")
#============= CAMERA TRA CỨU =============
@app.route("/CameraTraCuu")
def CameraTraCuu():
    return render_template("CameraTraCuu.html")