# Используйте базовый образ Python 3
FROM python:3.8

# Установите рабочую директорию для контейнера
WORKDIR /code 
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
# Скопируйте содержимое проекта в контейнер
COPY . .

# Запустите сервер на порту 8000
CMD ["python", "server.py", "8000"]