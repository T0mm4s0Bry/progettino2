from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

Lista_Spesa = []


@app.route('/api/lista', methods=['GET'])
def get_lista():
    return jsonify(Lista_Spesa)

@app.route('/api/aggiungi', methods=['POST'])
def aggiungi_elemento():
    data = request.json
    Lista_Spesa.append(data['elemento'])
    return jsonify({"message": "Elemento aggiunto", "lista": Lista_Spesa})

@app.route('/api/rimuovi/<int:index>', methods=['DELETE'])
def rimuovi_elemento(index):
    if 0 <= index < len(Lista_Spesa):
        elemento_rimosso = Lista_Spesa.pop(index)
        return jsonify({"message": f"Elemento '{elemento_rimosso}' rimosso", "lista": Lista_Spesa})
    else:
        return jsonify({"error": "Indice non valido"}), 400

@app.route('/api/svuota', methods=['DELETE'])
def svuota_lista():
    Lista_Spesa.clear()
    return jsonify({"message": "Lista svuotata"})

if __name__ == '__main__':
    app.run(debug=True)
