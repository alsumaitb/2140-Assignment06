# Assignment 06, Question 01

class Animal:
    def eat(self):
        print("Animal is eating.")
        
    def sleep(self):
        print("Animal is sleeping")
        
class Mammal(Animal):
    def eat(self):
        print("Mammal is eating.")
        
    def sleep(self):
        print("Mammal is sleeping")
    
class Bird(Animal):
    def eat(self):
        print("Bird is eating.")

    def sleep(self):
        print("Bird is sleeping")
    
class Fish(Animal):
    def eat(self):
        print("Fish is eating.")
        
    def sleep(self):
        print("Fish is sleeping")
        
class Dog(Mammal):
    def eat(self):
        print("Dog is eating.")
        
    def sleep(self):
        print("Dog is sleeping")
    
class Tuna(Fish):
    def eat(self):
        print("Tuna is eating.")
        
    def sleep(self):
        print("Tuna is sleeping")
 
class Eagle(Bird):
    def eat(self):
        print("Eagle is eating.")
        
    def sleep(self):
        print("Eagle is sleeping")
    
def call_eat(animal):
    animal.eat()
    
def main():
    dog = Dog()
    animal = Animal()
    fish = Fish()
    eagle = Eagle()
    
    objects = [dog, animal, fish, eagle]
    
    for a in objects:
        call_eat(a)
    
main()

