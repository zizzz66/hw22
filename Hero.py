
class SuperHero:
    people='people'

    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        print("Адмирал", self.name)


    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return F'nickname: {self.nickname}  superpower: {self.superpower}\n' \
               F'health_points:  {self.health_points} catchphrase:  {self.catchphrase} '



hero = SuperHero('Гарп', 'Монкиди', 'power', 10000, 'волосы не зубы отрастут!')
hero.get_name()
hero.double_health()
print(hero)



def catchphrase (hero):
    return len(hero00)
hero00 = "волосы не зубы отрастут!"
length = catchphrase(hero)
print("Длина коронной фразы героя:", length)
