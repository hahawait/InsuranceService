FROM python:3.9-slim

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt

# Копируем файлы проекта в контейнер
COPY . .

WORKDIR src

# Запуск приложения при запуске контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
