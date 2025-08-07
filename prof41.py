from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    episodes = [
        "premier-episode",
        "deuxieme-episode",
        "troisieme-episode",
        "quatrieme-episode"
    ]
    return render_template("index.html", episodes=episodes)

@app.route("/episode/<nom>")
def afficher_episode(nom):
    chemin = os.path.join(os.getcwd(), f"{nom}.txt")
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        contenu = "Épisode introuvable."
    return render_template("episode.html", nom=nom, contenu=contenu)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
