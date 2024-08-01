class Animal:     #Родитель
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):  # Результат поедания чего ли-бо
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Mammal(Animal): #наследник

    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):   #наследник

    def __init__(self, name):
        super().__init__(name)



class Plant:      #Родитель

    def __init__(self, name):
        self.name = name
        self.edible = False

class Flower(Plant):     #наследник

    def __init__(self, name):
        super().__init__(name)
        self.edible = True

class Fruit(Plant):      #наследник

    def __init__(self, name):
        super().__init__(name)
        self.edible = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.


