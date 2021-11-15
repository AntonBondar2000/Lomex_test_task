## Инструкция по развертыванию
```
cd Lomex_test_task
docker-compose up --build
```

## Воозможные вопросы
```
### backend сервис доступен по адресу: 0.0.0.0:8081
### frontend сервис доступен по адресу: localhost:8080
### Если возникает ошибка port already use, необходимось очистить порт и запустить заново
```

## Описание API

### Автодокументация доступна по адрессу: /docs

### /api/genres
```
  [
    {
      "genre": Название жанра,
      "movies_count": Кол-во фильмов этого жанра,
      "avg_rating": Средняя оценка фильмов этого жанра
    }
  ]
```

### /api/actors
```
  [
    {
      "name": Имя актера,
      "movies_count": Кол-во фильмов с актером,
      "best_genre": Лучший жанр с этим актеров
    }
  ]
```

### /api/directors
```
  [
    {
      "director": Имя режисера,
      "best_movies": Часто встречаемые актеры у этого режисера,
      "favourite_actors": топ 3 фильма
    }
  ]
```