# Projeto Fase 4 5MLET
Este documento contém informações sobre o projeto da quarta fase do curso 5MLT. Este projeto apresenta um modelo preditivo de redes neurais Long Short
Term Memory (LSTM) especializado na predição do valor das ações do Google.

## Treinamento
O modelo foi treinato utilizando o Google Colab e salvo no formato pkl.

- Foram utilizados dados históricos da API yfinance dos últimos 2 anos:

https://github.com/ranaroussi/yfinance

# Frameworks
- Python 3.x
- numpy
- flask
- keras
- tensorflow

## Executar Localmente
- python -m venv venv
- pip install -r requirements.txt
- python app.py

## Executar no Container Docker
docker build -t tc04 .
docker run --gpus all -it tc04

> Nota: É necessário possuir uma GPU NVIDIA

## API
Para utilizar o modelo foi contruida uma API com os seguintes endpoints:

|Funçao|Endpoint|
| ------ | ------- |
|Previsão do próximo fechamento|http://localhost:5000/predict|
|Health Check|http://localhost:5000/healthcheck|

### /predict (POST)
Enviar no corpo da requisição, formato raw/JSON uma série temporal contendo o valor de fechamento das ações do Google para obter o valor do próximo fechamento.

### /healthcheck (GET)
Retorna HTTP 200 OK caso o serviço esteja disponível.
