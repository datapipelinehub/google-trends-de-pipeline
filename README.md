# Google Trends DE Pipeline

Data Engineering проект для сбора, хранения и подготовки данных Google Trends по нишам.

## Цель проекта
Собрать portfolio-проект для позиции Data Engineer: от получения данных из внешнего источника до их сохранения, логирования и дальнейшей подготовки к аналитике.

## Что уже реализовано
- структура репозитория под DE-проект
- конфигурация таймфреймов
- manifest-подход через `niche.json`
- raw/audit/manifests слои
- базовая документация проекта

## Текущий стек
- Python
- pytrends
- pandas
- JSON / JSONL
- CSV

## План развития
- ingestion для одной ниши и одного timeframe
- сохранение raw CSV
- audit logging
- batch processing по нескольким нишам
- clean layer
- загрузка в PostgreSQL или ClickHouse
- orchestration через Airflow
- Docker-окружение

## Почему этот проект важен
Проект показывает не просто парсинг, а подход Data Engineering:
- работа с внешним источником данных
- управляемая конфигурацией обработка
- понятная структура хранения
- логирование
- развитие от MVP к более production-like решению

## Текущий статус
В разработке. Текущий этап: подготовка MVP ingestion-слоя.
