# Nginx + Backend (Test EM)

## Архитектура

nginx → backend (python http server)

Backend работает только внутри docker-сети, а снаружи nginx.

## Структура

backend — Python HTTP сервер (app.py , Dockerfile)

nginx — reverse proxy 

docker-compose — оркестрация, поднимает оба сервиса и сеть

## Запуск

cp .env.example .env

docker compose up --build -d

## Проверка

curl http://localhost

Ожидаемый ответ:

Hello from Effective Mobile!

## Используемые технологии

- Docker
- Docker Compose
- Nginx
- Python http.server
