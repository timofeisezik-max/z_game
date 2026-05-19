#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

struct activeAbilites{char name[20];int price;} aktivka;

struct passiveAbilities{char name[20];int pool;} pasivka;

void bazaEvent(int *guessed, int *almostGuessed, int *didntGuessed, int *money, int difficulty, int target){
    int shot;
    printf("Угадай число от %d до %d  Ваши деньги: %d\n",target-(1+rand()%(20*difficulty)),target+(1+rand()%(20*difficulty)),*money);
    scanf("%d",&shot);
    if(shot==target){
        *guessed+=1;
        *money+= 250 + rand()%(400*(1+rand()%difficulty)-199);
        printf("Угадал\n");
    } else if(shot+1==target || shot-1==target){
        *almostGuessed+=1;
        *money+= 25 + rand()%(85*(1+rand()%difficulty)-24);
        printf("Почти угадал\n");
    } else{
        *didntGuessed+=1;
        *money-=difficulty;
        printf("Не угадал\n");
    }

} 

void shopEvent(int *money, struct activeAbilites abilityPool, int difficulty){
    printf("МАГАЗИН\n");
    *money -= 5 + rand()%(51+difficulty*difficulty-4);
    printf("Ваш баланс: %d",*money);
    
}

int main(){

    srand(time(NULL));

    struct activeAbilites abilityPool[7] = {
        {"Слон",450},
        {"Коньяк",1000},
        {"D=b^2-4ac",40},
        {"Мультиварка",350},
        {"Геноцид",300},
        {"Куркума",750},
        {"Лампочка",45}
    };
    
    struct passiveAbilities passiveAbilityPool[3] = {
        {"Алгебра",0},
        {"Амулет",0},
        {"Рубль",0}
    };

    int difficulty;
    printf("Выберите сложность(от 1 до 5): ");
    scanf("%d",&difficulty);
    int guessed = 0;
    int didntGuessed = 0;
    int almostGuessed = 0;
    int money = 10 + rand()%(150*(1+rand()%difficulty)-9);
    int bankBalance;
    int playerActiveAbilites[3];
    int playerPassiveAbilites[4];
    int target;
    int ivent;

    

    while(1 != 0){
        ivent = rand()%100;
        target = 1 + rand()%(50*difficulty);
        if (ivent%13==0){

        }else if(ivent == 1){

        }else{
            bazaEvent(&guessed,&almostGuessed,&didntGuessed,&money,difficulty,target);
        }
        if(money<0) break;
    }
}