# Используйте официальный образ Python
FROM python:3.10

# Установите рабочую директорию
WORKDIR /app

# Копируем файл requirements.txt отдельно
COPY ./requirements.txt /app/requirements.txt

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы в рабочую директорию
COPY app /app/

# Копируем entrypoint.sh
COPY entrypoint.sh /entrypoint.sh

# Делаем entrypoint.sh исполняемым
RUN chmod +x /entrypoint.sh

# Запустите FastAPI
ENTRYPOINT ["/entrypoint.sh"]
