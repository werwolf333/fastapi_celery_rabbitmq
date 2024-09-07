#!/bin/bash

celery -A app.celery_app.celery worker --concurrency=5 --loglevel=info
