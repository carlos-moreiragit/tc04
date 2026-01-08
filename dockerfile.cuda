# Imagem NVIDIA com suprte a GPU
FROM nvidia/cuda:13.0.1-base-ubuntu24.04 AS base

WORKDIR /app

# Updade e instalação de dependendias
RUN apt-get update && apt-get install -y python3 python3-pip build-essential python3-venv

# Criação do ambiente virtual
RUN python3 -m venv /opt/venv

# Criação das variáveis de ambiente
ENV PATH="/opt/venv/bin:$PATH"
ENV XLA_FLAGS=--xla_gpu_cuda_data_dir=/usr/lib/cuda/

# Copia os arquivos necessários
COPY requirements.txt .
COPY app.py .
COPY tc04.pkl .

# Instala as dependêicas do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta
EXPOSE 5000

# Executa o projeto
CMD ["python3", "./app.py"]
