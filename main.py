from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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


#============= DANH SACH GIA =============
@app.route("/DanhSachGia")
def DanhSachGia():
    return render_template("DanhSachGia.html")

#============= ĐẶT LỊCH =============
@app.route("/DatLich")
def DatLich():
    return render_template("DatLich.html")