# Load Balancer com NGINX e FastAPI
## Versão 1.0.1
#### Este é um projeto de balanceamento de carga usando Docker e NGINX para gerenciar múltiplas instâncias de APIs criadas com FastAPI. O NGINX atua como um proxy reverso para distribuir as requisições entre diferentes containers de API, permitindo escalabilidade e maior disponibilidade.

## Descrição

#### Este projeto simula um sistema de balanceamento de carga para múltiplas instâncias de APIs. O NGINX é configurado para distribuir as requisições de forma equilibrada entre os containers do Docker. As APIs são implementadas com FastAPI, um framework de alto desempenho para a construção de APIs.

### A configuração do NGINX inclui dois clusters de APIs:

- **Cluster 1: APIs 1, 2 e 3 (atendendo em rotas /, balanceadas)**
- **Cluster 2: APIs 4, 5 e 6 (atendendo em rotas /two, balanceadas)**

### Tecnologias

- **Docker**: Para orquestrar os containers.
- **NGINX**: Para balanceamento de carga entre as instâncias de API.
- **FastAPI**: Framework utilizado para criar as APIs.
- **Docker Compose**: Para orquestrar a configuração dos containers.

## Como Rodar o Projeto
### Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

- **Docker**: [Instalar Docke](https://github.com/Rodrigo-Kelven/Script-Docker)


Passo a Passo

- **Clone este repositório:**

        git clone https://github.com/Rodrigo-Kelven/Project_Load_Balancer
        cd Project_Load_Balancer

- **Construa as imagens e inicie os containers com o Docker Compose:**

        docker-compose up --build
  
- **Caso queira saber o status do Load Balancer -> NGINX:**

        docker stats project_load_balancer_nginx_1 

- **Para ver os logs do container Load Balancer -> NGINX:**

        docker logs -f project_load_balancer_nginx_1

- ### Este comando irá:

    - Construir as imagens dos containers.
    - Subir as APIs e o NGINX.
    - Expor as APIs nas portas 8001-8006 e o NGINX na porta 80.

- ### Após a execução bem-sucedida, o NGINX estará balanceando as requisições para as APIs.

## Estrutura do Projeto

### A estrutura do projeto é a seguinte:

    /Project_Load_Balancer
    ├── api_1/
    │    ├── Dockerfile
    │    ├── main.py
    │    └── requirements.txt
    ├── api_2/
    │    ├── Dockerfile
    │    ├── main.py
    │    └── requirements.txt
    ├── api_3/
    │    ├── Dockerfile
    │    ├── main.py
    │    └── requirements.txt
    ├── api_4/
    │    ├── Dockerfile
    │    ├── main.py
    │    └── requirements.txt
    ├── api_5/
    │    ├── Dockerfile
    │    ├── main.py
    │    └── requirements.txt
    ├── api_6/
    │    ├── Dockerfile
    │    ├── main.py
    │    └── requirements.txt
    ├── nginx/
    │    ├── Dockerfile
    │    └── nginx.conf
    └── docker-compose.yml


## Descrição dos Arquivos

- **api/Dockerfile:** Contém a configuração para construir o container da API com FastAPI.
- **nginx/nginx.conf:** Arquivo de configuração do NGINX, que define os clusters de APIs e a distribuição de requisições.
- **docker-compose.yml:** Configuração para orquestrar todos os containers (NGINX e APIs) dentro de uma rede interna.

# Configurações

### O arquivo nginx.conf contém duas seções principais para o balanceamento de carga:

    Upstreams: Define dois clusters de APIs:
        fastapi_cluster_1 (APIs 1, 2 e 3)
        fastapi_cluster_2 (APIs 4, 5 e 6)

    Proxy Reverso:
        /: Roteia para o fastapi_cluster_1.
        /two: Roteia para o fastapi_cluster_2.

## Exemplo de nginx.conf
    events {
        worker_connections 1024;
    }

    http {
        upstream fastapi_cluster_1 {
            server api_1:8000;
            server api_2:8000;
            server api_3:8000;
        }

        upstream fastapi_cluster_2 {
            server api_4:8000;
            server api_5:8000;
            server api_6:8000;
        }

        server {
            listen 80;

            location / {
                proxy_pass http://fastapi_cluster_1;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }

            location /two {
                proxy_pass http://fastapi_cluster_2;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
    }


## Como Testar

### Após rodar o projeto, você pode testar as APIs balanceadas pelo NGINX acessando as seguintes rotas:

- API Cluster 1 (APIs 1, 2 e 3):
    - Acesse http://localhost/ para testar o balanceamento entre as APIs 1, 2 e 3.
- API Cluster 2 (APIs 4, 5 e 6):
    - Acesse http://localhost/two para testar o balanceamento entre as APIs 4, 5 e 6.

**Você pode verificar o balanceamento de carga fazendo múltiplas requisições e observando qual API responde.**

## Exemplo de Teste com **curl**:

- ### Teste Cluster 1 (APIs 1, 2, 3):
        curl http://localhost/
- ### Teste Cluster 2 (APIs 4, 5, 6):
        curl http://localhost/two/

## Considerações Finais

**Este projeto oferece uma solução simples de balanceamento de carga usando Docker, NGINX e FastAPI. Ele pode ser expandido para suportar mais APIs e implementações de balanceamento, como round-robin, least connections, etc.**

**Caso precise ajustar o projeto para diferentes cenários ou implementar mais recursos, fique à vontade para modificar os arquivos de configuração e adicionar novas APIs.**

# Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.;)

## Autores
- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
