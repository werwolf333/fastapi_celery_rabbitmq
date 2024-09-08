# FastAPI + Celery + RabbitMQ Project
## Описание

Этот проект демонстрирует использование FastAPI с Celery и RabbitMQ. В проекте используется два контейнера с воркерами и один контейнер с FastAPI, который добавляет задачи в очередь RabbitMQ (Задачи обрабатываются примитивом цепочки, состоящей из двух шагов). Проект также включает Flower для мониторинга задач.

## Установка и настройка

Следуйте этим шагам, чтобы развернуть проект на своей машине.

### 1. Клонирование репозитория

Начните с клонирования репозитория на локальную машину:

```bash
git clone https://github.com/yourusername/fastapi_celery_rabbitmq.git
```
Перейдите в директорию проекта:

```bash
cd fastapi_celery_rabbitmq
```

### 2. Запуск проекта

После клонирования репозитория выполните команду для сборки и запуска контейнеров:


```bash
docker-compose up --build
```

Это поднимет следующие сервисы:

- **FastAPI** на порту 8000 для добавления задач в очередь.
- **RabbitMQ** с веб-интерфейсом на порту 15672 (логин/пароль: guest/guest).
- **Worker1** и **Worker2**, которые обрабатывают задачи из очереди.
- **Flower** на порту 5555 для мониторинга задач Celery.

### 3. Открытие интерфейсов

- FastAPI доступен по адресу: http://localhost:8000
- RabbitMQ Management доступен по адресу: http://localhost:15672
- Flower доступен по адресу: http://localhost:5555

### 4. Пример использования

После запуска проекта вы можете отправлять задачи через FastAPI двумя способами:
- Использовать Swagger-документацию для тестирования POST-запросов: http://127.0.0.1:8000/docs 
- Через веб-форму: http://localhost:8000

Выберите число запросов которое хотите отправить в очередь. Например, 100, и отправьте их в очередь.  По адресу RabbitMQ http://localhost:15672/#/queues вы увидите как в таблице, как добавленные вами в очередь  **task_queue** задачи будут обрабатываться. Каждый воркер обрабатывает за раз по 5 задач, каждую задачу он обрабатывает 10 секунд. То есть вы увидите как каждые 10 секунд будут убывать по 10 задач из очереди (Задачи обрабатываются примитивом цепочки, состоящей из двух шагов).

Так же можно воспользоваться **Flower** для мониторинга http://localhost:5555

