from random import randint, choice

def gimn():
    print('Россия - священная наша держава,')
    print('Россия - любимая наша страна.')
    print('Могучая воля, великая слава -')
    print('Твое достоянье на все времена!')
    print('Славься, Отечество наше свободное,')
    print('Братских народов союз вековой,')
    print('Предками данная мудрость народная!')
    print('Славься, страна! Мы гордимся тобой!')
    print('От южных морей до полярного края')
    print('Раскинулись наши леса и поля.')
    print('Одна ты на свете! Одна ты такая -')
    print('Хранимая Богом родная земля!')
    print('Славься, Отечество наше свободное,')
    print('Братских народов союз вековой,')
    print('Предками данная мудрость народная!')
    print('Славься, страна! Мы гордимся тобой!')
    print('Широкий простор для мечты и для жизни')
    print('Грядущие нам открывают года.')
    print('Нам силу дает наша верность Отчизне.')
    print('Так было, так есть и так будет всегда!')
    print('Славься, Отечество наше свободное,')
    print('Братских народов союз вековой,')
    print('Предками данная мудрость народная!')
    print('Славься, страна! Мы гордимся тобой!')

def SS(a):
    """Считает количество положительных элементов"""
    g = 0
    for i in a:
        if i > 0:
            g += 1
    return g

def sus(a):
    """Сумма всех элементов в списке списков"""
    g = 0
    for i in a:
        g += sum(i)
    return g

def nip():
    """Генератор случайных буквенных строк"""
    alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    j = randint(1, randint(2, randint(3, 15)))
    g = ''
    for i in range(j):
        g += alf[randint(0, len(alf) - 1)]
    return g

def entry(s, g):
    """Поиск индекса элемента в списке списков"""
    for i in range(len(g)):
        if s in g[i]:
            return i
    return -1

def entrys(s, g):
    """Проверка наличия элемента в списке списков"""
    for i in range(len(g)):
        if s in g[i]:
            return True
    return False

def randi(g):
    """Перемешивание списка"""
    import copy
    g = copy.copy(g)
    i = []
    while len(g) != 0:
        gg = g[randint(0, len(g) - 1)]
        i.append(gg)
        g.remove(gg)
    return i

def tr(a, b, c):
    """Форматирование коэффициентов для уравнений"""
    k = [a, b, c]
    g = []
    for i in k:
        if i > 0:
            i = '+' + str(i)
        else:
            i = str(i)
        if i == '+1':
            i = '+'
        elif i == '-1':
            i = '-'
        g.append(i)
    if g[2] == '-':
        g[2] = '-1'
    if g[0][0] == '+':
        g[0] = g[0].replace(g[0][0], '', 1)
    return g[0], g[1], g[2]

def gener(dif=1):
    """Генерация квадратного уравнения"""
    chance = randint(1, 4)
    if chance == 4:
        xxx = [i for i in range(1, 26 * dif) if i % 4 == 0]
        b = xxx[randint(0, len(xxx) - 1)] * choice([-1, 1])
        c = b ** 2 // 4
        a = randint(1, 15 * dif) * choice([-1, 1])
        b, c = b * a, c * a
        x1 = -b // (a * 2)
        a, b, c = tr(a, b, c)
        f = a + 'x²' + b + 'x' + c + '=0'
        return f, str(x1)
    else:
        x1 = randint(1, 15 + dif) * choice([-1, 1])
        x2 = randint(1, 15 + dif) * choice([-1, 1])
        b = -(x1 + x2)
        c = (x1 * x2)
        while b ** 2 - 4 * c == 0:
            x1 = randint(1, 15 + dif) * choice([-1, 1])
            x2 = randint(1, 15 + dif) * choice([-1, 1])
            b = -(x1 + x2)
            c = (x1 * x2)
        a = randint(1, 15 * dif) * choice([-1, 1])
        b *= a
        c *= a
        a, b, c = tr(a, b, c)
        f = a + 'x²' + b + 'x' + c + '=0'
        return f, str(min(x1, x2)) + str(max(x1, x2))

def generA(dif=1):
    """Генерация биквадратного уравнения"""
    chanse = randint(1, 5)
    if chanse == 2:
        xx = []
        while len(xx) != 2:
            x = randint(1, 5 + dif)
            if x not in xx:
                xx.append(x)
        a = randint(1, 20) * choice([-1, 1])
        b = -(xx[0] ** 2 + xx[1] ** 2) * a
        c = (xx[0] ** 2 * xx[1] ** 2) * a
    else:
        x1 = randint(1, 5 + dif)
        xx = [x1]
        x2 = randint(1, 25) * (-1)
        a = randint(1, 20) * choice([-1, 1])
        b = -(x1 ** 2 + x2) * a
        c = (x1 ** 2 * x2) * a
    for i in xx:
        if -i not in xx:
            xx.append(-i)
    xx = sorted(xx)
    g = ''
    a, b, c = tr(a, b, c)[0], tr(a, b, c)[1], tr(a, b, c)[2]
    for i in xx:
        g += str(i)
    return a + 'x⁴' + b + 'x²' + c + '=0', g

def titr():
    print('В создании проекта приняли участие:')
    from config import TITR_AUTHORS, TITR_CREATOR
    for author in TITR_AUTHORS:
        print(author)
    print('Создатель, главная движущая и рабочая сила -', TITR_CREATOR, sep='\n')

def print_passives(state):
    """Вывод иконок активных пассивов (бывшая pp())"""
    from config import PASSIVE_SYMBOLS
    g = ''
    if sum(state.passives) == 0:
        print()
    else:
        for i in range(len(state.passives)):
            if state.passives[i] != 0:
                g += PASSIVE_SYMBOLS[i]
        print(g)

def print_stat(state):
    """Вывод статистики если активен Око (бывшая O())"""
    if state.passives[2] == 1:
        stat = state.get_stat()
        for i in stat:
            print(i, end=' ')
        print()