from random import randint, choice
from config import WEAPONS, BOSS_NAMES, MONET, RUBLES
from utils import entry, entrys, sus

def player_hit(state, weapon_name: str, kof: int = 0):
    """Атака по боссу"""
    w1 = [randint(1, 8), randint(1, 20), sum([randint(1, 12) for _ in range(randint(1, 6))])]
    if weapon_name != '1к4':
        damage = w1[entry(weapon_name, WEAPONS[0])]
        state.wl[0][entry(weapon_name, WEAPONS[0])] -= 1
    else:
        damage = randint(1, 4)
    print(f'Выпадает {damage}' + ['!', '!(+Пила Струна)'][state.passives[15]])
    bonus = randint(5, 15) if state.passives[15] else 0
    if kof == 2:
        state.boss_hp -= (damage + bonus) // 4
    else:
        state.boss_hp -= damage + bonus
    if state.passives[10] == 1:
        state.wl[randint(0, len(state.wl) - 2)][randint(0, len(state.wl[0]) - 1)] += 1

def player_heal(state, item_name: str):
    """Лечение"""
    w2 = [20, 50, 105]
    if item_name not in ['Пластырь', 'Медведь']:
        damage = w2[entry(item_name, WEAPONS[1])]
        state.wl[1][entry(item_name, WEAPONS[1])] -= 1
    elif item_name == 'Медведь' and state.passives[15] == 1 and state.ab_vol[19] > 0:
        damage = 35
        state.ab_vol[19] -= 1
    else:
        damage = 10
    print(f'Вы восстановили {damage} HP!')
    state.hp += damage
    if state.passives[10] == 1:
        state.wl[randint(0, len(state.wl) - 2)][randint(0, len(state.wl[0]) - 1)] += 1

def player_turn(state, kof: int = 0):
    """Ход игрока в бою"""
    print('Ваш ход(используйте 1 из способностей(чукчи, сеньоры и космодесантники являются пассивными способностями))')
    hod_name = input()
    
    if hod_name in WEAPONS[0] and state.wl[0][entry(hod_name, WEAPONS[0])] > 0 or (state.passives[16] == 1 and hod_name == '1к4'):
        player_hit(state, hod_name, kof)
    elif (hod_name in WEAPONS[1] and state.wl[1][entry(hod_name, WEAPONS[1])] > 0) or \
         (state.passives[16] == 1 and hod_name == 'Пластырь') or \
         (state.passives[15] == 1 and hod_name == 'Медведь' and state.ab_vol[19] > 0):
        player_heal(state, hod_name)
    else:
        print('Ты помойму перепутал')

def wait_enter():
    print('Вам нечего использовать...')
    print('"нажмите enter"', end=' ')
    input()

def transform_wl3(state):
    """Трансформация пассивных юнитов"""
    to_remove = []
    for i, unit in enumerate(state.wl3_h):
        if unit[0] < 0:
            state.wl[-1][unit[0] + unit[2]] -= unit[1]
            to_remove.append(i)
    # Удаляем в обратном порядке
    for idx in reversed(to_remove):
        state.wl3_h.pop(idx)
    
    for i in range(len(state.wl3_h)):
        if state.wl3_h[i][2] == 2:
            state.wl3_h[i][-1] += 2
        else:
            state.wl3_h[i][-1] *= 2

def boss_fight(state, kof: int = None, invent=None):
    """Бой с боссом"""
    if kof is None:
        kof = randint(0, len(BOSS_NAMES) - 2)  # -1 чтобы не попасть на Оружейника случайно
    
    print('На вас напал ' + BOSS_NAMES[kof])
    
    # Пассивный урон от юнитов
    pas_damage = 0
    pil = qq = v = 0
    
    if state.wl3_h:
        for unit in state.wl3_h:
            if kof != 2:
                pas_damage += unit[1] * unit[-1]
            else:
                pas_damage += unit[1] // 8 * unit[-1]
    
    # === ТАНОС ===
    if kof == 0:
        state.boss_hp = 150
        while state.boss_hp > 0 and state.hp > 0:
            print(f'Ваше HP:{state.hp}, HP ' + BOSS_NAMES[kof] + f': {state.boss_hp}')
            print(BOSS_NAMES[kof] + f' атакует и наносит {state.hp // 2 + state.hp % 2} урона.')
            state.hp //= 2
            state.boss_hp -= state.hp // 2
            print(f'Ваши солдаты нанесли {pas_damage} урона')
            state.boss_hp -= pas_damage
            if sus(state.wl[:-1]) != 0 or state.passives[16] == 1 or (state.ab_vol[19] > 0 and state.passives[15] == 1):
                player_turn(state)
            else:
                wait_enter()
    
    # === ТЗИНЧ ===
    elif kof == 1 and state.passives[4] == 0:
        state.boss_hp = -1
        while state.hp > 0:
            print(f'Ваше HP:{state.hp}, HP ' + BOSS_NAMES[kof] + f': {state.boss_hp}')
            c = randint(1, 5)
            print('УгОдАй ЧиСлО jN -10000000000 до 1000000000')
            try:
                h = int(input())
            except ValueError:
                h = 0
            if h == c:
                print('ВыБиРаЙ: ДеНьГи ИлИ оСоБыЙ пРиЗ(2 иЛи 1 СоОтВеТсТвЕнНо)')
                try:
                    v = int(input())
                except ValueError:
                    v = 0
                break
            else:
                print(BOSS_NAMES[kof] + f' атакует и наносит {-1 * state.boss_hp} урон.')
                state.hp += state.boss_hp
                if randint(1, 20) == 5:
                    print('Ты Не СмОжЕшЬ еСлИ нЕ пОсМоТрИшЬ в КоД')
            print(f'Ваши солдаты нанесли {pas_damage} урона')
            state.boss_hp -= pas_damage
            if sus(state.wl[:-1]) != 0 or state.passives[16] == 1 or (state.ab_vol[19] > 0 and state.passives[15] == 1):
                player_turn(state)
            else:
                wait_enter()
    
    elif kof == 1 and state.passives[4] != 0:
        print("Тзинч хотел на вас напасть, но Бог Император защитил вас")
        return False
    
    # === СТРАЖ ХОРОГРАДА ===
    elif kof == 2:
        state.boss_hp = 75
        while state.hp > 0 and state.boss_hp > 0:
            print(f'Ваше HP:{state.hp}, HP ' + BOSS_NAMES[kof] + f': {state.boss_hp}')
            damag = randint(1, 15)
            print(BOSS_NAMES[kof] + f' атакует и наносит {damag} урона.')
            state.hp -= damag
            print(f'Ваши солдаты нанесли {pas_damage} урона')
            state.boss_hp -= pas_damage
            if sus(state.wl[:-1]) != 0 or state.passives[16] == 1 or (state.ab_vol[19] > 0 and state.passives[15] == 1):
                player_turn(state, kof)
            else:
                wait_enter()

    # === ВОР ===
    elif kof == 3:
        state.boss_hp = 10
        while state.hp > 0 and state.boss_hp > 0:
            kraz = randint(1, randint(1, randint(1, randint(1, randint(1, randint(1, randint(1, randint(1, 10000))))))))
            print(f'Вор украл у вас {kraz} ' + state.get_currency())
            state.boss_hp += kraz
            state.money -= kraz
            print(f'Ваше HP:{state.hp}, HP ' + BOSS_NAMES[kof] + f': {state.boss_hp}')
            print(BOSS_NAMES[kof] + f' атакует и наносит {state.boss_hp // 10} урона.')
            state.hp -= state.boss_hp // 10
            print(f'Ваши солдаты нанесли {pas_damage} урона')
            state.boss_hp -= pas_damage
            if sus(state.wl[:-1]) != 0 or state.passives[16] == 1 or (state.ab_vol[19] > 0 and state.passives[15] == 1):
                player_turn(state)
            else:
                wait_enter()

    # === ВЫЖИВАЛОВО ===
    elif kof == 4:
        state.boss_hp = 80
        zvero = sum([state.ab_vol[i] for i in [0, 3, 17, 19] if state.ab_vol[i] > 0])
        if zvero > 0:
            state.boss_hp += zvero * 5
            for i in [0, 3, 17, 19]:
                if state.ab_vol[i] > 0:
                    state.ab_vol[i] = 0
            print('Хорошая животина, на сытый желудок можно и побиться')
            print('"Достает пилу струну"')
            pil = 1
        while state.hp > 0 and state.boss_hp > 0:
            print(f'Ваше HP:{state.hp}, HP ' + BOSS_NAMES[kof] + f': {state.boss_hp}')
            atak = [randint(1, 15), randint(10, 20)][pil]
            print(BOSS_NAMES[kof] + f' атакует и наносит {atak} урона.')
            state.hp -= atak
            print(f'Ваши солдаты нанесли {pas_damage} урона')
            state.boss_hp -= pas_damage
            if sus(state.wl[:-1]) != 0 or state.passives[16] == 1 or (state.ab_vol[19] > 0 and state.passives[15] == 1):
                player_turn(state)
            else:
                wait_enter()
            if pil == 1 and randint(1, 2) == 2:
                atak = randint(1, 15)
                print(BOSS_NAMES[kof] + f' атакует и наносит {atak} урона.')
                state.hp -= atak

    # === ОРУЖЕЙНИК (kof == -1) ===
    elif kof == -1:
        qq = 1
        h = [20, 50, 105, 10]
        state.boss_hp = 100
        kategorys = [[], [], []]
        for i in invent:
            cat_idx = entry(i[0], WEAPONS)
            if cat_idx == -1:
                cat_idx = 2
            item_idx = entry(i[0], WEAPONS[cat_idx])
            kategorys[cat_idx].append([item_idx, i[-1]])
        
        atak = kategorys[0]
        hil = kategorys[1]
        sold = kategorys[2]
        pasD = 0
        for i in sold:
            pasD += [1, 4, 8][i[0]] * i[1]
        
        while state.hp > 0 and state.boss_hp > 0:
            print(f'Ваше HP:{state.hp}, HP ' + BOSS_NAMES[kof] + f': {state.boss_hp}')
            print(f'Солдаты Оружейника нанесли вам {pasD} урона')
            state.hp -= pasD
            d = [randint(1, 8), randint(1, 20), sum([randint(1, 12) for _ in range(randint(1, 6))]), randint(1, 4)]
            
            if len(hil) > 0 and len(atak) > 0:
                if state.boss_hp >= state.hp:
                    print('Оружейник использует ' + WEAPONS[0][atak[-1][0]])
                    print(f'Выпадает {d[atak[-1][0]]}!')
                    state.hp -= d[atak[-1][0]]
                    atak[-1][-1] -= 1
                else:
                    print('Оружейник использует ' + WEAPONS[1][hil[-1][0]])
                    state.boss_hp += h[hil[-1][0]]
                    hil[-1][-1] -= 1
            elif len(hil) > 0 and len(atak) == 0:
                if randint(1, 20) > 11:
                    print('Оружейник использует 1к4')
                    print(f'Выпадает {d[-1]}!')
                    state.hp -= d[-1]
                else:
                    print('Оружейник использует ' + WEAPONS[1][hil[-1][0]])
                    state.boss_hp += h[hil[-1][0]]
                    hil[-1][-1] -= 1
            elif len(hil) == 0 and len(atak) > 0:
                if randint(1, 20) <= 11:
                    print('Оружейник использует ' + WEAPONS[0][atak[-1][0]])
                    print(f'Выпадает {d[atak[-1][0]]}!')
                    state.hp -= d[atak[-1][0]]
                    atak[-1][-1] -= 1
                else:
                    print('Оружейник использует пластырь')
                    state.boss_hp += h[-1]
            else:
                if randint(1, 2) == 1:
                    print('Оружейник использует 1к4')
                    print(f'Выпадает {d[-1]}!')
                    state.hp -= d[-1]
                else:
                    print('Оружейник использует пластырь')
                    state.boss_hp += h[-1]
            
            # Чистка пустых элементов — безопасно
            hil = [x for x in hil if x[-1] > 0]
            atak = [x for x in atak if x[-1] > 0]
            
            print(f'Ваши солдаты нанесли {pas_damage} урона')
            state.boss_hp -= pas_damage
            if sus(state.wl[:-1]) != 0 or state.passives[16] == 1 or (state.ab_vol[19] > 0 and state.passives[15] == 1):
                player_turn(state)
            else:
                wait_enter()

    # === ФИНАЛ БОЯ: награды и проверка смерти ===
    for i in range(len(state.wl3_h)):
        state.wl3_h[i][0] -= 1
    transform_wl3(state)
    
    mom = randint(500, 1000 * state.dif)
    if qq == 1 and state.hp > 0 and state.passives[16] == 0:
        print('Вы, как победитель, получили Банку от Оружейника')
        state.passives[16] = 1
    if pil == 1 and state.hp > 0 and state.passives[15] == 0:
        print('Пила струна теперь ваша!')
        state.passives[15] = 1
    if v == 1:
        state.passives[17] = 1
        print('ХоРоШиЙ вЫбОр...')
    elif v == 2:
        print(f'ЛаДнО, дЕрЖи {mom} ' + state.get_currency())
        state.boskill += 1
        state.inf_rez += 10
        state.money += mom
    elif state.boss_hp <= 0 and state.hp > 0 and v == 0:
        print(BOSS_NAMES[kof] + f' был побежден, вы получили {mom} ' + state.get_currency() + ' и защитный слой из 10 Полиэтиленов!')
        state.inf_rez += 10
        state.boskill += 1
        state.money += mom
    elif state.boss_hp > 0 and state.hp <= 0:
        print(BOSS_NAMES[kof] + ' вас одолел(ну вы ботик нулевый конечно)')
        return True
    else:
        print('Вы вышли в ноль, но это не отменяет того факта что вы умерли')
        return True
    
    return False             