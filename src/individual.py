#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


# Пример входных данных (можно заменить своими)
cities = {
    'Лонгфорд': {
        'Ньюнхем': 31.4, 'Экстон': 37.1,
        'Бреона': 51.4, 'Конара': 43.2, 'Дерби': 111.9
    },
    'Конара': {'Сент-Мэрис': 73.9, 'Кэмпбелл-Таун': 12.5},
    'Кэмпбелл-Таун': {'Танбридж': 27.1, 'Лейк Лик': 34.8},
    'Лейк Лик': {'Бичено': 57, 'Суонси': 33.8},
    'Ньюнхем': {'Джордж Таун': 44.3, 'Лилидейл': 21.3},
    'Джордж Таун': {},
    'Лилидейл': {'Лебрина': 8.7},
    'Лебрина': {'Пайперс Брук': 13.3, 'Бридпорт': 27},
    'Экстон': {'Элизабет Таун': 18.4, 'Мол Крик': 30.8, 'Бреона': 38.4},
    'Элизабет Таун': {'Шеффилд': 28, 'Девонпорт': 42.5},
    'Девонпорт': {},
    'Шеффилд': {'Мойна': 31.7},
    'Мойна': {},
    'Бреона': {'Рейнольдс Лейк': 11.2, 'Шеннон': 26.5, 'Ботуэлл': 66.7},
    'Рейнольдс Лейк': {'Миена': 18.5},
    'Мол Крик': {'Шеффилд': 51.5},
    'Миена': {'Тарралия': 59.2},
    'Шеннон': {'Миена': 17.2},
    'Тарралия': {'Уэйятина': 16.5},
    'Уэйятина': {},
    'Ботуэлл': {},
    'Танбридж': {},
    'Литл Суонпорт': {},
    'Суонси': {'Литл Суонпорт': 27.7},
    'Сент-Мэрис': {'Гарденс': 55.8},
    'Гарденс': {'Дерби': 61.1},
    'Дерби': {},
    'Пайперс Брук': {},
    'Бридпорт': {},
}

start_city = 'Гарденс'  # Исходный город
end_city = 'Мойна'    # Целевой город
max_depth = 6  # Ограничение глубины поиска


# Создание симметричного графа
def create_symmetric_graph(cities):
    symmetric_cities = {}
    for city, neighbors in cities.items():
        if city not in symmetric_cities:
            symmetric_cities[city] = {}
        for neighbor, distance in neighbors.items():
            symmetric_cities[city][neighbor] = distance
            if neighbor not in symmetric_cities:
                symmetric_cities[neighbor] = {}
            symmetric_cities[neighbor][city] = distance
    return symmetric_cities


symmetric_cities = create_symmetric_graph(cities)


# Генерация всех возможных маршрутов с ограничением глубины
def find_routes(cities, start, end, max_depth):
    routes = []

    def dfs(path, current_city, depth):
        if current_city == end:
            routes.append(path)
            return
        if depth >= max_depth:
            return
        for neighbor in cities.get(current_city, {}):
            if neighbor not in path:
                dfs(path + [neighbor], neighbor, depth + 1)

    dfs([start], start, 0)
    return routes


# Вычисление длины маршрута
def calculate_distance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i + 1]]
    return distance


# Построение графа и отображение маршрутов
def plot_graph(cities, routes, shortest_route):
    G = nx.DiGraph()

    # Добавление рёбер с весами
    for city, neighbors in cities.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(city, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Позиционирование узлов

    # Отображение графа
    plt.figure(figsize=(12, 8))
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700,
            node_color='lightblue', font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Подсветка всех маршрутов
    for route in routes:
        edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges,
                               edge_color='gray', width=1, style='dotted')

    # Подсветка альтернативных маршрутов
    for route in routes:
        if route != shortest_route:
            alt_edges = [
                (route[i], route[i + 1])
                for i in range(len(route) - 1)
            ]
            nx.draw_networkx_edges(G, pos, edgelist=alt_edges,
                                   edge_color='blue', width=1)

    # Подсветка самого короткого маршрута
    shortest_edges = [
        (shortest_route[i], shortest_route[i + 1])
        for i in range(len(shortest_route) - 1)
    ]
    nx.draw_networkx_edges(G, pos, edgelist=shortest_edges,
                           edge_color='red', width=2)

    plt.title("Граф маршрутов")
    plt.show()


# Основной код
all_routes = find_routes(symmetric_cities, start_city, end_city, max_depth)
all_routes_with_distances = [
    (route, calculate_distance(route, symmetric_cities))
    for route in all_routes
]
sorted_routes = sorted(all_routes_with_distances, key=lambda x: x[1])

# Вывод всех маршрутов
print("Все маршруты из", start_city, "в",
      end_city, "с ограничением глубины", max_depth, ":")
for route, distance in sorted_routes:
    print(f"Маршрут: {'->'.join(route)}, Расстояние: {round(distance, 1)} км")

# Вывод самого короткого маршрута
if sorted_routes:
    shortest_route = sorted_routes[0][0]
    shortest_distance = sorted_routes[0][1]
    print(f"\nСамый короткий маршрут: {' -> '.join(shortest_route)},")
    print(f"Расстояние: {round(shortest_distance, 1)} км")
    plot_graph(symmetric_cities, [route for route, _ in sorted_routes],
               shortest_route)
