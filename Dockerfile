FROM docker.elastic.co/elasticsearch/elasticsearch:7.16.0
RUN apt-get update && apt-get install openssl -y
