# CandBenchmark

**Автор:** Голубенко Андрей

### Установка
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Запуск
```bash
docker compose up -d --build
```
