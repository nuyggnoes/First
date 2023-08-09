class Human:
    def __init__(self,name):
        self.name=name 

    def say_hello(self):
        print(f"hello my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp

class Fan(Human):
    def __init__(self,name,fav_team):
        super().__init__(name)
        self.fav_team =fav_team

steve_player = Player("steve", 1000)
steve_fan = Fan("steve_fan", "dontknow")
steve_player.say_hello()