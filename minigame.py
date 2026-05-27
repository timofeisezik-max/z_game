from random import randint
from config import WIN_PHRASES, ALMOST_WIN_PHRASES, LOSE_PHRASES
from utils import gimn

def game_basic(state, guess: int, target: int):
    """Базовая мини-игра угадай число"""
    if guess == target and state.passives[6] == 0:
        print(WIN_PHRASES[randint(0, len(WIN_PHRASES) - 1)])
        state.money += randint(250, 526 * state.dif) * state.money_sign()
        state.wins += 1
        if state.passives[12] == 1 and state.dif != 1:
            state.dif -= 1
    elif guess == target and state.passives[6] == 2:
        gimn()
        state.money += randint(250, 526 * state.dif) * state.money_sign()
        state.wins += 1
    elif guess == target + 1 or guess == target - 1:
        print(ALMOST_WIN_PHRASES[randint(0, len(ALMOST_WIN_PHRASES) - 1)])
        state.money += randint(5, 10 * state.dif) * state.money_sign()
        state.pwins += 1
    else:
        print(LOSE_PHRASES[randint(0, len(LOSE_PHRASES) - 1)])
        state.money -= state.dif * state.money_sign()
        state.nwins += 1

def game_amulet(state, guesses: list, limit: int, target: int):
    """Мини-игра с амулетом (несколько чисел)"""
    if len(guesses) > limit:
        print('От такой наглости амулет сломался!')
        state.passives[9] += 1
        return
    
    target_str = str(target)
    target_plus = str(target + 1)
    target_minus = str(target - 1)
    
    if target_str in guesses and state.passives[6] == 0:
        print(WIN_PHRASES[randint(0, len(WIN_PHRASES) - 1)])
        state.money += randint(250, 526 * state.dif) * state.money_sign()
        state.wins += 1
        if state.passives[12] == 1 and state.dif != 1:
            state.dif -= 1
    elif target_str in guesses and state.passives[6] == 2:
        gimn()
        state.money += randint(250, 526 * state.dif) * state.money_sign()
        state.wins += 1
        if state.passives[12] == 1 and state.dif != 1:
            state.dif -= 1
    elif target_plus in guesses or target_minus in guesses:
        print(ALMOST_WIN_PHRASES[randint(0, len(ALMOST_WIN_PHRASES) - 1)])
        state.money += randint(5, 10 * state.dif) * state.money_sign()
        state.pwins += 1
    else:
        print(LOSE_PHRASES[randint(0, len(LOSE_PHRASES) - 1)])
        state.money -= state.dif * state.money_sign()
        state.nwins += 1