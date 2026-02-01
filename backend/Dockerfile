FROM python:3.12-alpine

WORKDIR /app

RUN adduser -D appuser

COPY app.py .

EXPOSE 8080

USER appuser

CMD ["python", "app.py"]
