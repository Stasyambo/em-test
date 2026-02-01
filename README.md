# Nginx + Backend (Test EM)

## Архитектура

nginx → backend (python http server)

Backend работает только внутри docker-сети, а снаружи nginx.

## Структура

backend — Python HTTP сервер (app.py , Dockerfile)

nginx — reverse proxy (nginx.conf)

docker-compose — оркестрация, поднимает оба сервиса и сеть (docker-compose.yml)

## Запуск

cp .env.example .env (пример файла конфигурации)

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
