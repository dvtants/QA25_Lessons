import random
class User:
    names = ['Jason', 'Stacy', 'Barbara', 'Demi']
    surnames = ['Johnson', 'Johns', 'Jacobs', 'Stathem']
    def __init__(self):
        self.nick = random.choice(self.names) + '_' + random.choice(self.surnames)
        self.email = (self.nick).lower() + '@gmail.com'
        self.password = ((random.choice(self.names))[random.randint(0,2)]).upper() + \
                        ((random.choice(self.names))[random.randint(0,2)]).lower() + \
                        (random.choice(self.names))[random.randint(0,2)] + \
                        str(random.randint(0,9)) + \
                        str(random.randint(0,9)) + \
                        str(random.randint(0,9))

if __name__ == '__main__':# убрать сравнить
    a = User()
    print(a.nick, a.email, a.password)