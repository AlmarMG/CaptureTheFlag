from flask import Flask, redirect, url_for, render_template, request
from app import app

@app.route("/")
def home():
    return render_template("index.html")
