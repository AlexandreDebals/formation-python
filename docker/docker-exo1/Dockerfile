FROM ubuntu:bionic
RUN apt-get update && apt-get install -y git python3
WORKDIR exo
COPY hello.py .

# Commande de démarrage par défaut (écrasable, ex: ls)
# docker run --rm docker-exo1:1
# docker run --rm docker-exo1:1 ls
CMD ["python3", "hello.py"]