# Case-study Game
# Developers:   Karunina A. (55%)
#               Smetannikova V. (53%)
#               Grishaev G. (60%)
import random
from termcolor import colored


class Game:
    st = ['фраер', 'сомнительный', 'приблатненный', 'блатной', 'пахан']

    def __init__(self, team, guns=0, n=2, t=0, food=0, flag=True):
        self.flag = flag
        self.n = n
        self.t = t
        self.food = food
        self.status = Game.st[self.n]
        if team == '1':
            self.money = 100
            self.labor = 10
            self.guns = guns
        elif team == '2':
            self.money = 120
            self.labor = 10
            self.guns = guns

    def shopping(self):
        print('Осталось денег:', self.money)
        self.ans = input('Ребята проголодались, будем закупать еду? Да / нет: ').lower()
        if self.ans == 'да':
            while self.t != -1:
                self.food_bought = int(input('Сколько пайков возьмем? '))
                if self.food_bought * 10 <= self.money:
                    self.money -= self.food_bought * 10
                    self.food += self.food_bought
                    self.t = -1
        self.t = 0
        print('Осталось денег: ', self.money)
        self.ans = input(
            'Время сейчас такое, что голыми руками мало, что можно сделать. Будем покупать кастеты? Да / нет: ').lower()
        if self.ans == 'да':
            while self.t != -1:
                print()
                k = self.money // 20
                self.guns_bought = int(input('Сколько берем? (хватает на ' + str(k) + ')? '))
                if self.guns_bought * 20 <= self.money:
                    self.money -= self.guns_bought * 20
                    self.guns += self.guns_bought
                    self.t = -1

    def war_pandemic(self):
        '''Regulated event - war, unregulated event - pandemic'''
        print(
            'События не радуют. Очередная вспышка ковида скосила несколько твоих ребят, а противники решили, что сейчас самое время забить стрелу. Придется идти, честью не рискуют. ')
        # The pandemic has resulted in three-people decreasing
        if self.labor >= 3:
            self.labor -= 3
        else:
            self.labor = 0

        self.enemy = random.randint(4, 12)
        self.enemy_guns = random.randint(0, 5)
        print('Численность противника: ', self.enemy)
        print('Кастетов у противника: ', self.enemy_guns)
        print('У тебя людей: ', self.labor)
        print('У тебя кастетов: ', self.guns)
        # Determine the probability of victory in war
        if (self.labor == self.enemy) and (self.guns == self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0, 4]:
                self.status = Game.st[self.n + 1]
                print('Красивая драка. Равная. Победа за вами!')
            else:
                self.status = Game.st[self.n - 1]
                print('Несмотря на равные условия, вы не вывезли.')
        elif (self.labor == self.enemy) and (self.guns > self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0, 5]:
                self.status = Game.st[self.n + 1]
                print('Ваши ребята оказались экипированнее. Так держать, это победа!')
            else:
                self.status = Game.st[self.n - 1]
                print(
                    'Мало купить кастеты, с ними еще нужно уметь обращаться. Похоже, этого навыка вам не хватило. Вы покинули стрелку с позором. ')
        elif (self.labor == self.enemy) and (self.guns < self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0, 3]:
                self.status = Game.st[self.n + 1]
                print(
                    'Ни одно оружие не может противостоять силе большинства и его слаженной работе. Респект, это победа в вашу копилку. ')
            else:
                self.status = Game.st[self.n - 1]
                print(
                    'Стоять с голыми руками перед вооруженной толпой — страшное дело. Шансов на победу особо и не было, но кто виноват? ')
        elif (self.labor > self.enemy) and (self.guns == self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0, 5]:
                self.status = Game.st[self.n + 1]
                print('Вас оказалось больше. Вы быстро расправились с агрессорами. Отлично!')
            else:
                self.status = Game.st[self.n - 1]
                print(
                    'Похоже, толку от численного превосходства оказалось мало, вас разбили. Не думали над тем, чтобы заглянуть в оружейный?')
        elif (self.labor > self.enemy) and (self.guns > self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0, 8]:
                self.status = Game.st[self.n + 1]
                print('Пришел, увидел, победил. Это определенно про вас. Абсолютное превосходство.')
            else:
                self.status = Game.st[self.n - 1]
                print(
                    'Одному Богу известно, как вы могли проиграть, имея такое преимущество. Будь уверен, это пагубно скажется на твоем авторитете.')
        elif (self.labor > self.enemy) and (self.guns < self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0, 4]:
                self.status = Game.st[self.n + 1]
                print(
                    'Ни одно оружие не может противостоять силе большинства и его слаженной работе. Респект, это победа в вашу копилку.')
            else:
                self.status = Game.st[self.n - 1]
                print(
                    'Стоять с голыми руками перед вооруженной толпой — страшное дело. Шансов на победу особо и не было, но кто виноват?')
        elif (self.labor < self.enemy) and (self.guns < self.enemy_guns):
            self.status = Game.st[self.n - 1]
            print('После такого невольно начинаешь сомневаться, стоило ли вообще приходить. Было больно. Очень больно.')
        elif (self.labor < self.enemy) and (self.guns == self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0]:
                self.status = Game.st[self.n + 1]
                print('Быть в меньшинстве нелегко, но техника зарешала. Враг разбит! ')
            else:
                self.status = Game.st[self.n - 1]
                print('Не стоило недооценивать силу холодного оружия. На вас снова отыгрались.')
        elif (self.labor < self.enemy) and (self.guns > self.enemy_guns):
            a = random.randint(0, 9)
            if a in [0, 2]:
                self.status = Game.st[self.n + 1]
                print(
                    'Как говорил Макиавелли: "Та война справедлива, которая необходима, и то оружие священно, на которое единственная надежда". Хоть вы и были в меньшинстве, кастеты сделали свое дело. Это победа!')
            else:
                self.status = Game.st[self.n - 1]
                print(
                    'После такого невольно начинаешь сомневаться, стоило ли вообще приходить. Было больно. Очень больно.')

    def amnesty_fire(self):
        print(
            'Вот это встреча! Без криминала на улицах обходится редко, и год назад трех твоих друзей закрыли, но выпустили за примерное поведение. Они услышали о твоем положении и хотят присоединиться к банде. Берем? Да / нет:')
        print('У тебя людей:', self.labor)
        self.a = input()
        if self.a == 'да':
            self.labor += 3
            print('У тебя людей:', self.labor)
        else:
            print(
                'О как! Старые друзья не ожидали от тебя такого ответа. Но сейчас твое слово — закон, поэтому они уходят.')
        print(
            'Похоже, твоих ребят улица научила всему, кроме обращения с огнем. Неосторжно брошенная кем-то тлеющая сигарета спровоцировала пожар. Теперь придется отстегивать денег на ремонт.')
        self.money -= 10
        print('Осталось денег:', self.money)

    def feeding(self):
        print('Народ проголодался.')
        if self.food >= self.labor:
            self.food -= self.labor
            self.status = Game.st[self.n + 1]
            print('Отлично, все накормлены.')
        else:
            print(
                'Похоже, тебе нечем кормить людей. Хочешь обменять кастеты на еду (1 кастет = 2 единицы еды)? У вас есть ',
                self.guns,
                'кастетов. Да / нет: ')
            self.ans = input()
            if self.ans == 'да':
                print('Сколько кастетов обменять? ')
                self.guns_sold = int(input())
                if self.guns_sold <= self.guns:
                    self.food += (self.guns_sold * 2)
                if self.food >= self.labor:
                    self.food -= self.labor
                    self.status = Game.st[self.n + 1]
                    print('Отлично, все накормлены.')
                else:
                    self.status = Game.st[self.n - 1]
                    print('Без комментариев. Ну, ничего не поделаешь.')
                    self.labor -= self.food
                    self.food = 0
            else:
                self.status = Game.st[self.n - 1]
                print('Без комментариев. Однако, это твой выбор. ')
                self.labor -= self.food
                self.food = 0

    def raid(self):
        '''The player has to decide whether he/she will participate in raid or will not'''
        print('Появилась тема, можно испытать судьбу и устроить рейд. Погнали? Да / нет: ')
        self.ans = input().lower()
        if self.ans == 'да':
            r = random.randint(0, 1)
            if r == 0:
                res = 'Не повезло, не повезло. Отпинали и отобрали последнее, что звенело у ребят в карманах.'
                self.money -= random.randint(10, 50)
            else:
                res = 'Фиксируем прибыль! Сегодня удача на вашей стороне.'
                self.money += random.randint(10, 50)
            return 'Итоги рейда: ' + res + '\n' + 'Деньги: ' + str(self.money)
        else:
            return 'Это твой выбор. Обойдемся без нечестных методов.'

    def res(self):
        '''The final output'''
        status = self.status
        money = str(self.money)
        guns = str(self.guns)
        labor = str(self.labor)
        if self.labor <= 0:
            self.flag = False
        if status == Game.st[0]:
            self.flag = False
        if self.flag == True:
            return 'Пора посмотреть, к чему ты привел свою банду. ' + '\n' + 'Статус: ' + status + '\n' + 'Люди: ' + labor + '\n' + 'Кастеты: ' + guns + '\n' + 'Деньги: ' + money + '\n' + 'На этом история не заканчивается, встретимся в следующем году.'
        else:
            return 'Пора посмотреть, к чему ты привел свою банду. ' + '\n' + 'Статус: ' + status + '\n' + 'Люди: ' + labor + '\n' + 'Кастеты: ' + guns + '\n' + 'Деньги: ' + money

    def minus(self):
        if self.money < 0 or self.labor <= 0:
            return False
        else:
            return True

    def next(self):
        return self.flag


print(colored("ЗА ГАРАЖАМИ", 'red'))
print('')
# здесь введение в игру. правила
print(
    'Ну что, бродяга, сегодня жизнь тебе улыбнулась. Пара нужных знакомств, и вот тебе предлагают возглавить одну из двух молодых районных группировок. У каждого района свой колорит, выбирай, кто тебе ближе.')
print('')
print(colored('1) ОПГ "Затулинка"', 'blue'))
print(
    'Говорят, именно по этому району Элджей скромно двигал на Air Jordan, чем и поделился в треке "Бошки дымятся". Неудивительно, что двигался именно скромно: судя по новостям в Новосибирских СМИ с тегом "Затулинка", по ней в целом-то передвигаться страшно, но не такому как ты.')
print('')
print(colored('2) ОПГ "Дзержинка"', 'blue'))
print(
    'Многие люди летают за рубеж, чтобы посмотреть на иностранцев и познакомиться с их культурой. А могли просто съездить в Дзержинский. Может, про местные улицы и не читал Элджей, зато здесь можно найти Мияги, который за шаурму исполнит все свои хиты вживую. ')
print('')
team = input('Введи номер команды, которую поведешь: ')
print('')
print(
    'Поздравляю, камрад, теперь у тебя в подчинении ребята, которые кого угодно (почти) напугают сильнее, чем студента бизнес-информатики диффуры. Но чтобы пугать, нужны силы, так что парней надо кормить, и теперь это твоя обязанность. Паек на человека стоит 10 рублей. Голод — главный враг твоих подопечных. Тот, кого ты не смог прокормить, умирает и из загробного мира, к сожалению, не возвращается, а терять людей не в твоих интересах.')
print('')
print(
    'Предупрежден — значит вооружен. В районных реалиях все настолько непредсказуемо, что ты вряд ли когда-то будешь о чем-то предупрежден, но вот вооружаться ты можешь. Твое оружие — кастет. Один кастет стоит 20 рублей. Чем больше в твоей банде вооруженных ребят, тем больше у тебя шансов отовсюду выйти победителем.')
print('')
print(colored('Авторитет', 'red'))
print(
    'Реальные пацаны чаще всего дерутся именно за респект. И не зря: авторитет определяет лидера, и исход твоей бандитской карьеры зависит именно от него. Всего существует 5 уровней авторитета.')
print(
    '1) Фраер — беги, пока не поздно. Ты растерял последние капли уважения, в глазах собственного окружения ты хуже рядового. При достижении такого статуса игра для тебя заканчивается. Будет ли этот исход летальным зависит от того, как быстро ты бегаешь.')
print(
    '2) Сомнительный — похоже, косяков за тобой много, но еще не все потеряно. Остались люди, которые верят в тебя и твое благоразумие в будущем.')
print(
    '3) Приблатненный — это твой статус в начале игры. Хоть ты для банды и не эталон, но тебе хотя бы никто особо не перечит.')
print(
    '4) Блатной — дела идут в гору, с твоим мнением считаются, уважают за грамотное управление и защиту чести. Дальше — больше.')
print('5) Пахан — о большем и мечтать нельзя. Твоя власть безгранична, на тебя смотрят, как на небожителя. Это победа!')
print(
    'Заработать авторитет можно, побеждая на стрелках. Потерять его гораздо легче. Мнение о тебе ухудшается, если ты не смог обеспечить всех едой или не смог отстоять честь банды на стрелке.')
print('')
print(colored('Стрелки', 'red'))
print(
    'Жизнь без насилия была бы скучной. По крайней мере, так считают парни из другого района. Поэтому периодически они забивают стрелы, чтобы показать, кто здесь самый ровный, самый сильный, самый четкий. Чтобы поставить их на место и не потерять авторитет, нужно заставить их сдаться. На улицах все просто: кто сильнее, тот и прав. Чем больше у тебя людей и кастетов, тем выше твои шансы на победу. Победил — стал еще выше в глазах своей банды, проиграл — наоборот. ')
print('')
print(colored('Рейды', 'red'))
print(
    'Районная суета отнимает слишком много времени и сил, так что дети улиц не работают. Но еда и кастеты, к сожалению, не бесплатные. Хорошо, что существуют соседи, у которых можно позаимствовать пару десятков рублей. И даже возвращать не придется. Для этого можно устроить рейд. У рейда два исхода: либо тебе везет, и твои ребята приносят деньги, либо их ловят с поличным и забирают наличку, чтоб не повадно было.')
print('')
print(colored('Теперь ты готов ко всему. Почти ко всему. Игра началась. Удачи!', 'blue'))
print('')

if team == '1':
    c = Game('1', 0)
    k = c.next()
    while k == True:
        i = random.randint(1, 2)
        c.shopping()
        if c.minus() == False:
            k = False
        if i == 1:
            c.war_pandemic()
        elif i == 2:
            c.amnesty_fire()
        c.feeding()
        if c.minus() == False:
            k = False
        print(c.raid())
        if c.minus() == False:
            k = False
        print(c.res())
        if c.minus() == False:
            print(colored(
                'Ты не оправдал ожиданий. Давно твоих парней не видели такими обозленными. Твоя история на этом закончена.',
                'red'))
            k = False
elif team == '2':
    s = Game('2', 0)
    h = s.next()
    while h == True:
        i = random.randint(1, 2)
        s.shopping()
        if s.minus() == False:
            h = False
        if i == 1:
            s.war_pandemic()
        elif i == 2:
            s.amnesty_fire()
        s.feeding()
        if s.minus() == False:
            k = False
        print(s.raid())
        if s.minus() == False:
            h = False
        print(s.res())
        if s.minus() == False:
            print('К сожалению, игра окончена')
            k = False

