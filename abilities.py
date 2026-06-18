from random import randint
from config import ABILITIES_DATA, MONET, RUBLES, WIN_PHRASES, ALMOST_WIN_PHRASES, LOSE_PHRASES, ALCOHOL_DEATH
from utils import entry, entrys, SS, nip, gener, generA, gimn, titr
from minigame import game_basic, game_amulet

def use_slon(state, target: int):
    """Слон — показывает разброс и запускает угадай число"""
    state.ab_vol[0] -= 1
    print(f'разброс от {target - randint(1, 3)} до {target + randint(1, 3)}')
    if state.passives[9] == 1:
        game_amulet(state, input().split(), 1 + state.dif, target)
    else:
        guess = input("Введите число: ")
        game_basic(state, int(guess), target)

def use_genocide(state, raw_input: str, target: int):
    """Геноцид — стреляем по списку чисел"""
    state.ab_vol[1] -= 1
    print('Кого стреляем?')
    nums = [int(i) for i in raw_input.split()]
    limit = 10 * randint(1, state.dif)
    
    if len(nums) > limit:
        print('Будь поосторожней с Геноцидом, ведь он может задеть и тебя!')
        return True  # смерть
    
    if target in nums:
        print(WIN_PHRASES[randint(0, len(WIN_PHRASES) - 1)])
        state.money += randint(250, 526 * state.dif) * state.money_sign()
        state.wins += 1
    elif (target + 1 in nums) or (target - 1 in nums):
        print(ALMOST_WIN_PHRASES[randint(0, len(ALMOST_WIN_PHRASES) - 1)])
        state.money += randint(5, 10 * state.dif) * state.money_sign()
        state.pwins += 1
    else:
        print(LOSE_PHRASES[randint(0, len(LOSE_PHRASES) - 1)])
        state.money -= state.dif * state.money_sign()
        state.nwins += 1
    return False

def use_rubashka(state, target: int):
    """Рубашка — показывает ложные числа"""
    state.ab_vol[2] -= 1
    aaa = []
    for _ in range(1 + randint(1, 11 * state.dif) * state.passives[5]):
        aa = [randint(0, target - 1), randint(target + 1, 51 * state.dif)]
        aaa.append(aa[randint(0, 1)])
    print('Это не', end=' ')
    for i in aaa:
        print(i, end=' ')
    print()
    if state.passives[9] == 1:
        game_amulet(state, input().split(), 1 + state.dif, target)
    else:
        game_basic(state, int(input()), target)

def use_cherepakha(state):
    """Черепаха — +1 монета"""
    state.money += 1
    state.ab_vol[3] -= 1

def use_inflyaciya(state):
    """Инфляция — обработка инфляции"""
    state.ab_vol[4] -= 1
    from economy import process_inflation
    process_inflation(state)

def use_discriminant(state, target: int):
    """D=b2-4ac — решение квадратного уравнения"""
    state.ab_vol[5] -= 1
    if state.passives[7] == 0:
        D = gener(state.dif)
    else:
        D = generA(state.dif)
    print(D[0])
    if state.passives[0] == 1:
        print('Для балбесов: ответ -', D[1])
    print('Ответ:(jn меньшего к большему, без пробелов)', end=' ')
    otv = input("Ответ (от меньшего к большему, без пробелов): ")
    if otv == D[1]:
        print(f'Неплох, держи 60^2/120*dif', state.get_currency())
        state.money += (30 * state.dif) * state.money_sign()
    else:
        currency = RUBLES[1] if state.passives[3] else MONET[1]
        print(f'Такое не прощается, С ДНЕМ', currency, '! УРААААААА!!!')
        state.money = 1

def use_udlinitel(state):
    """Удлинитель — +1 сложность"""
    state.ab_vol[6] -= 1
    state.dif += 1
    print('Мне кажется что то изменилось...')

def use_konyak(state):
    """Коньяк — смерть"""
    state.ab_vol[7] -= 1
    print(ALCOHOL_DEATH[randint(0, len(ALCOHOL_DEATH) - 1)])
    return True  # смерть

def use_globus(state):
    """Глобус — получить любую способность"""
    state.ab_vol[8] -= 1
    print('Какую способность надобно?')
    spos = input()
    if not entrys(spos, state.abilities):
        print('Ты по мойму перепутал...')
    else:
        idx = entry(spos, state.abilities)
        state.ab_vol[idx] += 1
        print('Надо было выбирать викингов...')

def use_kurkuma(state):
    """Куркума — +1 ко всем способностям"""
    print('СИЛА КУРКУМЫ')
    for i in range(len(state.ab_vol)):
        state.ab_vol[i] += 1
    state.ab_vol[9] -= 2  # саму куркуму тратим

def use_chemodan(state):
    """Чемодан — случайная способность"""
    q = randint(0, len(state.ab_vol) - 1)
    state.ab_vol[q] += 1
    print(f'Выпадает {state.abilities[q][0]}')
    state.ab_vol[10] -= 1

def use_pnu(state, target: int):
    """ПНУ — противотанковая немецкая установка"""
    state.ab_vol[11] -= 1
    ddd = randint(1, 20)
    print('Противотанковая Немецкая Установка делает выстрел ииииииии...')
    if ddd == randint(1, 20):
        print(f'говорит правильный ответ - {target}, НЕВЕРОЯТНО, ВОТ ЭТО ДА')
        print('Жаль одноразовая...')
    else:
        print('БАБАХ')
    if state.passives[9] == 1:
        game_amulet(state, input().split(), 1 + state.dif, target)
    else:
        game_basic(state, int(input()), target)

def use_oguzok(state):
    """Огузок — ничего не делает"""
    state.ab_vol[12] -= 1
    print('Ты думал тут что-то будет?')

def use_ges(state):
    """ГЭС — казино на деньги"""
    state.ab_vol[13] -= 1
    k = randint(-50 * state.dif, 50 * state.dif) * state.money_sign()
    
    if k > 0:
        print(f'Вы окупились на {k}', state.get_currency(), '!')
    elif k == 0:
        print('Вы вышли в ноль, неплохо')
    elif randint(1, 10) == 1:
        if state.katastrof == 0:
            state.katastrof += 1
            print('Из за вашей ГЭС произошла крупная экологическая катастрофа, огромное колличество животных умерло, вы понесли КОЛОСАЛЬНЫЕ убытки!!!')
            # Уничтожаем животных
            for idx in [0, 3, 17, 19, 20, 21]:
                state.ab_vol[idx] = -(10 ** 10)
                state.a_v[idx] = 0
            k -= (abs(int(state.money * 75 / 100)) + abs(k * (2 * randint(1, state.dif)))) * state.money_sign()
        else:
            state.katastrof += 1
            print('Из за ГЭС снова произошла экологическая катастрофа, но на этот раз все обошлось только лишь КОЛОСАКЛЬНЫМИ убытками...')
            k -= (abs(int(state.money * 75 / 100)) + abs(k * (2 * randint(1, state.dif)))) * state.money_sign()
    else:
        print(f'Ваши убытки составили {k}', state.get_currency())
    state.money += k

def use_lampochka(state, target: int):
    """Лампочка — инвентарь или разброс"""
    state.ab_vol[14] -= 1
    if state.passives[2] == 0:
        print('Ваш инвентарь:')
        if sum(state.ab_vol) <= 0:
            print('Пусто')
        else:
            for i in range(len(state.ab_vol)):
                if state.ab_vol[i] != 0:
                    print(f'{state.abilities[i][0]}: {state.ab_vol[i]} штук')
    else:
        print(f'Разброс jn {target - randint(1, 50 * state.dif // 4)} lj {target + randint(1, 50 * state.dif // 4)}')
        if state.passives[9] == 1:
            game_amulet(state, input().split(), 1 + state.dif, target)
        else:
            game_basic(state, int(input()), target)

def use_polietilen(state):
    """Полиэтилен — защита от инфляции"""
    state.inf_rez += 1
    state.ab_vol[15] -= 1
    print('Его надолго не хватит...')

def use_multivarka(state):
    """Мультиварка — выбор из случайных способностей"""
    state.ab_vol[16] -= 1
    print('Какую выберешь?')
    s = []
    h = randint(1, randint(1, len(state.abilities)))
    while len(s) != h:
        d = randint(0, len(state.abilities) - 1)
        if d not in s:
            s.append(d)
    products = []
    for i in s:
        print(state.abilities[i][0])
        products.append(state.abilities[i][0])
    print('Выбор:', end=' ')
    shop = input().split()
    if entrys(shop[0], [[p] for p in products]):
        idx = entry(shop[0], [[p] for p in products])
        real_idx = s[idx]
        state.ab_vol[real_idx] += 1
        print('Неплохой выбор, но вон та способность подошла бы больше...')
    else:
        print('Не хочешь, как хочешь...')

def use_ryba(state):
    """Рыба — магазин способностей по завышенным ценам"""
    state.ab_vol[17] -= 1
    print('Вы можете купить у рыбы:')
    s = []
    h = randint(1, randint(3, 4))
    while len(s) != h and len(s) != SS(state.a_v):
        d = randint(0, len(state.abilities) - 1)
        if d not in s and state.a_v[d] > 0:
            s.append(d)
    
    if not s:
        print('Рыба сегодня без улова...')
        return
    
    products = []
    for i in s:
        k = randint(1, state.a_v[i])
        price = state.abilities[i][2] * 2 + 1
        print(f'{state.abilities[i][0]}: {k} штук, за одну штуку {price}', state.get_currency())
        products.append([state.abilities[i][0], k, price])
    
    print('Do you want to buy something?(yes или no)')
    ToF = input()
    if ToF == 'yes':
        print('Че из и по скоку вы хотите приобрести?')
        shop = input().split()
        if len(shop) == 1:
            shop.append('1')
        if entrys(shop[0], products):
            q = entry(shop[0], products)
            total_price = products[q][2] * int(shop[1])
            if total_price <= state.money and int(shop[1]) <= products[q][1]:
                if state.passives[10] == 1:
                    for _ in range(int(shop[1]) + 1):
                        state.ab_vol[randint(0, len(state.ab_vol) - 1)] -= 1
                state.money -= total_price
                real_idx = entry(shop[0], state.abilities)
                state.a_v[real_idx] -= int(shop[1])
                state.ab_vol[real_idx] += int(shop[1])
            else:
                print('Обманывать не хорошо, ая-яй!')
                state.passives[1] = 1
        else:
            print('Нет такой буквы!')
    else:
        print('А вот это уже явно не моя проблема...')

def use_nipon(state):
    """Нипон — случайная строка"""
    state.ab_vol[18] -= 1
    print(nip())

def use_medved(state):
    """Медведь — оружейная"""
    from economy import open_armory
    dead = open_armory(state)
    state.ab_vol[19] -= 1
    return dead

def use_pora(state):
    """Пора — лор"""
    print('Поры представляют собой отверстия на поверхности клетки, обычно расположенные на неживых участках зеленых органов растений, таких как листья и стебли. Главной функцией пор является регуляция газообмена, позволяя растительным клеткам получать необходимый уровень кислорода и выводить избыток углекислого газа, который образуется в процессе фотосинтеза.Кроме того, поры также отвечают за регуляцию водного баланса растения.')
    state.ab_vol[20] -= 1

def use_fikus(state):
    """Фикус — рандомизирует банк и удачу"""
    state.ab_vol[21] -= 1
    state.bank = [state.bank + round(state.bank / 10), state.bank - round(state.bank / 10)][randint(0, 1)]
    state.luk = [state.luk - 1, state.luk + 1][randint(0, 1)]
    print('Фикус сделал все что мог...')

def use_gimn(state):
    """Гимн России — автопобеда"""
    state.wins += 1
    state.ab_vol[-1] -= 1
    if state.passives[12] == 1 and state.dif != 1:
        state.dif -= 1
    gimn()

def use_titry(state):
    """Титры — авторы"""
    titr()
    state.ab_vol[22] -= 1