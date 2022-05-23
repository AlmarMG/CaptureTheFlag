from flask import Flask, redirect, url_for, render_template, request, session, flash
from app import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/StijnsBureauTour")
def video():
    return render_template("video.html")
