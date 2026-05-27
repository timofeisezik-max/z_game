from random import randint
from config import ABILITIES_DATA, GIMN_DATA, WEAPONS, WEAPON_PRICES, BOSS_NAMES
class GameState:
    def __init__(self, difficulty: int):
        self.dif = difficulty
        self.hp = 100
        self.boss_hp = 0
        self.luk = 35
        self.katastrof = 0
        self.money = randint(10, 151 * randint(1, difficulty) - randint(1, 15))
        self.bank = randint(10, 100 * difficulty)
        self.wins = 0
        self.pwins = 0
        self.nwins = 0
        self.inf_rez = 0
        self.motion = -1
        self.boskill = 0
        self.available_passives = [1] * 12  # доступные пассивы для выбора (бывший pas)
        # Способности
        self.abilities = [list(a) for a in ABILITIES_DATA]
        # Фиксим цену ГЭС
        self.abilities[13][2] = 29 * difficulty + (difficulty % 10 - 1)
        self.gimn = list(GIMN_DATA)
        self.gimn[2] = (randint(50, 100) * difficulty - randint(1, 25) * difficulty)
        
        self.ab_name = [a[0] for a in self.abilities]
        self.ab_vol = [0] * len(self.abilities)
        self.a_v = [a[1] for a in self.abilities]
        
        # Оружие
        self.wl = [[0] * 3 for _ in range(len(WEAPONS))]
        self.wl3_h = []  # пассивные юниты
        
        # Лутбоксы
        self.box_q = [0] * 4
        
        # Пассивы (18 штук, +1 для разделения Пилы и Подковы)
        # Индексы: 0-Балбес, 1-Шулер, 2-Око, 3-Рубль, 4-Моление, 5-Пальто,
        # 6-Гимн, 7-Алгебра, 8-Реверс, 9-Амулет, 10-Брелочек, 11-Лутбоксы,
        # 12-Брелочек(Ключ), 13-Подкова, 14-... 15-Пила струна, 16-Банка, 17-Моление Хаосу
        self.passives = [0] * 18
        
        # Для пассивки "Подкова" — контрольная точка поражений
        self.nwins_checkpoint = 0
        
        # Флаг добавления Гимна в список способностей
        self.gimn_added = False

    def get_currency(self):
        """Возвращает название валюты в зависимости от пассива Рубль"""
        from config import MONET, RUBLES
        return RUBLES[0] if self.passives[3] else MONET[2]

    def money_sign(self):
        """Множитель для денег (Реверс)"""
        return -1 if self.passives[8] else 1

    def has_gimn(self):
        """Проверка, есть ли Гимн в списке способностей"""
        return self.gimn_added

    def add_gimn(self):
        """Добавляет Гимн России в список способностей"""
        if not self.gimn_added:
            self.abilities.append(self.gimn)
            self.ab_vol.append(1)
            self.ab_name.append(self.gimn[0])
            self.a_v = [a[1] for a in self.abilities]
            self.gimn_added = True
            self.passives[6] += 1  # переходим из состояния 1 в 2

    def get_stat(self):
        """Формирует массив статистики для Око"""
        stat = [
            self.dif, self.hp, self.wins, self.pwins, self.nwins,
            self.wins + self.pwins + self.nwins, self.motion
        ]
        stat += self.wl[0] + self.wl[1] + self.wl[2]
        stat += self.box_q
        stat += self.ab_vol
        stat += self.a_v
        stat += [self.money, self.katastrof, self.inf_rez, self.bank, self.luk, self.boskill]
        stat += [item for sub in self.wl3_h for item in sub]  # разворачиваем wl3_h
        return stat