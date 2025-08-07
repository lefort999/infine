from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    episodes = [
        {"nom": "premier-episode", "image": "image1.jpg"},
        {"nom": "deuxieme-episode", "image": "image2.jpg"},
        {"nom": "troisieme-episode", "image": "image3.jpg"},
        {"nom": "quatrieme-episode", "image": "image4.jpg"}
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

    # Trouver l'image associée
    images = {
        "premier-episode": "image1.jpg",
        "deuxieme-episode": "image2.jpg",
        "troisieme-episode": "image3.jpg",
        "quatrieme-episode": "image4.jpg"
    }
    image = images.get(nom, None)

    return render_template("episode.html", nom=nom, contenu=contenu, image=image)
