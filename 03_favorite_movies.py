#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Стрингер, Американский психопат, Бойцовский клуб, Драйв, Таксист'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
print(my_favorite_movies[:8])
print(my_favorite_movies[57:])
print(my_favorite_movies[10:31])
print(my_favorite_movies[50:55])
