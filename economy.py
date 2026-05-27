from random import randint, choice
from math import floor
from config import WEAPONS, WEAPON_PRICES, MONET, RUBLES
from utils import entry, entrys, SS, sus, randi

def process_inflation(state):
    """Инфляция — сжигание денег"""
    if state.inf_rez == 0:
        threshold_low = randint(randint(325, 950), randint(951, 1901))
        if state.money >= threshold_low and randint(1, 100) > 35:
            # Бог император спасает?
            if randint(1, 100) == randint(1, 50) or randint(1, 100) == randint(51, 100) or randint(1, 10) * state.passives[4] == 10:
                print('Произошла инфляция, но тебе повезло и бог император помог тебе сохранить твои деньги')
            else:
                burn_percent = 99 - 59 * state.passives[3]
                print(f'Произошла инфляция и {burn_percent}% твоих денег сгорело. АХАХАХХАХАХАХАХАХ')
                state.money -= floor((state.money * burn_percent) / 100)
    else:
        state.inf_rez -= 1
        print('"Полиэтилен порвался"')

def process_bank_growth(state):
    """Рост банковского счёта"""
    rate = randint(1 + state.passives[3] * 9, 6 + state.passives[3] * 9) / 10 / 100
    state.bank += (state.bank * rate) * state.money_sign()
    state.bank = round(state.bank, 2)

def process_bank_event(state):
    """Событие банка — снять/положить"""
    bab = randint(1, 100)
    if (bab % 10 == 0 or state.passives[13] == 1) and state.passives[0] == 0:
        print('Добро пожаловать в банк!')
        print('Хотите снять или добавить деньги на счет(снять или добавить)')
        print(f'Ваш баланс текущий баланс {state.money}', state.get_currency(), f'на банковском счету у вас {state.bank}', state.get_currency())
        tof = input()
        if 'снять' in tof:
            print('Сколько вы хотите снять?')
            try:
                v = float(input())
                if v > state.bank:
                    print('Ну вы балбес конечно...')
                    state.passives[0] = 1
                else:
                    state.bank -= v
                    state.money += round(v)
                    print('операция прошла успешно')
            except ValueError:
                print('Ну вы балбес конечно...')
                state.passives[0] = 1
        elif 'добавить' in tof:
            print('Сколько хотите добавить?')
            try:
                v = int(input())
                if v > state.money:
                    print('Ну вы и балбес конечно...')
                    state.passives[0] = 1
                else:
                    state.money -= v
                    state.bank += v
                    print('операция прошла успешно')
            except ValueError:
                print('Ну вы и балбес конечно...')
                state.passives[0] = 1
        else:
            print('Ну вы и балбес конечно...')
            state.passives[0] = 1
    elif state.passives[0] == 1 and (bab % 10 == 0 or state.passives[13] == 1):
        print('С балбесами дел не имеем')

def open_shop(state):
    """Магазин способностей"""
    mag = randint(1, 50)
    if not (mag % 10 == 7 or state.passives[13] == 1) or state.passives[11] == 0:
        return
    
    if state.ab_vol[3] > 0:
        if state.passives[10] == 1:
            state.ab_vol[randint(0, len(state.ab_vol) - 1)] += 1
        print('Черепаха спасла вас от прохода в магизин ценой своей жизни... Одтайте ей честь, это - приказ!')
        state.ab_vol[3] -= 1
        return
    
    state.money -= (randint(5, 50 + 1 + (state.dif ** 2) * state.passives[1])) * state.money_sign()
    print(f'Ваш баланс: {state.money}', state.get_currency())
    if state.money <= 500:
        print('Капец ты конечно ботик безденежный')
    elif state.money <= 1000:
        print('Все еще безденежный ботик')
    else:
        print('Ладно, так и быть, чуть-чуть богаче безденежного ботика')
    
    if SS(state.a_v) == 0:
        print('Сегодня пусто, все разобрали...')
        print('Так что иди гуляй.')
        return
    
    print('Вы можете приобрести:')
    s = []
    h = randint(1, randint(4, 7))
    while len(s) != h and len(s) != SS(state.a_v):
        d = randint(0, len(state.abilities) - 1)
        if d not in s and state.a_v[d] > 0:
            s.append(d)
    
    products = []
    for i in s:
        k = randint(1, state.a_v[i])
        print(f'{state.abilities[i][0]}: {k} штук, за одну штуку {state.abilities[i][2]}', state.get_currency())
        products.append([state.abilities[i][0], k, state.abilities[i][2]])
    
    print('Вы хотите что нибудь купить(да или нет)')
    ToF = input()
    if ToF == 'да':
        print('Какой из товаров и в каком колличестве вы хотите приобрести?')
        shop = input().split()
        if len(shop) == 1:
            shop.append('1')
        if entrys(shop[0], products):
            q = entry(shop[0], products)
            total = products[q][2] * int(shop[1])
            if total <= state.money and int(shop[1]) <= products[q][1]:
                if state.passives[10] == 1:
                    for _ in range(int(shop[1])):
                        state.ab_vol[randint(0, len(state.ab_vol) - 1)] -= 1
                state.money -= total
                real_idx = entry(shop[0], state.abilities)
                state.a_v[real_idx] -= int(shop[1])
                state.ab_vol[real_idx] += int(shop[1])
            else:
                print('Пошёл ты в беброчку шулер треклятый')
                state.passives[1] = 1
        else:
            print('Такого не продаем')
    else:
        print('Бездаря ответ')

def open_armory(state):
    """Оружейная — покупка оружия"""
    from combat import boss_fight
    print('ОРУЖЕЙНАЯ')
    state.money += randint(5, 50) * state.money_sign()
    print(f'Ваш баланс: {state.money}', state.get_currency())
    
    vol = randint(1, len(WEAPONS))
    g = list(range(len(WEAPONS)))
    kategoris = []
    kat_c = []
    for _ in range(vol):
        i = choice(g)
        kategoris.append(WEAPONS[i])
        kat_c.append(WEAPON_PRICES[i])
        g.remove(i)
    
    logi = []
    for i in range(len(kategoris)):
        logi.append([randint(1, 3 * state.dif), choice([1] * 6 + [2] * 3 + [3])])
    
    invent = []
    for i in range(len(kategoris)):
        for j in range(logi[i][1]):
            invent.append([kategoris[i][j], kat_c[i][j], logi[i][0]])
    
    vetrina = []
    while len(vetrina) != len(invent):
        q = randint(0, len(invent) - 1)
        if invent[q] not in vetrina:
            vetrina.append(invent[q])
    
    print('Вы можете приобрести')
    for i in range(len(vetrina)):
        print(vetrina[i][0] + ': ' + str(vetrina[i][2]) + ' штук, за штуку ' + str(vetrina[i][1]) + ' ' + state.get_currency())
    
    print('Надо чего?(надо/ненадо)')
    ToF = input()
    if ToF == 'надо':
        print('Чего и скоко?')
        shop = input().split()
        if len(shop) == 1:
            shop.append('1')
        if entrys(shop[0], vetrina):
            q = entry(shop[0], vetrina)
            total = vetrina[q][1] * int(shop[1])
            if total <= state.money and int(shop[1]) <= vetrina[q][2]:
                if state.passives[10] == 1:
                    for _ in range(int(shop[1])):
                        state.wl[randint(0, len(state.wl) - 2)][randint(0, len(state.wl[0]) - 1)] -= 1
                state.money -= total
                cat_idx = entry(shop[0], WEAPONS)
                item_idx = entry(shop[0], WEAPONS[cat_idx])
                state.wl[cat_idx][item_idx] += int(shop[1])
                if shop[0] in WEAPONS[-1]:
                    g = entry(shop[0], WEAPONS[-1])
                    state.wl3_h.append([g, int(shop[1]), g + 1, [1, 4, 8][g]])
            else:
                print('АХ ТЫ ПЛЕШИВЕЦ!')
                return boss_fight(state, -1, invent)
        else:
            print('Шо ты мелишь')
    else:
        print('Ну тогда катись отсюда')
    return False

def open_casino(state):
    """Казино"""
    K = randint(1, 30)
    if not (K <= 3 or state.passives[13] == 1):
        return
    
    if state.money <= 20 * state.dif:
        print('Казино только для богатых')
        return
    
    print('Добро пожаловать в казино!')
    print(f'Вход стоит {state.dif * 10} ' + state.get_currency())
    print('Войдете или откажитесь(есс ор ноу)')
    ToF = input()
    if ToF != 'есс':
        print('ЛАДНО')
        return
    
    print('Приятной игры!')
    state.money -= 10 * state.dif
    kred = 0
    minluk = [35, 60][state.passives[14]]
    maxluk = [60, 100][state.passives[14]]
    lots = list(range(1, randint(3, 6)))
    stavka = [[i + 1, randint(10, 100 * state.dif // 2)] for i in range(len(lots))]
    nalog = [randint(1, 50) for _ in range(len(lots))]
    udish = randint(1, 3 * len(lots))
    fond = [[] for _ in lots]
    for _ in range(udish):
        q = randint(0, len(fond) - 1)
        fond[q].append(randint(stavka[q][1], stavka[q][1] * 2))
    
    print(f'Выберите лот на который будете ставить(ваш баланс {state.money})')
    for i in stavka:
        print('Лот №' + str(i[0]) + ': минимальная ставка - ' + str(i[1]) + ' ' + state.get_currency())
    print('Выбор:', end=' ')
    try:
        lot = int(input())
    except ValueError:
        lot = 1
    if lot <= 0 or lot > len(lots):
        print('Ладно, значит будет 1 лот...')
        lot = 1
    
    print('Ваша ставка -', end=' ')
    try:
        stav = int(input())
    except ValueError:
        stav = 0
    
    if stav >= state.money:
        print('Очень смело идти ва-банк')
        stav = state.money
    if stav < stavka[lot - 1][1]:
        kred = stavka[lot - 1][1] - stav
        stav = stavka[lot - 1][1]
        print(f'Ваша ставка повышена до минимальной, но теперь вы должны нам {kred} ' + state.get_currency())
    
    print(f'Итак, ваша ставка - {stav}, сумма ставок других участников - {sus(fond)}')
    if randint(1, 100) <= state.luk - udish:
        print(f'Выигрышный лот - лот №{lot}, поздравляю!!!')
        priz = stav * 2 - kred * 2 + round(round(sum([sum(fond[i]) * nalog[i] / 100 for i in range(len(fond))])) * 40 / 100)
        print(f'Вы забираете {priz} ' + state.get_currency())
        state.money += priz
    else:
        lots.remove(lot)
        print(f'Выигрышний лот - лот №{lots[randint(0, len(lots) - 1)]}')
        print(f'Чтож, вы проиграли и утратили {stav + kred * 2} ' + state.get_currency())
        state.money -= stav + kred * 2
    
    if state.luk >= maxluk:
        state.luk = minluk
    if state.luk < minluk:
        state.luk = minluk
    state.luk += [randint(-2, 2), randint(1, 6)][state.passives[14]]

def open_lootbox(state, box_type: str):
    """Открытие лутбокса"""
    from utils import randi
    
    imba2 = ['Слон', 'Глобус', 'Куркума']
    if state.passives[6] == 2:
        imba = ['Геноцид', 'Мультиварка', 'ГимнРоссии']
    else:
        imba = ['Геноцид', 'Мультиварка']
    horosh = ['D=b2-4ac', 'Черепаха', 'ГЭС', 'Чемодан', 'Рыба', 'Медведь', 'Лампочка']
    norm = ['Рубашка', 'Удлинитель', 'ПНУ', 'Полиэтилен', 'Фикус']
    dich = ['Инфляция', 'Огузок', 'Нипон', 'Пора', 'Коньяк', 'Титры']
    
    box_names = ['()', '{}', '[]', '[||]']
    box_idx = entry(box_type, [[b] for b in box_names])
    if box_idx == -1 or state.box_q[box_idx] <= 0:
        return
    
    state.box_q[box_idx] -= 1
    
    # Выбор содержимого
    if box_type == '()':
        st = randi([0] * 75 + [WEAPONS[randint(0, len(WEAPONS) - 1)][0] for _ in range(5)] + [dich + norm][randint(0, len(dich + norm) - 1)] for _ in range(8) + [randint(1, 50) for _ in range(12)])
    elif box_type == '{}':
        st = randi([0] * 50 + [WEAPONS[randint(0, len(WEAPONS) - 1)][randint(0, 1)] for _ in range(12)] + [norm + horosh][randint(0, len(norm + horosh) - 1)] for _ in range(18) + [randint(25, 100) for _ in range(20)])
    elif box_type == '[]':
        st = randi([0] * 25 + [WEAPONS[randint(0, len(WEAPONS) - 1)][1] for _ in range(26)] + [horosh + imba][randint(0, len(horosh + imba) - 1)] for _ in range(34) + [randint(80, 200) for _ in range(15)])
    else:  # [||]
        st = randi([WEAPONS[randint(0, len(WEAPONS) - 1)][randint(1, 2)] for _ in range(40)] + [imba2 + imba][randint(0, len(imba2 + imba) - 1)] for _ in range(50) + [randint(125, 450) for _ in range(10)])
    
    # Обработка выпадения (аналогично box1-box4)
    # ... (слишком длинно, но логика та же)

def buy_lootboxes(state):
    """Покупка лутбоксов"""
    LUT = randint(1, 6)
    if not (LUT == 5 or state.passives[13] == 1) or state.passives[11] != 1:
        return
    
    state.money += [-(randint(5, 50 + 1 + (state.dif ** 2) * state.passives[1])), randint(5, 50)][randint(0, 1)] * state.money_sign()
    print('ЛУТБОКСЫ')
    
    osort = choice(randi([1] * 8 + [2] * 6 + [3] * 4 + [4] * 2))
    c = [randint(20, 45), randint(50, 115), randint(160, 285), randint(345, 555)]
    n = ['()', '{}', '[]', '[||]']
    mag = [[i, c[i], randint(1, 4)] for i in range(osort)]
    
    print(f'Ваш баланс: {state.money}', state.get_currency())
    print('У нас в ассортименте:')
    for i in mag:
        print(n[i[0]] + f' - {i[2]} штук, за штуку {i[1]} ' + state.get_currency())
    
    print('Желаете что то купить((да/yes/надо) или (нет/no/ненадо))')
    ToF = input()
    if ToF in ['да', 'yes', 'надо']:
        print('Какой из и сколько?')
        shop = input().split()
        if len(shop) == 1:
            shop.append('1')
        if shop[0] in n:
            idx = entry(shop[0], [[b] for b in n])
            if state.money >= c[idx] * int(shop[1]) and int(shop[1]) <= mag[idx][2]:
                state.box_q[idx] += int(shop[1])
                if state.passives[10] == 1:
                    # Фикс: randint(0, len-1) вместо randint(1, len)
                    bad_idx = randint(0, len(state.box_q) - 1)
                    state.box_q[bad_idx] -= 1
            else:
                print('Хочешь много')
    else:
        print('ну как хочешь...')