@echo off
docker build -t helloworldapi .
docker run -p 8080:80 helloworldapi
