
# Insurance Cost Calculator

Проект представляет собой REST API сервис для расчета стоимости страхования грузов.

## Технологии

- FastAPI
- Tortoise ORM
- SQLite
- Docker

## Установка и запуск проекта 

### Шаг 1: Клонирование репозитория

Для начала работы необходимо клонировать репозиторий на ваш локальный компьютер. Для этого используйте следующую команду:

```bash
git clone https://github.com/hahawait/InsuranceService
```

### Шаг 2: Сборка и запуск Docker контейнера

Перейдите в директорию проекта с помощью команды `cd InsuranceService`. Затем выполните следующие команды для создания образа Docker и его запуска:

```bash
docker build -t insurance-calculator .
docker run -p 8000:8000 insurance-calculator 
```

После выполнения этих шагов ваш сервер будет доступен по адресу `http://localhost:8000`.

## Использование API 

### Добавление тарифов
Сервис предоставляет возможность добавления тарифов. Данный функционал доступен через следующий endpoint:

`POST /tariff/add`

**UPD Структура json данных с тарифами должна выглядеть следующим образом:**
```json
{
    "2020-06-01": [
        {
            "cargo-type": "Glass",
            "rate": "0.04"
        },
        {
            "cargo-type": "Other",
            "rate": "0.01"
        }
    ],
    "2020-07-01": [
        {
            "cargo-type": "Glass",
            "rate": "0.035"
        },
        {
            "cargo-type": "Other",
            "rate": "0.015"
        }
    ]
}
```

### Расчет стоимости страховки 

Сервис предоставляет возможность расчитывать стоимость страховки для разных типов грузов. Данный функционал доступен через следующий endpoint:

`POST /calculate-insurance`


**Подробнее на `http://localhost:8000/docs`**
