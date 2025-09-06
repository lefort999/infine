from flask import Flask, render_template, url_for, abort
import os

app = Flask(__name__)  # static/ est utilisé par défaut comme dossier de fichiers statiques

CHAPITRES = ["chapitre1", "chapitre2", "chapitre3", "chapitre4","chapitre5","chapitre6","chapitre7","chapitre8","chapitre9"]

@app.route("/")
def accueil():
    return render_template("index.html", chapitres=CHAPITRES)

@app.route("/chapitre/<nom>")
def afficher_chapitre(nom):
    # Sécurise: n'autorise que les chapitres connus
    if nom not in CHAPITRES:
        abort(404)

    # Fichier texte (placé à la racine du projet ou adapte le chemin si besoin)
    chemin_txt = os.path.join(os.getcwd(), f"{nom}.txt")
    try:
        with open(chemin_txt, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        contenu = "Chapitre introuvable."

    # Vérifie si une image existe dans static/ avec le même nom (ex: static/chapitre1.jpg)
    # Tu peux changer l'extension si tu utilises .png/.webp
    image_rel = f"{nom}.jpg"
    image_abs = os.path.join(app.static_folder, image_rel)
    image_exists = os.path.exists(image_abs)

    image_url = url_for("static", filename=image_rel) if image_exists else None

    return render_template("chapitre.html", nom=nom, contenu=contenu, image_url=image_url)

if __name__ == "__main__":
    # Render utilise le port défini par PORT ; si tu testes en local tu peux garder 10000.
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)






