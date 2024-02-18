from collections import (
    Counter,
    namedtuple,
    deque,
    defaultdict
)

# deque
queue = deque()
queue.append(1) # Добавление элемента в конец очереди
queue.append(2)
queue.appendleft(3) # Добавление элемента в начало очереди
print(queue) # Вывод: deque([3, 1, 2])
item = queue.popleft() # Удаление и получение элемента из начала очереди
print(item) # Вывод: 3

# Counter
data = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 2, 1]
counter = Counter(data)
# counter = {elem: data.count(elem) for elem in data}
# print(counter) # Вывод: Counter({1: 4, 2: 3, 3: 2, 4: 2, 5: 1})
# print(counter[1]) # Вывод: 4 (количество вхождений элемента 1)
most_common = counter.most_common(2)
# print(most_common) # Вывод: [(1, 4), (2, 3)]

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
# print(p.x) # Вывод: 2
# print(p.y)
# print(p)


# defaultdict
d = defaultdict(list)
d['apple'].append('red') # Добавление значения 'red' к ключу 'apple'
d['banana'].append('yellow') # Добавление значения 'yellow' к ключу 'banana'
d['apple'].append('green') # Добавление значения 'green' к ключу 'apple'
# print(d) # Вывод: defaultdict(<class 'list'>, {'apple': ['red', 'green'], 'banana': ['yellow']})
# print(d['apple']) # Вывод: ['red', 'green']
# print(d['banana']) # Вывод: ['yellow']
# print(d['cherry']) # Вывод: [] (пустой список, значение по умолчанию)
# print(d) # Вывод: defaultdict(<class 'list'>, {'apple': ['red', 'green'], 'banana': ['yellow']
