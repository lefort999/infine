from flask import Flask, request, render_template
import os

app = Flask(__name__)

def lire_texte(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return fichier.read().replace("\n", "<br>")
    except FileNotFoundError:
        return f"❌ Fichier {nom_fichier} introuvable."

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():
    msg = []
    prof = request.form.get("profession", "").lower()
    naissance_lieu = request.form.get("naissance_lieu", "").lower()
    naissance_date = request.form.get("naissance_date", type=int)
    liste_prof = request.form.get("liste_prof", "").lower()
    liste_doc = request.form.get("liste_doc", "").lower()

    for i in range(1, 16):
        religion = request.form.get(f"religion{i}", "")
        if religion == "juif" and naissance_lieu == "avignon":
            msg.append(f"🕍 Ligne {i} : Juif né à Avignon — consulter les archives spéciales.")

    if prof == "militaire":
        msg.append("🪖 Profil militaire détecté — voir registres de conscription.")
    if naissance_date == 1800 and naissance_lieu == "strasbourg":
        msg.append("📅 Né en 1800 à Strasbourg — nombreuses archives napoléoniennes.")
    if liste_prof == "militaire":
        msg.append("🧑‍✈️ Liste déroulante : militaire — orientation vers les archives de guerre.")
    if liste_doc == "cadastre" and naissance_date == 1800:
        msg.append("🗺️ Cadastre en 1800 — premières cartes sous Napoléon Bonaparte.")

    # Ajout du fichier texte
    doc_texte = lire_texte(f"{liste_doc}.txt")
    msg.append(f"📄 <strong>{liste_doc}.txt</strong> :<br>{doc_texte}")

    if not msg:
        msg.append("🤷 Aucune règle n’a été déclenchée.")

    return render_template("index.html", message="<br><br>".join(msg))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)