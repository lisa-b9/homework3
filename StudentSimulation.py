import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 50
        self.studying_progress = 10
        self.energy = 20
        self.hunger = 20
        self.entertainment = 20
        self.thirst = 20
        self.house_energy = 10

    def to_study(self):
        print("I'm going to study...how dull :[ ")
        self.studying_progress += 2 #boring but...
        self.energy -= 0.5  # I always get tiered :_>
        self.hunger -= 0.1  #I mean , your brain needs energy!
        self.entertainment -= 0.4 #who said it's fun?
        self.thirst -= 0.1 #I mean..
        self.house_energy -= 1 #That's your energy bills :<


    def to_sleep(self):
        print("I'm going to go to bed :}")
        self.energy += 3 #now you can relax :>
        self.studying_progress -= 0.5 # I promise you, you'll definitely forget something!
        self.hunger -= 0.1 #you don't really get hungry do u?
        self.entertainment -= 0.2# I think sleeping is fun :>
        self.thirst -= 0.08# do u actually want anything while you're asleep?
        self.house_energy -= 0.5 #you may be asleep but the bills aren't

    def to_eat(self):
        print("I'm going to eat :D")
        self.energy += 1 #now you can eat :>
        self.studying_progress -= 0.5 # I promise you, you'll definitely forget something!
        self.hunger += 5
        self.entertainment -= 0.1# I think eating is fun :>
        self.thirst -= 1
        self.house_energy -= 1

    def to_drink(self):
        print("I'm going to drink:}")
        self.energy += 1  # now you can drink :>
        self.studying_progress -= 0.5  # I promise you, you'll definitely forget something!
        self.hunger += 5
        self.entertainment -= 0.1  # I think drinking is important :>
        self.thirst -= 1
        self.house_energy -= 1

    def to_relax(self):
        print("Time to relax")
        self.energy += 1  # now you can relax :>
        self.studying_progress -= 3  # If u relax, be ready to forget stuff!
        self.hunger -= 0.3  # you don't really get hungry do u?
        self.entertainment += 5  # I think relaxing is the best :>
        self.thirst -= 0.1  # u do have to hydrate!
        self.house_energy -= 1  # you're siting there watching netflix but the bills are going up!

    def to_work(self):
        print("Well, time to do some boring work!")
        self.energy -= 3  # nobody likes to work!
        self.studying_progress -= 1.5  # I mean u re  working not studying, right?
        self.hunger -= 3  # you will get hungry!
        self.entertainment += 5  # Definitely not fun!
        self.thirst -= 0.3  # u do have to hydrate!
        self.house_energy -= 1 # you're not working from home? or are you?

    def end_of_day(self):
        print(f"Energy = {self.energy}")
        print(f"Studying Progress = {round(self.studying_progress , 2)}")
        print(f"Money = {round(self.money , 2)}")
        print(f"Hunger = {round(self.hunger , 2)}")
        print(f"Fun = {round(self.entertainment, 2)}")
        print(f"Thirst = {round(self.thirst, 2)}")
        print(f"House energy = {round(self.house_energy, 2)}")

    def is_alive(self):
        if self.studying_progress < -2:
            print("Should've focused earlier...")
            return False
        elif self.entertainment <= -2:
            print("Diagnosed with depression..tough...I guess..")
            return False
        elif self.hunger < 0:
            print("Passed of famine...")
            return False
        elif self.thirst < 0:
            print("Told you to hydrate!")
            return False
        elif self.money < 0:
            print("Well, no money, no honey!")
            return False
        elif self.house_energy < 45:
            self.money -= 5
            self.house_energy += 5
        elif self.money < 20:
            self.to_work()

        return True  # Lisa is still alive

    def live(self, day):
        day_text = f"Day {day} of {self.name}'s life"
        print(f"{day_text:=^20}")

        for _ in range(5):
            live_cube = random.randint(1, 4)

            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_work()
            elif live_cube == 4:
                self.to_relax()

        self.end_of_day()

Lisa = Student(name="Lisa")

for day in range(1, 366):
    if not Lisa.is_alive():
        break
    Lisa.live(day)