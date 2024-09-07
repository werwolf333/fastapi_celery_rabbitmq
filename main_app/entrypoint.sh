#!/bin/bash

# Запускаем FastAPI приложение на порту 8000
uvicorn app.main:app --host 0.0.0.0 --port 8000
