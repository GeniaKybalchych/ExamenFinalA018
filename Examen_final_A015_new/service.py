import requests
from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('/test')
def test():
    return "Test successful"

# Ajouter les données
@app.route('/projets', methods=['POST'])
def ajouter_projet():

    try:
        # Récupérez les données
        data = request.json

        # Appelez le service DAO pour insérer les données dans la BD
        response = requests.post(f'http://127.0.0.1:5001/projets', json=data)
        response_data = response.json()
        return jsonify(projet=response_data), response.status_code
    except Exception as e:
        return jsonify(error=str(e)), 500

# Rechercher les données
@app.route('/projets/<string:codeProjet>', methods=['GET'])
def get_projet(codeProjet):

    try:

        # Appelez le service DAO pour rechercher les données dans la BD
        response = requests.get(f'http://127.0.0.1:5001/projets/{codeProjet}')

        response_data = response.json()
        return jsonify(response_data), response.status_code
    except Exception as e:
        return jsonify(status="error", message=str(e)), 500

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)