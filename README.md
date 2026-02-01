# Nginx + Backend (Test EM)

## Архитектура

nginx → backend (python http server)

Backend работает только внутри docker-сети, а снаружи nginx.

## Структура

backend — Python HTTP сервер 

nginx — reverse proxy 

docker-compose — оркестрация

## Запуск

cp .env.example .env

docker compose up --build

## Проверка

curl http://localhost

Ожидаемый ответ:

Hello from Effective Mobile!

## Healthcheck

curl http://localhost/health

## Используемые технологии

- Docker
- Docker Compose
- Nginx
- Python http.server
