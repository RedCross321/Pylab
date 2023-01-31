#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
    'бобовый клуб':
        [
            {'name': 'печенье', 'price': 110.99},
            {'name': 'конфеты', 'price': 50.99},
            {'name': 'энергетик Drive', 'price': 71.99},
            {'name': 'пирожное', 'price': 162.99}
        ],
    'У Гарри':
        [
            {'name': 'плод кактуса', 'price': 11.99},
            {'name': 'киви', 'price': 30.99},
            {'name': 'суши', 'price': 41.99},
        ]
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99},  
    ],
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},  
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},  
    ]
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
}
# Указать надо только по 2 магазина с минимальными ценами
