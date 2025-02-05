# Usando a imagem oficial do NGINX
FROM nginx:latest


# Instalar o nano e o utilitário tail
RUN apt-get update && apt-get install -y nano && apt-get clean

# Copiar o arquivo de configuração do NGINX
COPY nginx.conf /etc/nginx/nginx.conf

# Expondo a porta 80 para o NGINX
EXPOSE 80
