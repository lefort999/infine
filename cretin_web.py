import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Déclaration de la variable port
port = int(os.environ.get("PORT", 4000))

# Fonction qui traite la demande de l'utilisateur
def rechercher_dossier(profession, date):
    if profession.lower() == "douanier" and date == "1805":
        return {"message": "Le dossier se trouve aux archives nationales."}
    else:
        return {"message": "Pas de dossiers."}

# Endpoint API
@app.route("/recherche", methods=["GET"])
def recherche():
    profession = request.args.get("profession")
    date = request.args.get("date")
    
    if not profession or not date:
        return jsonify({"error": "Veuillez fournir une profession et une date."}), 400
    
    return jsonify(rechercher_dossier(profession, date))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

