from flask import Flask, request, render_template
import os

app = Flask(__name__)

def lire_texte(nom_fichier):
    try:
        with open(nom_fichier + ".txt", "r", encoding="utf-8") as fichier:
            return fichier.read().replace("\n", "<br>")
    except FileNotFoundError:
        return f"❌ Fichier {nom_fichier}.txt introuvable."

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():
    msg = []

    # Champs individuels
    prof = request.form.get("profession", "").lower()
    naissance_lieu = request.form.get("naissance_lieu", "").lower()
    naissance_date = request.form.get("naissance_date", type=int)
    religion_naissance = request.form.get("religion_naissance", "")
    religion_mariage = request.form.get("religion_mariage", "")
    cause_deces = request.form.get("cause_deces", "")
    liste_prof = request.form.get("liste_prof", "").lower()
    liste_doc = request.form.get("liste_doc", "").lower()

    # Règles
    if religion_naissance == "juif" and naissance_lieu == "avignon":
        msg.append("🕍 Religion juive à la naissance à Avignon — archives communautaires à consulter.")
    if religion_mariage == "musulman":
        msg.append("💍 Mariage musulman — consulter les actes religieux spécifiques.")
    if cause_deces == "suicide":
        msg.append("⚠️ Cause du décès : suicide — voir archives judiciaires ou hospitalières.")
    if prof == "militaire":
        msg.append("🪖 Profession militaire détectée — consulter registres de conscription.")
    if naissance_date == 1800 and naissance_lieu == "strasbourg":
        msg.append("📅 Né en 1800 à Strasbourg — archives napoléoniennes disponibles.")
    if liste_prof == "militaire":
        msg.append("🧑‍✈️ Sélection dans la liste : militaire — orienter vers les archives de guerre.")
    if liste_doc == "cadastre" and naissance_date == 1800:
        msg.append("🗺️ Cadastre en 1800 — premières cartes sous Napoléon Bonaparte.")

    doc_texte = lire_texte(liste_doc)
    msg.append(f"📄 <strong>{liste_doc}.txt</strong> :<br>{doc_texte}")

    if not msg:
        msg.append("🤷 Aucune règle n’a été déclenchée.")

    return render_template("index.html", message="<br><br>".join(msg))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
🧾 templates/index.html — Interface utilisateur
💡 Ce fichier est à placer dans le dossier templates/ à la racine de ton projet.

html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Prof41 – Généalogie</title>
  <style>
    /* ... styles identiques à ceux déjà définis ... */
  </style>
</head>
<body>
  <form method="post" action="/analyse">
    <div class="left">
      <h3>🧬 Analyse par événements</h3>
      <!-- ... tout ton bloc de formulaire à gauche ... -->
    </div>

    <div class="center">
      <h3>📜 Infos personnelles</h3>
      <!-- ... formulaire central ... -->
      <button type="submit">Lancer l’analyse</button>
    </div>

    <div class="right">
      <h3>📡 Résultat</h3>
      {% if message %}
        <div class="message-box">
          {{ message|safe }}
        </div>
      {% endif %}
    </div>
  </form>
</body>
</html>
