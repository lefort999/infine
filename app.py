import os
from flask import Flask, render_template, url_for, abort

app = Flask(__name__)  # 'static/' utilisé par défaut

CHAPITRES = [
    "chapitre1","chapitre2","chapitre3","chapitre4","chapitre5",
    "chapitre6","chapitre7","chapitre8","chapitre9","chapitre10",
    "chapitre11","chapitre12","chapitre13","chapitre14","chapitre15"
]

@app.route("/")
def accueil():
    return render_template("index.html", chapitres=CHAPITRES)

@app.route("/chapitre/<nom>")
def afficher_chapitre(nom):
    # Autorise uniquement les chapitres connus
    if nom not in CHAPITRES:
        abort(404)

    # Texte du chapitre (fichiers à la racine: chapitreX.txt)
    chemin_txt = os.path.join(os.getcwd(), f"{nom}.txt")
    try:
        with open(chemin_txt, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        contenu = "Chapitre introuvable."

    # Images autorisées:
    # - principale :  static/chapitre3.jpg
    # - supplémentaires : static/chapitre3-bis.jpg, static/chapitre3-ter.jpg, etc.
    # On accepte **uniquement** les fichiers qui commencent par "<nom>" et finissent par ".jpg"
    images_abs = []
    if os.path.isdir(app.static_folder):
        for fname in os.listdir(app.static_folder):
            if fname.lower().endswith(".jpg") and fname.startswith(nom):
                images_abs.append(os.path.join(app.static_folder, fname))

    # Trie: l'image exacte "<nom>.jpg" en premier, puis les autres par ordre alphabétique
    def sort_key(p):
        base = os.path.basename(p)
        return (0 if base == f"{nom}.jpg" else 1, base.lower())

    images_abs.sort(key=sort_key)

    # Construit les URLs (pour le template)
    images_urls = [url_for("static", filename=os.path.basename(p)) for p in images_abs]

    return render_template("chapitre.html", nom=nom, contenu=contenu, images_urls=images_urls)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)






