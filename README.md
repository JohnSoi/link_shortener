# LinkShortener

Приложение для сокращения ссылок. Поддерживает анонимное и пользовательское сохранение ссылок со статистикой.

## Структура проекта

* ```backend``` - работа с БЛ через FastAPI.
* ```frontend``` - интерфейсная часть приложения на VueJS.
* ```docs``` - документация к продукту.
* ```docker``` - контейнеры для запуска приложения.

## Полезные команды

* Поднять конкретный контейнер: 

```bash
docker compose up -d <название контейнера>
```

* Посмотреть логи контейнера: 

```bash
docker compose logs -f <название контейнера>
```

* Пересборка контейнера:

```bash
docker-compose up --build <название контейнера>
```
## Статусы проверок:

* Backend: 

[![Backend CI](https://github.com/JohnSoi/link_shortener/actions/workflows/backend-ci.yml/badge.svg)](https://github.com/JohnSoi/link_shortener/actions/workflows/backend-ci.yml)
