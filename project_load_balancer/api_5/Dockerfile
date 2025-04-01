# Usando a imagem oficial do Python
FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos de requisitos para o container
COPY requirements.txt /app/

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . /app/

# Expondo a porta da aplicação
EXPOSE 8000

# Comando para rodar a aplicação FastAPI com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
