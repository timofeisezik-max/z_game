from random import *
from math import *

print('Выберите сложность(от 2 до 144)')
dif = int(input())
hp = 100
bossHp = 0
luk = 35

katastrof = 0
money = randint(10,151*randint(1,dif)-randint(1,15))
bank = randint(10,100*dif)
wins = pwins = nwins = 0
infRez = 0
abilki = [['Слон',randint(1,randint(2,15*dif)),450],['Геноцид',randint(1,randint(2,15*dif)),300],['Рубашка',randint(1,randint(2,15*dif)),25],['Черепаха',randint(1,randint(2,15*dif)),50],
          ['Инфляция',randint(1,randint(2,15*dif)),6],['D=b2-4ac',randint(1,randint(2,15*dif)),40],['Удлинитель',randint(1,randint(2,15*dif)),55],['Коньяк',randint(1,randint(2,15*dif)),1000],
          ['Глобус',randint(1,randint(2,15*dif)),500],['Куркума',randint(1,randint(2,15*dif)),750],['Чемодан',randint(1,randint(2,15*dif)),200],['ПНУ',randint(2,15*dif),35],
          ['Огузок',randint(2,15*dif),35],['ГЭС',randint(2,15*dif),29*dif+(dif%10-1)],['Лампочка',randint(2,15*dif),45],['Полиэтилен',randint(2,15*dif),40],
          ['Мультиварка',randint(2,15*dif),350],['Рыба',randint(2,15*dif),100],['Нипон',randint(1,15*dif),15],['Медведь',randint(1,15*dif),200],['Пора',randint(1,15*dif),40],
          ['Фикус',randint(1,15*dif),90],['Титры',randint(1,15),1]]
gigi = ['ГимнРоссии',randint(1,15*dif),randint(50,100)*dif - randint(1,25)*dif]
    
abName = [i[0] for i in abilki]
abVol = [0 for i in range(23)]
aV = [i[1] for i in abilki]
motion = -1
#1)Слон 2)Геноцид 3)Рубашка 4)Черепаха 5)Инфляция 6)D=b2-4ac 7)Удлинитель 8)Коньяк 9)Глобус 10)Куркума 11)Чемодан
#12)ПНУ 13)Огузок 14)ГЭС 15)Лампочка 16)Полиэтилен 17)Мультиварка 18)Рыба 19)Нипон 20)Медведь
#21)Пора 22)Фикус 23)Титры -1)ГимнРоссии


#1] 1d6, 1d10, 1d6d10
#2] Подорожник, Банка арбузов, Тульский пряник
#3] Чукча, Сеньор, Космодесантник
wep = [['1к8','1к20','1к6к12'],['Подорожник','Банка_арбузов','Тульский_пряник'],['Чукча','Сеньор','Космодесантник']]
wep_c = [[40,120,250],[60,140,280],[20,95,300]]
wl = [[0]*3 for i in range(len(wep))]
wl3_h = []

#1)Танос 2)Тзинч 3)страж Хорограда 4)Вор 5)Выживалово 6)Оружейник
bosN = ['Танос','Тзинч','страж Хорограда','Вор','Выживалово','Оружейник']
boskill = 0


#1)Балбес 2)Шулер 3)Око 4)Рубль 5)Моление богу императору 6)Пальто 7)Гимн России 8)Алгебра 9)Реверс 10)Амулет 11)Круговая порука 12)Лутбоксы 13)Брелочек
#14)Ключ 15)Подкова -3)Пила струна -2)Банка -1)Моление Богам Хаоса
pasivki = [0 for i in range(18)]
pas = [1 for i in range(12)]
#1)() 2){} 3)[] 4)[||]
box_q = [0]*4
pN = ['Око','Рубль','Моление Богу Императору','Пальто','Гимн России','Алгебра','Реверс','Амулет','Круговая порука','Лутбоксы','Брелочек','Ключ','Подкова']
stat = [dif,hp,wins,pwins,nwins,wins+pwins+nwins,motion] + wl[0] + wl[1] + wl[2] + box_q + abVol + aV + [money,katastrof,infRez,bank,luk,boskill]+wl3_h

wF = ['Нифига крутой, вытри противотанковую немецкую установку под губой','Нифига крутой - Иди домой!!! АХАХАХАХХА','Ты медуза','ЭТО НЕ ПРОСТО ГНЕВ ТО ЧТО ЖИВЕТ ВО МНЕ ПЫТАЯСЬ ВЫРВАТЬСЯ ИЗ ПОД КОНТРОЛЯ','Император гордится тобой']
pwF = ['Нифига крутой, ладно шучу конечно','Домой','Почти мега плох','Ты бог дедов','1101000010100010110100011000101100100000110100001011111111010001100000001101000010111110110100011000000111010001100000101101000010111110001000001101000010111101110100011000001111010000101110111101000010110101110100001011001011010001100010111101000010111001(UFT8)']
nwF = ['Ну ты ботик конечно','Слабочек','Ультрасверхдупергипермеганевероятногигакилоэксапетатерагектодекаплох','Иди учись','Сэр, вы просто нулёвый!']
alk = ['Слово Коньяк и слово смерть, для вас означают одно и тоже','Вы умерли из-за употребления алкоголя... Алкоголь убивает!']



def gimn():
    print('Россия - священная наша держава,','Россия - любимая наша страна.','Могучая воля, великая слава -','Твое достоянье на все времена!','Славься, Отечество наше свободное,','Братских народов союз вековой,','Предками данная мудрость народная!','Славься, страна! Мы гордимся тобой!','От южных морей до полярного края','Раскинулись наши леса и поля.','Одна ты на свете! Одна ты такая -','Хранимая Богом родная земля!','Славься, Отечество наше свободное,','Братских народов союз вековой,','Предками данная мудрость народная!','Славься, страна! Мы гордимся тобой!','Широкий простор для мечты и для жизни','Грядущие нам открывают года.','Нам силу дает наша верность Отчизне.','Так было, так есть и так будет всегда!','Славься, Отечество наше свободное,','Братских народов союз вековой,','Предками данная мудрость народная!','Славься, страна! Мы гордимся тобой!',sep='\n')

def SS(a):
    g = 0
    for i in a:
        if i > 0:
            g += 1
    return g

def nip():
    alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    j = randint(1,randint(2,randint(3,15)))
    g = ''
    for i in range(j):
        g += alf[randint(1,len(alf))-1]
    return g

def O(pasivki,stat):
    if pasivki[2] == 1:
        for i in stat:
            print(i,end= ' ')
        print()

def pp(pasivki):
    pas = ['Б','Ш','Ꝺ','₽','۞','Ѧ','Г','√','Ѻ','Ꙋ','꙰','꙱','Ϫ','ჭ','Ω','δ','Ꙫ','ꙮ']
    g = ''
    if sum(pasivki) == 0:
        print()
    else:
        for i in range(len(pasivki)):
            if pasivki[i] != 0:
                g += pas[i]
        print(g)
        

def entry(s,g):
    for i in range(len(g)):
        if s in g[i]:
            return i
            break

def randi(g):
    i = []
    while len(g) != 0:
        gg = g[randint(0,len(g)-1)]
        i.append(gg)
        g.remove(gg)
    return i
        

def box1(wep,abilki,spos,moneys,abVols,wls,wl3_hs,pasivki,abName):
    global wl,wl3_h,abVol,money
    wl,wl3_h,abVol,money=wls,wl3_hs,abVols,moneys
    st = randi([0]*75+[wep[randint(0,len(wep)-1)][0] for i in range(5)]+[spos[randint(0,len(spos)-1)] for i in range(8)]+[randint(1,50) for i in range(12)])
    priz = st[randint(0,len(st)-1)]
    if entrys(priz,wep):
        print('Выпадает '+priz)
        if priz in wep[-1]:
            wl[-1][entry(priz,wep[-1])] += 1
            wl3_h.append([entry(priz,wep[-1]),1,entry(priz,wep[-1])+1,[1,4,8][entry(priz,wep[-1])]])
        else:
            wl[entry(priz,wep)][entry(priz,wep[entry(priz,wep)])] += 1
    elif priz in abName:
        abVol[entry(priz,abName)] += 1
        print('Выпадает '+priz)
    elif priz != 0:
        print(f'Выпадает {priz} '+[monet[2],rubles[0]][pasivki[3]])
        money += priz
    else:
        print('Ничего не выпало')

def box2(wep,abilki,spos,moneys,abVols,wls,wl3_hs,pasivki,abName):
    global wl,wl3_h,abVol,money
    wl,wl3_h,abVol,money=wls,wl3_hs,abVols,moneys
    st = randi([0]*50+[wep[randint(0,len(wep)-1)][randint(0,1)] for i in range(12)]+[spos[randint(0,len(spos)-1)] for i in range(18)]+[randint(25,100) for i in range(20)])
    i = []
    for j in range(randint(1,2)):
        i.append(st[randint(0,len(st)-1)])
        st.remove(st[randint(0,len(st)-1)])
    for priz in i: 
        if entrys(priz,wep):
            print('Выпадает '+priz)
            if priz in wep[-1]:
                wl[-1][entry(priz,wep[-1])] += 1
                wl3_h.append([entry(priz,wep[-1]),1,entry(priz,wep[-1])+1,[1,4,8][entry(priz,wep[-1])]])
            else:
                wl[entry(priz,wep)][entry(priz,wep[entry(priz,wep)])] += 1
        elif priz in abName:
            abVol[entry(priz,abName)] += 1
            print('Выпадает '+priz)
        elif priz != 0:
            print(f'Выпадает {priz} '+[monet[2],rubles[0]][pasivki[3]])
            money += priz
        else:
            print('Ничего не выпало')

def box3(wep,abilki,spos,moneys,abVols,wls,wl3_hs,pasivki,abName):
    global wl,wl3_h,abVol,money
    wl,wl3_h,abVol,money=wls,wl3_hs,abVols,moneys
    st = randi([0]*25+[wep[randint(0,len(wep)-1)][1] for i in range(26)]+[spos[randint(0,len(spos)-1)] for i in range(34)]+[randint(80,200) for i in range(15)])
    i = []
    for j in range(2):
        i.append(st[randint(0,len(st)-1)])
        st.remove(st[randint(0,len(st)-1)])
    for priz in i: 
        if entrys(priz,wep):
            print('Выпадает '+priz)
            if priz in wep[-1]:
                wl[-1][entry(priz,wep[-1])] += 1
                wl3_h.append([entry(priz,wep[-1]),1,entry(priz,wep[-1])+1,[1,4,8][entry(priz,wep[-1])]])
            else:
                wl[entry(priz,wep)][entry(priz,wep[entry(priz,wep)])] += 1
        elif priz in abName:
            abVol[entry(priz,abName)] += 1
            print('Выпадает '+priz)
        elif priz != 0:
            print(f'Выпадает {priz} '+[monet[2],rubles[0]][pasivki[3]])
            money += priz
        else:
            print('Ничего не выпало')

def box4(wep,abilki,spos,moneys,abVols,wls,wl3_hs,pasivki,abName):
    global wl,wl3_h,abVol,money
    wl,wl3_h,abVol,money=wls,wl3_hs,abVols,moneys
    st = randi([wep[randint(0,len(wep)-1)][randint(1,2)] for i in range(40)]+[spos[randint(0,len(spos)-1)] for i in range(50)]+[randint(125,450) for i in range(10)])
    i = []
    for j in range(randint(2,3)):
        i.append(st[randint(0,len(st)-1)])
        st.remove(st[randint(0,len(st)-1)])
    for priz in i: 
        if entrys(priz,wep):
            print('Выпадает '+priz)
            if priz in wep[-1]:
                wl[-1][entry(priz,wep[-1])] += 1
                wl3_h.append([entry(priz,wep[-1]),1,entry(priz,wep[-1])+1,[1,4,8][entry(priz,wep[-1])]])
            else:
                wl[entry(priz,wep)][entry(priz,wep[entry(priz,wep)])] += 1
        elif priz in abName:
            abVol[entry(priz,abName)] += 1
            print('Выпадает '+priz)
        elif priz != 0:
            print(f'Выпадает {priz} '+[monet[2],rubles[0]][pasivki[3]])
            money += priz
        else:
            print('Ничего не выпало')
    
def lutBox(box,wep,wls,wl3_hs,abilki,abVols,moneys,pasivki,box_qs,abName):
    global wl,wl3_h,abVol,money,box_q
    wl,wl3_h,abVol,money,box_q=wls,wl3_hs,abVols,moneys,box_qs
    imba2 = ['Слон','Глобус','Куркума']
    if pasivki[6] == 2:
        imba = ['Геноцид','Мультиварка','ГимнРоссии']
    else:
        imba = ['Геноцид','Мультиварка']    
    horosh = ['D=b2-4ac','Черепаха','ГЭС','Чемодан','Рыба','Медведь','Лампочка']
    norm = ['Рубашка','Удлинитель','ПНУ','Полиэтилен','Фикус']
    dich = ['Инфляция','Огузок','Нипон','Пора','Коньяк','Титры']
    if box == '()' and box_q[0] > 0:
        box_q[0] -= 1
        box1(wep,abilki,dich+norm,moneys,abVols,wls,wl3_h,pasivki,abName)
    elif box == '{}' and box_q[1] > 0:
        box_q[1] -= 1
        box2(wep,abilki,norm+horosh,moneys,abVols,wls,wl3_h,pasivki,abName)
    elif box == '[]' and box_q[2] > 0:
        box_q[2] -= 1
        box3(wep,abilki,horosh+imba,moneys,abVols,wls,wl3_h,pasivki,abName)    
    elif box == '[||]' and box_q[3] > 0:
        box_q[3] -= 1
        box4(wep,abilki,imba2+imba,moneys,abVols,wls,wl3_h,pasivki,abName)
    
def wl3_sh_transform(wl3_shs,wls):
    global wl3_sh, wl
    wl3_sh, wl = wl3_shs, wls
    if len(wl3_sh) != 0:
            for i in wl3_sh:
                if i[0] < 0:
                    wl[-1][i[0]+i[2]] -= i[1]
                    wl3_sh.remove(i)
            for i in range(len(wl3_sh)):
                if wl3_sh[i][2] == 2:
                    wl3_sh[i][-1] += 2
                else:
                    wl3_sh[i][-1] *= 2

def hill(hod,hps,wep,wls,pasivki,abVols,w2=[20,50,105]):
    global hp,wl,abVol
    hp,wl,abVol = hps, wls, abVols
    if hod != 'Пластырь' and hod != 'Медведь':
        damage = w2[entry(hod,wep[1])]
        wl[1][entry(hod,wep[1])] -= 1
    elif hod == 'Медведь' and pasivki[-3] == 1 and abVol[19] > 0:
        damage = 35
        abVol[19] -= 1
    else:
        damage = 10
    print(f'Вы восстановили {damage} HP!')
    hp += damage              
    if pasivki[10] == 1:
        wl[randint(0,len(wl)-2)][randint(0,len(wl[0]-1))] += 1

def hit(hod,bossHps,wep,wls,pasivki,kof):
    global bossHp, wl
    bossHp, wl = bossHps, wls
    w1=[randint(1,8),randint(1,20),sum([randint(1,12) for i in range(randint(1,6))])]
    if hod != '1к4':        
        damage = w1[entry(hod,wep[0])]
        wl[0][entry(hod,wep[0])] -= 1 
    else:
        damage = randint(1,4)
    print(f'Выпадает {damage}'+['!','!(+Пила Струна)'][pasivki[-3]])
    if kof == 2:
        bossHp -= (damage + [0,randint(5,15)][pasivki[-3]])//4 
    else:
        bossHp -= damage + [0,randint(5,15)][pasivki[-3]]            
    if pasivki[10] == 1:
        wl[randint(0,len(wl)-2)][randint(0,len(wl[0]-1))] += 1
    

def hod(wep,wls,bossHps,hps,pasivki,abVols,kof=0):
    global bossHp, wl, hp, abVol
    bossHp, wl, hp, abVol = bossHps, wls, hps, abVols
    print('Ваш ход(используйте 1 из способностей(чукчи, сеньоры и космодесантники являются пассивными способностями))')
    hod = input()
    if hod in wep[0] and wls[0][entry(hod,wep[0])] > 0 or (pasivki[-2] == 1 and hod == '1к4'):
        hit(hod,bossHps,wep,wls,pasivki,kof)
    elif hod in wep[1] and wls[1][entry(hod,wep[1])] > 0 or (pasivki[-2] == 1 and hod == 'Пластырь') or (pasivki[-3] == 1 and hod == 'Медведь' and abVol[19] > 0):
        hill(hod,hps,wep,wls,pasivki,abVols)
    else:
        print('Ты помойму перепутал')

def oryz(moneys,wep,wls,wl3_hs,wep_c,pasivki,abVol,monet,rubles,boskill,bosN):
    global money,wl,wl3_h
    money,wl,wl3_h = moneys,wls,wl3_hs
    print('ОРУЖЕЙНАЯ')
    money += randint(5,50)*[1,-1][pasivki[8]]
    print(f'Ваш баланс: {money}',[monet[2],rubles[0]][pasivki[3]])
    vol = randint(1,len(wep))
    kategoris = []
    kat_c = []
    g = list(range(0,len(wep)))
    for j in range(vol):
        i = choice(g)
        kategoris.append(wep[i])
        kat_c.append(wep_c[i])
        g.remove(i)                          
    logi = []
    for i in range(len(kategoris)):
        logi.append([randint(1,3*dif),choice([1]*6+[2]*3+[3])])
    invent = []
    for i in range(len(kategoris)):
        for j in range(logi[i][1]):
            invent.append([kategoris[i][j],kat_c[i][j],logi[i][0]])
    vetrina = []
    while len(vetrina) != len(invent):
        q = randint(1,len(invent))-1
        if not(invent[q] in vetrina):
            vetrina.append(invent[q])
    print('Вы можете приобрести')
    for i in range(len(vetrina)):
        print(vetrina[i][0]+': '+str(vetrina[i][2])+' штук, за штуку '+str(vetrina[i][1])+' '+[monet[2],rubles[0]][pasivki[3]])
    print('Надо чего?(надо/ненадо)')
    ToF = input()
    if ToF == 'надо':
        print('Чего и скоко?')
        shop = input().split()
        if len(shop) == 1:
            shop.append(1)
        if entrys(shop[0],vetrina):
            q = entry(shop[0],vetrina)
            if (vetrina[q][1]) * int(shop[1]) <= money and int(shop[1]) <= vetrina[q][2]:
                if pasivki[10] == 1:
                    for i in range(int(shop[1])):
                        wl[randint(0,len(wl)-2)][randint(0,len(wl[0])-1)] -= 1
                money -= vetrina[q][1] * int(shop[1])
                wl[entry(shop[0],wep)][entry(shop[0],wep[entry(shop[0],wep)])] += int(shop[1])
                if shop[0] in wep[-1]:
                    g = entry(shop[0],wep[-1])
                    wl3_h.append([g,int(shop[1]),g+1,[1,4,8][g]])
            else:
                print('АХ ТЫ ПЛЕШИВЕЦ!')
                return bossfight(money,bosN,pasivki,hp,wl,wep,wl3_h,infRez,boskill,monet,rubles,abVol,invent,-1)
        else:
            print('Шо ты мелишь')
    else:
        print('Ну тогда катись отсюда')


def enter():
    print('Вам нечего использовать...')
    print('"нажмите enter"',end=' ')
    enter = input()       
    
def bossfight(moneys,bosN,pasivkis,hps,wls,weps,wl3_hs,infRezs,boskills,monet,rubles,abVols,invent=0,kof=randint(1,len(bosN)-1)-1,bossHps=0):
    global pasivki,hp,wl,wl3_h,boskill,infRez,money,bossHp,abVol
    pasivki,hp,wl,wl3_sh,boskill,infRez,money,bossHp,abVol = pasivkis,hps,wls,wl3_hs,boskills,infRezs,moneys,bossHps,abVols
    print('На вас напал ' + bosN[kof])
    pasDamage = 0
    pil = qq = v = 0
    if len(wl3_sh) != 0:
        for i in wl3_h:
            if kof != 2:
                pasDamage += i[1]*i[-1]
            else:
                pasDamage += i[1]//8*i[-1]
    if kof == 0:
        bossHp = 150
        while bossHp > 0 and hp > 0:
            print(f'Ваше HP:{hp}, HP '+bosN[kof]+f': {bossHp}')
            print(bosN[kof]+f' атакует и наносит {hp // 2 + hp%2} урона.')
            hp //= 2
            bossHp -= hp//2
            print(f'Ваши солдаты нанесли {pasDamage} урона')
            bossHp -= pasDamage
            if sus(wl[0:len(wl)-1]) != 0 or pasivki[-2] == 1 or (abVol[19] > 0 and pasivki[-3] == 1):
                hod(wep,wl,bossHp,hp,pasivki,abVol)         
            else:
                enter()
    elif kof == 1 and pasivki[4] == 0:
        bossHp = -1
        while hp > 0:
            print(f'Ваше HP:{hp}, HP '+bosN[kof]+f': {bossHp}')
            c = randint(1,5)
            print('УгОдАй ЧиСлО jN -10000000000 до 1000000000')
            h = int(input())
            if h == c:
                print('ВыБиРаЙ: ДеНьГи ИлИ оСоБыЙ пРиЗ(2 иЛи 1 СоОтВеТсТвЕнНо)')
                v = int(input())
                break
            else:
                print(bosN[kof]+f' атакует и наносит {-1*bossHp} урон.')
                hp += bossHp
                if randint(1,20) == 5:
                    print('Ты Не СмОжЕшЬ еСлИ нЕ пОсМоТрИшЬ в КоД')
            print(f'Ваши солдаты нанесли {pasDamage} урона')
            bossHp -= pasDamage
            if sus(wl[0:len(wl)-1]) != 0 or pasivki[-2] == 1 or (abVol[19] > 0 and pasivki[-3] == 1):
                hod(wep,wl,bossHp,hp,pasivki,abVol)         
            else:
                enter()
    elif kof == 1 and pasivki[4] != 0:
        print("Тзинч хотел на вас напасть, но Бог Император защитил вас")    
    elif kof == 2:
        bossHp = 75
        while hp > 0 and bossHp > 0:
            print(f'Ваше HP:{hp}, HP '+bosN[kof]+f': {bossHp}')
            damag = randint(1,15)
            print(bosN[kof]+f' атакует и наносит {damag} урона.')
            hp -= damag
            print(f'Ваши солдаты нанесли {pasDamage} урона')
            bossHp -= pasDamage
            if sus(wl[0:len(wl)-1]) != 0 or pasivki[-2] == 1 or (abVol[19] > 0 and pasivki[-3] == 1):
                hod(wep,wl,bossHp,hp,pasivki,abVol,kof)         
            else:
                enter()
    elif kof == 3:
        bossHp = 10
        while hp > 0 and bossHp > 0:
            kraz = randint(1,randint(1,randint(1,randint(1,randint(1,randint(1,randint(1,randint(1,10000))))))))
            print(f'Вор украл у вас {kraz} '+[monet[2],rubles[0]][pasivki[3]])
            bossHp += kraz
            money -= kraz
            print(f'Ваше HP:{hp}, HP '+bosN[kof]+f': {bossHp}')
            print(bosN[kof]+f' атакует и наносит {bossHp // 10} урона.')
            hp -= bossHp//10
            print(f'Ваши солдаты нанесли {pasDamage} урона')
            bossHp -= pasDamage
            if sus(wl[0:len(wl)-1]) != 0 or pasivki[-2] == 1 or (abVol[19] > 0 and pasivki[-3] == 1):
                hod(wep,wl,bossHp,hp,pasivki,abVol)         
            else:
                enter()
    elif kof == 4:
        bossHp = 80
        zvero = sum([abVol[i] for i in range(len(abVol)) if (i in [0,3,17,19]) and (abVol[i] > 0)])
        if zvero > 0:
            bossHp += zvero*5
            for i in [0,3,17,19]:
                if abVol[i] > 0:
                    abVol[i] = 0 
            print('Хорошая животина, на сытый желудок можно и побиться')
            print('"Достает пилу струну"')
            pil = 1
        while hp > 0 and bossHp > 0:
            print(f'Ваше HP:{hp}, HP '+bosN[kof]+f': {bossHp}')
            atak = [randint(1,15),randint(10,20)][pil]
            print(bosN[kof]+f' атакует и наносит {atak} урона.')
            hp -= atak
            print(f'Ваши солдаты нанесли {pasDamage} урона')
            bossHp -= pasDamage
            if sus(wl[0:len(wl)-1]) != 0 or pasivki[-2] == 1 or (abVol[19] > 0 and pasivki[-3] == 1):
                hod(wep,wl,bossHp,hp,pasivki,abVol)
            else:
                enter()
            if pil == 1 and randint(1,2) == 2:
                atak = randint(1,15)
                print(bosN[kof]+f' атакует и наносит {atak} урона.')
                hp -= atak
    elif kof == -1:
        qq = 1
        h = [20,50,105,10]
        bossHp = 100
        kategorys = [[],[],[]]
        for i in invent:
            kategorys[entry(i[0],wep)].append([entry(i[0],wep[entry(i[0],wep)]),i[-1]])
        atak = kategorys[0]
        hil = kategorys[1]
        sold = kategorys[-1]
        pasD = 0
        for i in sold:
            pasD += [1,4,8][i[0]] * i[1]
        while hp > 0 and bossHp > 0:
            print(f'Ваше HP:{hp}, HP '+bosN[kof]+f': {bossHp}')
            print(f'Солдаты Оружейника нанесли вам {pasD} урона')
            hp -= pasD
            d = [randint(1,8),randint(1,20),sum([randint(1,12) for i in range(randint(1,6))]),randint(1,4)]
            if len(hil) > 0 and len(atak) > 0:
                if bossHp >= hp:
                    print('Оружейник использует '+wep[0][atak[-1][0]])
                    print(f'Выпадает {d[atak[-1][0]]}!')
                    hp -= d[atak[-1][0]]
                    atak[-1][-1] -= 1
                else:
                    print('Оружейник использует '+wep[1][hil[-1][0]])
                    bossHp += h[hil[-1][0]]
                    hil[-1][-1] -= 1
            elif len(hil) > 0 and len(atak) == 0:
                if randint(1,20) > 11:
                    print('Оружейник использует 1к4')
                    print(f'Выпадает {d[-1]}!')
                    hp -= d[-1]
                else:
                    print('Оружейник использует '+wep[1][hil[-1][0]])
                    bossHp += h[hil[-1][0]]
                    hil[-1][-1] -= 1
            elif len(hil) == 0 and len(atak) > 0:
                if randint(1,20) <= 11:
                    print('Оружейник использует '+wep[0][atak[-1][0]])
                    print(f'Выпадает {d[atak[-1][0]]}!')
                    hp -= d[atak[-1][0]]
                    atak[-1][-1] -= 1
                else:
                    print('Оружейник использует пластырь')
                    bossHp += h[-1]
            else:
                if randint(1,2) == 1:
                    print('Оружейник использует 1к4')
                    print(f'Выпадает {d[-1]}!')
                    hp -= d[-1]
                else:
                    print('Оружейник использует пластырь')
                    bossHp += h[-1]
            if len(hil) > 0:
                for i in hil:
                    if i[-1] == 0:
                        hil.remove(i)
            if len(atak) > 0:
                for i in atak:
                    if i[-1] == 0:
                        atak.remove(i)
            print(f'Ваши солдаты нанесли {pasDamage} урона')
            bossHp -= pasDamage
            if sus(wl[0:len(wl)-1]) != 0 or pasivki[-2] == 1 or (abVol[19] > 0 and pasivki[-3] == 1):
                hod(wep,wl,bossHp,hp,pasivki,abVol)
            else:
                enter()  
    for i in range(len(wl3_sh)):
        wl3_sh[i][0] -= 1
    wl3_sh_transform(wl3_sh,wl)
    mom = randint(500,1000*dif)
    if qq == 1 and hp > 0 and pasivki[-2] == 0:
        print('Вы, как победитель, получили Банку от Оружейника')
        pasivki[-2] = 1
    if pil == 1 and hp > 0 and pasivki[-3] == 0:
        print('Пила струна теперь ваша!')
        pasivki[-3] = 1
    if v == 1:
        pasivki[-1] = 1
        print('ХоРоШиЙ вЫбОр...')
    elif v == 2:
        print(f'ЛаДнО, дЕрЖи {mom} '+[monet[2],rubles[0]][pasivki[3]])
        boskill += 1
        infRez += 10
        money += mom
    elif bossHp <= 0 and hp > 0 and v == 0:
        print(bosN[kof]+f' был побежден, вы получили {mom} '+[monet[2],rubles[0]][pasivki[3]]+' и защитный слой из 10 Полиэтиленов!')
        infRez += 10
        boskill += 1
        money += mom
    elif bossHp > 0 and hp <= 0:
        print(bosN[kof]+' вас одолел(ну вы ботик нулевый конечно)')
        return True
    else:
        print('Вы вышли в ноль, но это не отменяет того факта что вы умерли')
        return True
                            
        
def game(g,winss,pwinss,nwinss,moneys,difs,a,pasivki,wF=wF,pwF=pwF,nwF=nwF):
    global dif,money, wins, pwins, nwins
    dif,money,wins,pwins,nwins = difs,moneys,winss,pwinss,nwinss
    if g == a and pasivki[6] == 0:
        print(wF[randint(1,len(wF))-1])
        money += (randint(250,526*dif))*[1,-1][pasivki[8]]
        wins += 1
        if pasivki[12] == 1:
            if dif != 1:
                dif -= 1
    elif g == a and pasivki[6] == 2:
        gimn()
        money +=(randint(250,526*dif))*[1,-1][pasivki[8]]
        wins += 1
    elif g == a+1 or g == a-1:
        print(pwF[randint(1,len(pwF))-1])
        money += (randint(5,10*dif)*[1,-1][pasivki[8]])
        pwins += 1
    else:
        print(nwF[randint(1,len(nwF))-1])
        money -= dif*[1,-1][pasivki[8]]
        nwins += 1
    
def game1(g,lim,winss,pwinss,nwinss,moneys,difs,a,pasivki,wF=wF,pwF=pwF,nwF=nwF):
    global dif, money, wins, pwins, nwins
    dif,money,wins,pwins,nwins = difs,moneys,winss,pwinss,nwinss
    if len(g) <= lim:
        if (str(a) in g) and pasivki[6] == 0:
            print(wF[randint(1,len(wF))-1])
            money += (randint(250,526*dif))*[1,-1][pasivki[8]]
            wins += 1
            if pasivki[12] == 1:
                if dif != 1:
                    dif -= 1
        elif (str(a) in g) and pasivki[6] == 2:
            gimn()
            money +=(randint(250,526*dif))*[1,-1][pasivki[8]]
            wins += 1
            if pasivki[12] == 1:
                if dif != 1:
                    dif -= 1
        elif (str(a+1) in g) or (str(a-1) in g):
            print(pwF[randint(1,len(pwF))-1])
            money += (randint(5,10*dif)*[1,-1][pasivki[8]])
            pwins += 1
        else:
            print(nwF[randint(1,len(nwF))-1])
            money -= dif*[1,-1][pasivki[8]]
            nwins += 1
    else:
        print('От такой наглости амулет сломался!')
        pasivki[9] += 1


def tr(a,b,c):
    k=[a,b,c]
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
        g[0] = g[0].replace(g[0][0],'',1)
    return g[0],g[1],g[2]

def entrys(s,g):
    d = False
    for i in range(len(g)):
        if s in g[i]:
            d = True
            break
    return d
    
def sus(a):
    g = 0
    for i in a:
        g += sum(i)
    return g

def generA(dif=1):
    chanse = randint(1,5)
    if chanse == 2:
        xx = []
        while len(xx) != 2:
            x = randint(1,5+dif)
            if not(x in xx):
                xx.append(x)
        a = randint(1,20)*choice([-1,1])
        b = -(xx[0]**2+xx[1]**2)*a
        c = (xx[0]**2*xx[1]**2)*a
    else:
        x1 = randint(1,5+dif)
        xx = [x1]
        x2 = randint(1,25)*(-1)
        a = randint(1,20)*choice([-1,1])
        b = -(x1**2+x2)*a
        c = (x1**2*x2)*a
    for i in xx:
        if not(-i in xx):
            xx.append(-i)
    xx = sorted(xx)
    g = ''
    a,b,c=tr(a,b,c)[0],tr(a,b,c)[1],tr(a,b,c)[2]
    for i in xx:
        g += str(i)
    return a+'x⁴'+b+'x²'+c+'=0',g


def gener(dif=1):
    chance = randint(1,4)
    if  chance == 4:
        xxx = [i for i in range(1,26*dif) if i % 4 == 0]
        b = xxx[randint(0,len(xxx)-1)]*choice([-1,1])
        c = b**2 // 4
        a = randint(1,15*dif)*choice([-1,1])
        b,c=b*a,c*a
        x1 = -b//(a*2)
        a,b,c=tr(a,b,c)[0],tr(a,b,c)[1],tr(a,b,c)[2]
        f = a+'x²'+b+'x'+c+'=0'
        return f,str(x1)
    else:
        x1 = randint(1,15+dif)*choice([-1,1])
        x2 = randint(1,15+dif)*choice([-1,1])
        b = -(x1+x2)
        c = (x1*x2)
        while b**2 - 4*c == 0:
            x1 = randint(1,15+dif)*choice([-1,1])
            x2 = randint(1,15+dif)*choice([-1,1])
            b = -(x1+x2)
            c = (x1*x2)            
        a = randint(1,15*dif)*choice([-1,1])
        b *= a
        c *= a
        a,b,c=tr(a,b,c)[0],tr(a,b,c)[1],tr(a,b,c)[2]
        f = a+'x²'+b+'x'+c+'=0'
        return f,str(min(x1,x2))+str(max(x1,x2))

def inf(moneys,infRezervs,pasivki):
    global money,infRez
    money,infRez=moneys,infRezervs
    if infRez == 0:
        if money >= randint(randint(325,950),randint(951,1901)) and randint(1,100) > 35:
            if randint(1,100) == randint(1,50) or randint(1,100) == randint(51,100) or randint(1,10)*pasivki[4] == 10:
                print('Произошла инфляция, но тебе повезло и бог император помог тебе сохранить твои деньги')
            else:
                print(f'Произошла инфляция и {99-59*pasivki[3]}% твоих денег сгорело. АХАХАХХАХАХАХАХАХ')
                money -= floor((money*(99-59*pasivki[3]))/100)
    else:
        infRez -= 1
        print('"Полиэтилен порвался"')

def prirost(bankM,pasivki):
    global bank
    bank = bankM
    bank += (bank * (randint(1+(pasivki[3]*9),6+(pasivki[3]*9))/10) / 100)*[1,-1][pasivki[8]]
    bank = round(bank,2)

def titr():
    print('В создании проекта приняли участие:')
    print('Егор','Лерочка','Красноволосый мальчик-погоняло Алина(вроде, я имя просто забыл пока думал титры, если что извиняюсь)','Алёна','Варя',sep='\n')
    print('Создатель, главная движущая и рабочая сила -', 'Сезик Тимофей Филиппович 2008 года рождения',sep='\n')

rubles = ['рублей','ОДНОГО РУБЛЯ']
monet = ['монет','ОДНОЙ МОНЕТЫ','денег']
winFraze = ['Нифига крутой, вытри противотанковую немецкую установку под губой','Нифига крутой - Иди домой!!! АХАХАХАХХА','Ты медуза','ЭТО НЕ ПРОСТО ГНЕВ ТО ЧТО ЖИВЕТ ВО МНЕ ПЫТАЯСЬ ВЫРВАТЬСЯ ИЗ ПОД КОНТРОЛЯ']
pochtiwinFraze = ['Нифига крутой, ладно шучу конечно','Домой','Почти мега плох','1101000010100010110100011000101100100000110100001011111111010001100000001101000010111110110100011000000111010001100000101101000010111110001000001101000010111101110100011000001111010000101110111101000010110101110100001011001011010001100010111101000010111001(UFT8)']
nowinFraze = ['Ну ты ботик конечно','Слабочек','Ультрасверхдупергипермеганевероятногигакилоэксапетатерагектодекаплох','Иди учись']
while True:
    if pasivki[-1] == 1:
        if randint(1,3) == 1:
            print('ЖАЛКИЙ ЕРЕТИК И КСЕНОС! ЗА МОЛЕНИЕ БОГАМ ХАОСА ТЫ БУДЕШЬ РАСТРЕЛЯН!!!!')
            break
    if pasivki[12] == 0:
        nnn = nwins
    if pasivki[12] == 1:
        if ((nwins-nnn)%45 == 0) and nwins-nnn != 0:
            dif += 1
    if pasivki[6] == 1:
        abilki.append(gigi)
        abVol.append(1)
        abName.append(gigi[0])
        aV = [i[1] for i in abilki]
        pasivki[6] += 1
    motion += 1
    stat = [dif,hp,wins,pwins,nwins,wins+pwins+nwins,motion] + wl[0] + wl[1] + wl[2] + box_q + abVol + aV + [money,katastrof,infRez,bank,luk,boskill]+wl3_h
    O(pasivki,stat)
    a = randint(1,50*dif)
    print(f'Угодай число jn {a - randint(1,20*dif)} lj {a + randint(1,20*dif)}  Ваши деньги: {money}',[' ',rubles[0]][pasivki[3]],end=' ')
    pp(pasivki)
    g = input()
    if (g in ['()','{}','[]','[||]']) and pasivki[11] == 1:
        lutBox(g,wep,wl,wl3_h,abilki,abVol,money,pasivki,box_q,abName)     
    elif g in abName:
        if pasivki[10] == 1:
            abVol[randint(1,len(abVol))-1] += 1
        if abVol[entry(g,abilki)] <= 0:
            print('Мошенник! За такую смеломть положена награда - прибавка к каждой способности на -578901234 едениц')
            abVol = [i-578901234 for i in abVol]
        elif g == 'Коньяк':
            print(alk[randint(1,len(alk))-1])
            abVol[7] -= 1
            break
        elif g == 'D=b2-4ac':
            abVol[5] -= 1
            if pasivki[7] == 0:
                D = gener(dif)
            else:
                D = generA(dif)
            print(D[0])
            if pasivki[0] == 1:
                print('Для балбесов: ответ -',D[1])
            print('Ответ:(jn меньшего к большему, без пробелов)',end=' ')
            otv = input()
            if otv == D[1]:
                print(f'Неплох, держи 60^2/120*dif',[monet[0],rubles[0]][pasivki[3]])
                money += (30*dif)*[1,-1][pasivki[8]]
            else:
                print(f'Такое не прощается, С ДНЕМ',[monet[1],rubles[1]][pasivki[3]],'! УРААААААА!!!')
                money = 1
        elif g == 'Слон':
            abVol[0] -= 1
            print(f'разброс от {a-randint(1,3)} до {a+randint(1,3)}')
            if pasivki[9] == 1:
                game1(input().split(),1+dif,wins,pwins,nwins,money,dif,a,pasivki)
            else:   
                game(int(input()),wins,pwins,nwins,money,dif,a,pasivki)
        elif g == 'Рубашка':
            abVol[2] -= 1
            aaa = []
            for i in range(1+randint(1,11*dif)*pasivki[5]):
                aa = [randint(0,a-1),randint(a+1,51*dif)]
                aaa.append(aa[randint(1,2)-1])
            print(f'Это не', end=' ')
            for i in aaa:
                print(i,end=' ')
            print()
            if pasivki[9] == 1:
                game1(input().split(),1+dif,wins,pwins,nwins,money,dif,a,pasivki)
            else:   
                game(int(input()),wins,pwins,nwins,money,dif,a,pasivki)
        elif g == 'Куркума':
            print('СИЛА КУРКУМЫ')
            for i in range(len(abVol)):
                abVol[i] += 1
            abVol[9] -= 2
        elif g == 'Чемодан':
            q = randint(1,len(abVol))-1
            abVol[q] += 1
            print(f'Выпадает {abilki[q][0]}')
            abVol[10] -= 1
        elif g == 'Глобус':
            abVol[8] -= 1
            print('Какую способность надобно?')
            spos = input()
            if entrys(spos,abilki) == False:
                print('Ты по мойму перепутал...')
            else:
                abVol[entry(spos,abilki)] += 1
                print('Надо было выбирать викингов...')
        elif g == 'ПНУ':
            abVol[11] -= 1
            ddd = randint(1,20)
            print('Противотанковая Немецкая Установка делает выстрел ииииииии...')
            if ddd == randint(1,20):
                print(f'говорит правильный ответ - {a}, НЕВЕРОЯТНО, ВОТ ЭТО ДА')
                print('Жаль одноразовая...')
            else:
                print('БАБАХ')
            if pasivki[9] == 1:
                game1(input().split(),1+dif,wins,pwins,nwins,money,dif,a,pasivki)
            else:   
                game(int(input()),wins,pwins,nwins,money,dif,a,pasivki)
        elif g == 'Удлинитель':
            abVol[6] -= 1
            dif += 1
            print('Мне кажется что то изменилось...')
        elif g == 'Инфляция':
            abVol[4] -= 1
            inf(money,infRez,pasivki)
        elif g == 'Геноцид':
            abVol[1] -= 1
            print('Кого стреляем?')
            g = [int(i) for i in input().split()]
            if len(g) > 10*randint(1,dif):
                print('Будь поосторожней с Геноцидом, ведь он может задеть и тебя!')
                break
            else:
                if a in g:
                    print(winFraze[randint(1,len(winFraze))-1])
                    money += (randint(250,526*dif))*[1,-1][pasivki[8]]
                    wins += 1
                elif (a+1 in g) or (a-1 in g):
                    print(pochtiwinFraze[randint(1,len(pochtiwinFraze))-1])
                    money += (randint(5,10*dif))*[1,-1][pasivki[8]]
                    pwins += 1
                else:
                    print(nowinFraze[randint(1,len(nowinFraze))-1])
                    money -= dif*[1,-1][pasivki[8]]
                    nwins += 1
        elif g == 'Огузок':
            abVol[12] -= 1
            print('Ты думал тут что-то будет?')
        elif g == 'ГЭС':
            abVol[13] -= 1
            k = randint(-50*dif,50*dif)*[1,-1][pasivki[8]]
            if k > 0:
                print(f'Вы окупились на {k}',[monet[2],rubles[0]][pasivki[3]],'!')
            elif k == 0:
                print('Вы вышли в ноль, неплохо')
            elif randint(1,10) == 1:
                if katastrof == 0:
                    katastrof += 1
                    print('Из за вашей ГЭС произошла крупная экологическая катастрофа, огромное колличество животных умерло, вы понесли КОЛОСАЛЬНЫЕ убытки!!!')
                    abVol[0] = abVol[3] = abVol[17] = abVol[19] = abVol[20] = abVol[21] = -(10**10)
                    aV[0] = aV[3] = aV[17] = aV[19] = aV[20] = aV[21] = 0
                    k -= (abs(floor(money*75/100))+abs(k*(2*randint(1,dif))))*[1,-1][pasivki[8]]
                    
                else:
                    katastrof += 1
                    print('Из за ГЭС снова произошла экологическая катастрофа, но на этот раз все обошлось только лишь КОЛОСАКЛЬНЫМИ убытками...')
                    k -= (abs(floor(money*75/100))+abs(k*(2*randint(1,dif))))*[1,-1][pasivki[8]]
            else:
                print(f'Ваши убытки составили {k}',[monet[2],rubles[0]][pasivki[3]])
            money += k
        elif g == 'Лампочка':
            if pasivki[2] == 0:
                abVol[14] -= 1
                print('Ваш инвентарь:')
                if sum(abVol) <= 0:
                    print('Пусто')
                else:
                   for i in range(len(abVol)):
                        if abVol[i] != 0:
                            print(f'{abilki[i][0]}: {abVol[i]} штук')
            else:
                abVol[14] -= 1
                print(f'Разброс jn {a-randint(1,50*dif//4)} lj {a+randint(1,50*dif//4)}')
                if pasivki[9] == 1:
                    game1(input().split(),1+dif,wins,pwins,nwins,money,dif,a,pasivki)
                else:   
                    game(int(input()),wins,pwins,nwins,money,dif,a,pasivki)
        elif g == 'Полиэтилен':
            infRez += 1
            abVol[15] -= 1
            print('Его надолго не хватит...')
        elif g == 'Мультиварка':
            abVol[16] -= 1
            print('Какую выберешь?')
            s = []
            h = randint(1,randint(1,len(abilki)))
            while len(s) != h:
                d = randint(1,len(abilki))
                if not((d-1) in s):
                    s.append(d-1)
            products = []
            for i in s:
                print(abilki[i][0])
                products.append(abilki[i][0])
            print('Выбор:',end=' ')
            shop = input().split()
            if entrys(shop[0],products):    
                abVol[entry(shop[0],abilki)] += 1
                print('Неплохой выбор, но вон та способность подошла бы больше...')
            else:
                print('Не хочешь, как хочешь...')
        elif g == 'ГимнРоссии':
            wins += 1
            abVol[-1] -= 1
            if pasivki[12] == 1:
                dif -= 1
            gimn()
        elif g == 'Рыба':
            abVol[17] -= 1
            print('Вы можете купить у рыбы:')
            s = []
            h = randint(1,randint(3,4))
            while len(s) != h and len(s) != SS(aV):
                d = randint(1,len(abilki))
                if not((d-1) in s) and aV[d-1] > 0:
                    s.append(d-1)
            products = []
            for i in s:
                k = randint(1,aV[i])
                print(f'{abilki[i][0]}: {k} штук, за одну штуку {abilki[i][2]*2+1}',[monet[2],rubles[0]][pasivki[3]])
                products.append([abilki[i][0],k,abilki[i][2]])
            print('Do you want to buy something?(yes или no)')
            ToF = input()
            if ToF == 'yes':
                print('Че из и по скоку вы хотите приобрести?')
                shop = input().split()
                if len(shop) == 1:
                    shop.append(1)
                if entrys(shop[0],products):
                    q = entry(shop[0],products)
                    if (products[q][2]*2+1) * int(shop[1]) <= money and int(shop[1]) <= products[q][1]:
                        if pasivki[10] == 1:
                            for i in range(int(shop[1])+1):
                                abVol[randint(1,len(abVol))-1] -= 1
                        money -= products[q][2] * int(shop[1])
                        aV[entry(shop[0],abilki)] -= int(shop[1])
                        abVol[entry(shop[0],abilki)] += int(shop[1])
                    else:
                        print('Обманывать не хорошо, ая-яй!')
                        pasivki[1] = 1
                else:
                    print('Нет такой буквы!')
            else:
                print('А вот это уже явно не моя проблема...')
        elif g == 'Нипон':
            abVol[18] -= 1
            print(nip())
        elif g == 'Медведь':
            if oryz(money,wep,wl,wl3_h,wep_c,pasivki,abVol,monet,rubles,boskill,bosN):
                break
            abVol[19] -= 1
        elif g == 'Пора':
            print('Поры представляют собой отверстия на поверхности клетки, обычно расположенные на неживых участках зеленых органов растений, таких как листья и стебли. Главной функцией пор является регуляция газообмена, позволяя растительным клеткам получать необходимый уровень кислорода и выводить избыток углекислого газа, который образуется в процессе фотосинтеза.Кроме того, поры также отвечают за регуляцию водного баланса растения.')
            abVol[20] -= 1
        elif g == 'Фикус':
            abVol[21] -= 1
            bank = [bank+round(bank/10),bank-round(bank/10)][randint(0,1)]
            luk = [luk-1,luk+1][randint(0,1)]
            print('Фикус сделал все что мог...')
        elif g == 'Черепаха':
            money += 1
            abVol[3] -= 1
        elif g == 'Титры':
            titr()
            abVol[22] -= 1
                   
    else:
        inf(money,infRez,pasivki)
        prirost(bank,pasivki)
        if pasivki[9] == 1:
            game1(g.split(),1+dif,wins,pwins,nwins,money,dif,a,pasivki)
        else:   
            game(int(g),wins,pwins,nwins,money,dif,a,pasivki)
        if pasivki[7] == 1 and str(randint(0,9)) in '02468':
            D = gener(dif)
            print(D[0])
            if pasivki[0] == 1:
                print('Для балбесов: ответ -',D[1])
            print('Ответ:(jn меньшего к большему, без пробелов)',end=' ')
            otv = input()
            if otv == D[1]:
                print('Неплох, держи 15*dif',[monet[2],rubles[0]][pasivki[3]])
                money += 15*dif*[1,-1][pasivki[8]]
            else:
                print(f'Такое не прощается, С ДНЕМ',[monet[1],rubles[1]][pasivki[3]],'! УРААААААА!!!')
                money = 1
        mag = randint(1,50)
        bab = randint(1,100)
        if (bab % 10 == 0 or pasivki[13] == 1) and pasivki[0] == 0:
            print('Добро пожаловать в банк!')
            print('Хотите снять или добавить деньги на счет(снять или добавить)')
            print(f'Ваш баланс текущий баланс {money}',[monet[2],rubles[0]][pasivki[3]],f'на банковском счету у вас {bank}',[monet[2],rubles[0]][pasivki[3]])
            tof = input()
            if 'снять' in tof:
                print('Сколько вы хотите снять?')
                v = float(input())
                if v > bank:
                    print('Ну вы балбес конечно...')
                    pasivki[0] = 1
                else:
                    bank -= v
                    money += round(v)
                    print('операция прошла успешно')
            elif 'добавить' in tof:
                print('Сколько хотите добавить?')
                v = int(input())
                if v > money:
                    print('Ну вы и балбес конечно...')
                    pasivki[0] = 1
                else:
                    money -= v
                    bank += v
                    print('операция прошла успешно')
            else:
                print('Ну вы и балбес конечно...')
                pasivki[0] = 1
        elif pasivki[0] == 1 and (bab % 10 == 0 or pasivki[13] == 1):
            print('С балбесами дел не имеем')
        if (mag % 10 == 7 or pasivki[13] == 1) and abVol[3] <= 0 and pasivki[11] == 0:
            print('МАГАЗИН')
            money -= (randint(5,50+1+(dif**2)*pasivki[1]))*[1,-1][pasivki[8]]
            print(f'Ваш баланс: {money}',[monet[2],rubles[0]][pasivki[3]])
            if money <= 500:
                print('Капец ты конечно ботик безденежный')
            elif money <= 1000:
                print('Все еще безденежный ботик')
            else:
                print('Ладно, так и быть, чуть-чуть богаче безденежного ботика')
            if SS(aV) == 0:
                print('Сегодня пусто, все разобрали...')
                print('Так что иди гуляй.')
            else:
                print('Вы можете приобрести:')
                s = []
                h = randint(1,randint(4,7))
                while len(s) != h and len(s) != SS(aV):
                    d = randint(1,len(abilki))
                    if not((d-1) in s) and aV[d-1] > 0:
                        s.append(d-1)
                products = []
                for i in s:
                    k = randint(1,aV[i])
                    print(f'{abilki[i][0]}: {k} штук, за одну штуку {abilki[i][2]}',[monet[2],rubles[0]][pasivki[3]])
                    products.append([abilki[i][0],k,abilki[i][2]])
                print('Вы хотите что нибудь купить(да или нет)')
                ToF = input()
                if ToF == 'да':
                    print('Какой из товаров и в каком колличестве вы хотите приобрести?')
                    shop = input().split()
                    if len(shop) == 1:
                        shop.append(1)
                    if entrys(shop[0],products):
                        q = entry(shop[0],products)
                        if products[q][2] * int(shop[1]) <= money and int(shop[1]) <= products[q][1]:
                            if pasivki[10] == 1:
                                for i in range(int(shop[1])):
                                    abVol[randint(1,len(abVol))-1] -= 1
                            money -= products[q][2] * int(shop[1])
                            aV[entry(shop[0],abilki)] -= int(shop[1])
                            abVol[entry(shop[0],abilki)] += int(shop[1])
                        else:
                            print('Пошёл ты в беброчку шулер треклятый')
                            pasivki[1] = 1
                    else:
                        print('Такого не продаем')
                else:
                    print('Бездаря ответ')
        elif (mag % 7 == 0 or pasivki[13] == 1) and abVol[3] > 0 and pasivki[11] == 0:
            if pasivki[10] == 1:
                abVol[randint(1,len(abVol))-1] += 1
            print('Черепаха спасла вас от прохода в магизин ценой своей жизни... Одтайте ей честь, это - приказ!')
            abVol[3] -= 1


        K = randint(1,30)
        if K <= 3 or pasivki[13] == 1:
            if money <= 20*dif:
                print('Казино только для богатых')
            else:
                print('Добро пожаловать в казино!')
                print(f'Вход стоит {dif*10} '+[monet[2],rubles[0]][pasivki[3]])
                print('Войдете или откажитесь(есс ор ноу)')
                ToF = input()
                if ToF == 'есс':
                    print('Приятной игры!')
                    money -= 10*dif              
                    kred = 0
                    minluk = [35,60][pasivki[14]]
                    maxluk = [60,100][pasivki[14]]
                    lots = list(range(1,randint(3,6)))
                    stavka = [[i+1,randint(10,100*dif//2)] for i in range(len(lots))]
                    nalog = [randint(1,50) for i in range(len(lots))]
                    udish = randint(1,3*len(lots))
                    fond = [[] for i in lots]
                    for i in range(udish):
                        q = randint(0,len(fond)-1)
                        fond[q].append(randint(stavka[q][1],stavka[q][1]*2))
                    print(f'Выберите лот на который будете ставить(ваш баланс {money})')
                    for i in stavka:
                        print('Лот №'+str(i[0])+': минимальная ставка - '+str(i[1])+' '+[monet[2],rubles[0]][pasivki[3]])
                    print('Выбор:',end=' ')
                    lot = int(input())
                    if lot <=0 or lot > len(lots):
                        print('Ладно, значит будет 1 лот...')
                        lot = 1
                    print('Ваша ставка -',end=' ')
                    stav = int(input())
                    if stav >= money:
                        print('Очень смело идти ва-банк')
                        stav = money
                    if stav < stavka[lot-1][1]:
                        kred = stavka[lot-1][1]-stav
                        stav = stavka[lot-1][1]
                        print(f'Ваша ставка повышена до минимальной, но теперь вы должны нам {kred} '+[monet[2],rubles[0]][pasivki[3]])
                    print(f'Итак, ваша ставка - {stav}, сумма ставок других участников - {sus(fond)}')
                    if randint(1,100) <= luk-udish:
                        print(f'Выигрышный лот - лот №{lot}, поздравляю!!!')
                        priz = stav*2-kred*2+round(round(sum([sum(fond[i])*nalog[i]/100 for i in range(len(fond))]))*40/100)
                        print(f'Вы забираете {priz} '+[monet[2],rubles[0]][pasivki[3]])
                        money += priz
                    else:
                        lots.remove(lot)
                        print(f'Выигрышний лот - лот №{lots[randint(0,len(lots)-1)]}')
                        print(f'Чтож, вы проиграли и утратили {stav+kred*2} '+[monet[2],rubles[0]][pasivki[3]])
                        money -= stav+kred*2
                    if luk >= maxluk:
                        luk = minluk
                    if luk < minluk:
                        luk = minluk
                    luk += [randint(-2,2),randint(1,6)][pasivki[14]]
                else:
                    print('ЛАДНО')
                
                    


        W = randint(1,20)
        if ((W in [1,2,3]) or pasivki[13] == 1) and pasivki[11] == 0:
            if oryz(money,wep,wl,wl3_h,wep_c,pasivki,abVol,monet,rubles,boskill,bosN):
                break

        LUT = randint(1,6)
        if (LUT == 5 or pasivki[13] == 1) and pasivki[11] == 1:
            money += [-(randint(5,50+1+(dif**2)*pasivki[1])),randint(5,50)][randint(0,1)]*[1,-1][pasivki[8]]
            print('ЛУТБОКСЫ')
            osort = choice(randi([1]*8+[2]*6+[3]*4+[4]*2))
            c = [randint(20,45),randint(50,115),randint(160,285),randint(345,555)]
            n = ['()','{}','[]','[||]']
            mag = [[i,c[i],randint(1,4)] for i in range(osort)]
            print(f'Ваш баланс: {money}',[monet[2],rubles[0]][pasivki[3]])
            print('У нас в ассортименте:')
            for i in mag:
                print(n[i[0]]+f' - {i[2]} штук, за штуку {i[1]} '+[monet[2],rubles[0]][pasivki[3]])
            print('Желаете что то купить((да/yes/надо) или (нет/no/ненадо))')
            ToF = input()
            if ToF in ['да','yes','надо']:
                print('Какой из и сколько?')
                shop = input().split()
                if len(shop) == 1:
                    shop.append(1)
                if shop[0] in n:
                    if money >= c[entry(shop[0],n)] * int(shop[1]) and int(shop[1]) <= mag[entry(shop[0],n)][2]:
                        box_q[entry(shop[0],n)] += 1
                        if pasivki[10] == 1:
                            box_q[randint(1,len(box_q))] -= 1
                    else:
                        print('Хочешь много')
            else:
                print('ну как хочешь...')
                      
                      
                
        B = randint(1,100)
        #ggg = input()
        if  ((B in [10,29,38,47,56]) or B <= 15*pasivki[13]) and wins >= 4: #or ggg == '1':
            if bossfight(money,bosN,pasivki,hp,wl,wep,wl3_h,infRez,boskill,monet,rubles,abVol,kof=randint(1,len(bosN)-1)-1):
                break
            
        if (randint(1,15) in [6,pasivki[13]]) and sum(pas) != 0 and pasivki[-1] == 0:
            print('Какую способность ты возьмешь?')
            s = []
            h = 2
            while len(s) != h and len(s) != SS(pas):
                d = randint(1,len(pas))
                if not((d-1) in s) and pas[d-1] != 0:
                    s.append(d-1)
            products = []
            for i in s:
                print(pN[i])
                products.append(pN[i])
            print('Выбор:',end=' ')
            shop = input()
            if entrys(shop,products) and shop != '':    
                pasivki[entry(shop,pN)+2] += 1
                pas[entry(shop,pN)] -= 1
                print('Ты сделал свой выбор...')
            else:
                print('Роковая ошибка...')
        
        
        if wins == 5*dif and pasivki[4] == 0:
            print('Хватит, много играть вредно для здоровья, иди лучше помолись богу императору')
            break
        elif wins == 5*dif and pasivki[4] == 1:
            print('Ладно, поиграй еще чуть-чуть....')
        elif wins == 10*dif:
            print('Хватит играть! Иди потрогай траву во имя бога Императора!!!')
            break
        elif money < 0 and pasivki[1] == 0:
            print('Вас обокрали на жизнь...')
            break
        elif money < 0 and money >= -(25*dif) and pasivki[1] == 1:
            print('Твои шулерские навыки еще позволяют держаться без денег, но какой ценой...')
            abVol[randint(1,len(abVol))-1] -= 1
            if pasivki[10] == 1:
                abVol[randint(1,len(abVol))-1] += 1
        elif money < -(25*dif):
            print('Твои навыки и так продлили тебе жизнь, но это не могло продолжаться вечно...')
            break
  
        
    
            
    
    
    
    


