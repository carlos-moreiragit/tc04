import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Carrega o modelo globalmente
with open('tc04.pkl', 'rb') as f:
    model = pickle.load(f)

# Rota para fazer previsões
@app.route('/predict', methods=['POST'])
def predict():

    # data recebe JSON do request body
    data = request.get_json(force=True)

    # cria numpy array
    input_features = np.array(data)

    prediction = model.predict(input_features.reshape(1, -1)) # Reshape para single prediction

    # transforma o numpy array em list
    prediction_list = prediction.tolist()

    # retorna JSON
    return jsonify({'prediction': prediction_list})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
