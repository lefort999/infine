from flask import Flask, render_template
app = Flask(__name__)

# Page d'accueil avec la liste des prénoms
@app.route("/")
def accueil():
    noms = ["Jacques", "Paul", "Jean", "Pierre"]
    return render_template("index.html", noms=noms)

# Page personnalisée pour chaque prénom
@app.route("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
