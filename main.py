from random import randint
from state import GameState
from config import ABILITY_NAMES, PASSIVE_NAMES, MONET, RUBLES
from utils import print_stat, print_passives, entry, entrys, SS, gener, generA
from abilities import (
    use_slon, use_genocide, use_rubashka, use_cherepakha, use_inflyaciya,
    use_discriminant, use_udlinitel, use_konyak, use_globus, use_kurkuma,
    use_chemodan, use_pnu, use_oguzok, use_ges, use_lampochka, use_polietilen,
    use_multivarka, use_gimn, use_ryba, use_nipon, use_medved, use_pora,
    use_fikus, use_titry
)
from economy import (
    process_inflation, process_bank_growth, process_bank_event,
    open_shop, open_casino, open_armory, buy_lootboxes, open_lootbox
)
from combat import boss_fight
from minigame import game_basic, game_amulet


def main():
    print('Выберите сложность(от 2 до 144)')
    dif = int(input())
    state = GameState(dif)

    while True:
        # === МОЛЕНИЕ БОГАМ ХАОСА ===
        if state.passives[17] == 1:
            if randint(1, 3) == 1:
                print('ЖАЛКИЙ ЕРЕТИК И КСЕНОС! ЗА МОЛЕНИЕ БОГАМ ХАОСА ТЫ БУДЕШЬ РАСТРЕЛЯН!!!!')
                break

        # === ПОДКОВА ===
        if state.passives[12] == 0:
            state.nwins_checkpoint = state.nwins
        if state.passives[12] == 1:
            diff_nwins = state.nwins - state.nwins_checkpoint
            if diff_nwins % 45 == 0 and diff_nwins != 0:
                state.dif += 1

        # === ГИМН РОССИИ (пассив) ===
        if state.passives[6] == 1:
            state.add_gimn()

        state.motion += 1
        print_stat(state)

        a = randint(1, 50 * state.dif)
        left = a - randint(1, 20 * state.dif)
        right = a + randint(1, 20 * state.dif)
        print(f'Угодай число jn {left} lj {right}  Ваши деньги: {state.money}', end=' ')
        print_passives(state)

        g = input()

        # === ЛУТБОКСЫ ===
        if g in ['()', '{}', '[]', '[||]'] and state.passives[11] == 1:
            open_lootbox(state, g)

        # === СПОСОБНОСТИ ===
        elif g in state.ab_name:
            if state.passives[10] == 1:
                state.ab_vol[randint(0, len(state.ab_vol) - 1)] += 1

            ab_idx = state.ab_name.index(g)
            if state.ab_vol[ab_idx] <= 0:
                print('Мошенник! За такую смеломть положена награда - прибавка к каждой способности на -578901234 едениц')
                state.ab_vol = [i - 578901234 for i in state.ab_vol]
                continue

            dead = False
            if g == 'Коньяк':
                dead = use_konyak(state)
            elif g == 'D=b2-4ac':
                use_discriminant(state, a)
            elif g == 'Слон':
                use_slon(state, a)
            elif g == 'Рубашка':
                use_rubashka(state, a)
            elif g == 'Куркума':
                use_kurkuma(state)
            elif g == 'Чемодан':
                use_chemodan(state)
            elif g == 'Глобус':
                use_globus(state)
            elif g == 'ПНУ':
                use_pnu(state, a)
            elif g == 'Удлинитель':
                use_udlinitel(state)
            elif g == 'Инфляция':
                use_inflyaciya(state)
            elif g == 'Геноцид':
                print('Кого стреляем?')
                dead = use_genocide(state, input(), a)
            elif g == 'Огузок':
                use_oguzok(state)
            elif g == 'ГЭС':
                use_ges(state)
            elif g == 'Лампочка':
                use_lampochka(state, a)
            elif g == 'Полиэтилен':
                use_polietilen(state)
            elif g == 'Мультиварка':
                use_multivarka(state)
            elif g == 'ГимнРоссии':
                use_gimn(state)
            elif g == 'Рыба':
                use_ryba(state)
            elif g == 'Нипон':
                use_nipon(state)
            elif g == 'Медведь':
                dead = use_medved(state)
            elif g == 'Пора':
                use_pora(state)
            elif g == 'Фикус':
                use_fikus(state)
            elif g == 'Черепаха':
                use_cherepakha(state)
            elif g == 'Титры':
                use_titry(state)

            if dead:
                break

        # === ОБЫЧНЫЙ ВВОД (мини-игра + события) ===
        else:
            process_inflation(state)
            process_bank_growth(state)

            if state.passives[9] == 1:
                game_amulet(state, g.split(), 1 + state.dif, a)
            else:
                try:
                    game_basic(state, int(g), a)
                except ValueError:
                    print('Ты помойму перепутал')
                    continue

            # Пассив "Алгебра" — шанс на уравнение после хода
            if state.passives[7] == 1 and str(randint(0, 9)) in '02468':
                D = gener(state.dif)
                print(D[0])
                if state.passives[0] == 1:
                    print('Для балбесов: ответ -', D[1])
                print('Ответ:(jn меньшего к большему, без пробелов)', end=' ')
                otv = input()
                if otv == D[1]:
                    print('Неплох, держи 15*dif', state.get_currency())
                    state.money += 15 * state.dif * state.money_sign()
                else:
                    currency = RUBLES[1] if state.passives[3] else MONET[1]
                    print(f'Такое не прощается, С ДНЕМ', currency, '! УРААААААА!!!')
                    state.money = 1

            # === БАНК ===
            process_bank_event(state)

            # === МАГАЗИН ===
            open_shop(state)

            # === КАЗИНО ===
            open_casino(state)

            # === ОРУЖЕЙНАЯ ===
            W = randint(1, 20)
            if ((W in [1, 2, 3]) or state.passives[13] == 1) and state.passives[11] == 0:
                if open_armory(state):
                    break

            # === ПОКУПКА ЛУТБОКСОВ ===
            buy_lootboxes(state)

            # === БОСС ===
            B = randint(1, 100)
            if ((B in [10, 29, 38, 47, 56]) or B <= 15 * state.passives[13]) and state.wins >= 4:
                if boss_fight(state):
                    break

            # === ВЫБОР НОВОГО ПАССИВА ===
            if (randint(1, 15) in [6, state.passives[13]]) and sum(state.available_passives) != 0 and state.passives[17] == 0:
                print('Какую способность ты возьмешь?')
                s = []
                h = 2
                while len(s) != h and len(s) != SS(state.available_passives):
                    d = randint(0, len(state.available_passives) - 1)
                    if d not in s and state.available_passives[d] != 0:
                        s.append(d)
                
                products = []
                for i in s:
                    print(PASSIVE_NAMES[i])
                    products.append(PASSIVE_NAMES[i])
                print('Выбор:', end=' ')
                shop = input()
                if entrys(shop, [[p] for p in products]) and shop != '':
                    idx = entry(shop, [[p] for p in products])
                    real_idx = s[idx]
                    state.passives[real_idx + 2] += 1
                    state.available_passives[real_idx] -= 1
                    print('Ты сделал свой выбор...')
                else:
                    print('Роковая ошибка...')

        # === ПРОВЕРКИ ОКОНЧАНИЯ ИГРЫ ===
        if state.wins == 5 * state.dif and state.passives[4] == 0:
            print('Хватит, много играть вредно для здоровья, иди лучше помолись богу императору')
            break
        elif state.wins == 5 * state.dif and state.passives[4] == 1:
            print('Ладно, поиграй еще чуть-чуть....')
        elif state.wins == 10 * state.dif:
            print('Хватит играть! Иди потрогай траву во имя бога Императора!!!')
            break
        elif state.money < 0 and state.passives[1] == 0:
            print('Вас обокрали на жизнь...')
            break
        elif state.money < 0 and state.money >= -(25 * state.dif) and state.passives[1] == 1:
            print('Твои шулерские навыки еще позволяют держаться без денег, но какой ценой...')
            state.ab_vol[randint(0, len(state.ab_vol) - 1)] -= 1
            if state.passives[10] == 1:
                state.ab_vol[randint(0, len(state.ab_vol) - 1)] += 1
        elif state.money < -(25 * state.dif):
            print('Твои навыки и так продлили тебе жизнь, но это не могло продолжаться вечно...')
            break


if __name__ == '__main__':
    main()