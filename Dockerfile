# Stage 1: Build React App
FROM node:16 as frontend-builder

WORKDIR /app
COPY ./frontend/package.json ./frontend/package-lock.json ./
COPY ./frontend ./

# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt /app/

# Копирование собранного фронтенда
COPY --from=frontend-builder /app/build ./frontend

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Устанавливаем переменную окружения PYTHONPATH
ENV PYTHONPATH=/app

# Указываем порт, который будет использовать приложение
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
