import os
from flask import Flask, render_template, url_for, abort


app = Flask(__name__) # Utilise automatiquement le dossier ./static


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


# Une et une seule image: static/<nom>.jpg (facultative)
image_path = os.path.join(app.static_folder, f"{nom}.jpg")
image_url = url_for("static", filename=f"{nom}.jpg") if os.path.isfile(image_path) else None


return render_template("chapitre.html", nom=nom, contenu=contenu, image_url=image_url)




@app.errorhandler(404)
def not_found(e):
return render_template("404.html"), 404




if __name__ == "__main__":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)






