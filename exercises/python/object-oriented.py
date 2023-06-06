# OOP in Python

# Exercise 9.1 – Classes and Objects
# Create a class called MyRecipe with two fields calories and cooking_time. 
# Add a cook() function to simulate cooking by just printing out a message. 
# Create the corresponding object and print out five of your favourite recipes.

class MyRecipie:
    calories = 0
    cooking_time = 0
    
    def __init__(self, cals, time) -> None:
        self.calories = cals
        self.cooking_time = time
    
    def cook(self):
        print(f"mmm this delicious recipie is cooking wow, its going to take {self.cooking_time} minutes and going to have {self.calories} kcal")
        
newRecipie = MyRecipie(500, 20)

newRecipie.cook()

# Exercise 9.2 – Inheritance
# multiple inheritance
# Implement the following class diagram paying attention to the two parent __init__ methods and a new attribute phone, 
# assuming we want to add a phone number for our close friends. 
# Test your implementation.

class Contact:

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def __str__(self):
        return f'name: {self.name}, email: {self.email}'
    
    
class AddressHolder:
    
    @property
    def street(self):
        return self.__street
    
    @street.setter
    def street(self, value):
        self.__street = value
    
    @property
    def postcode(self):
        return self.__postcode
    
    @postcode.setter
    def postcode(self, value):
        self.__postcode = value
        
    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, value):
        self.__city = value
    
    def __init__(self, street, postcode, city) -> None:
        self.__street = street
        self.__postcode = postcode
        self.__city = city
        
    def __str__(self) -> str:
        return f'address: {self.street}, postcode: {self.postcode}, city: {self.city}'
    
    
class Friend(Contact, AddressHolder):
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value
        
    def __init__(self, name, email, street, postcode, city, phone):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, postcode, city)
        self.__phone = phone
        
    def __str__(self):
        Contact.__str__(self)
        AddressHolder.__str__(self)
        return f'{Contact.__str__(self)}, {AddressHolder.__str__(self)}, phone: {self.phone}'
    
    
    
friend = Friend(
    name="John Doe",
    email="johndoe@example.com",
    street="123 Main St",
    postcode="12345",
    city="Anytown",
    phone="555-555-5555"
)

print(friend)
  
# Polymorhism

class Fish:

    def eat(self):
        print("Da fish is eating!")
        
    def swim(self):
        print("Da fish is swimming wow look!?")
    
class Shark(Fish):  
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def placeFound(self):
        return self.__placeFound
    
    @placeFound.setter
    def placeFound(self, value):
        self.__placeFound = value
        
    def __init__(self, name, placeFound):
        self.__name = name
        self.__placeFound = placeFound
    
    def eat(self):
        print(f"Da Shark {self.name} is eating whaaat??!")
        
    def swim(self):
        print(f"Da fish is swimming wow look!? He lives in {self.placeFound} wassup?")
        
        
class Dolphin(Fish):  
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    def __init__(self, name):
        self.__name = name
    
    def eat(self):
        print(f"Da Dolphin {self.name} is eating whaaat??!")
        
    def swim(self):
        print(f"Da fish {self.name} is swimming wow look!? He's homeless though")
        
        
# Create a new Shark instance
shark = Shark(name="J dawg", placeFound="Brooklin")
shark.eat()  # Outputs: Da Shark J dawg is eating whaaat??!
shark.swim()  # Outputs: Da fish is swimming wow look!? He lives in Brooklin

# Create a new Dolphin instance
dolphin = Dolphin(name="Trevor")
dolphin.eat()  # Outputs: Da Dolphin Trevor is eating whaaat??!
dolphin.swim()  # Outputs: Da fish Trevor is swimming wow look!? He's homeless though


# Exercise 9.4 - Extra
# Implement the following class diagram. 
# Note that the CaffeineDrink is an abstract class and get_price() an abstract method.

from abc import ABC, abstractmethod

class CaffeineDrink(ABC):
    
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        self.__description = value
        
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value
    
    def __init__(self, description, size):
        self.__description = description
        self.__size = size
    
    def drinkInfo(self) -> str:
        return f"description: {self.description}, size: {self.size}"
        
    @abstractmethod
    def getPrice(self):
        pass
    
    
class Coffee(CaffeineDrink):
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
        
    @property
    def taxRate(self):
        return self.__taxRate
    
    @taxRate.setter
    def taxRate(self, value):
        self.__taxRate = value
    
    def __init__(self, description, size, quantity, taxRate):
        super().__init__(description, size)
        self.__quantity = quantity
        self.__taxRate = taxRate
    
    def getPrice(self):
        basePrice = 10
        finalPrice = (basePrice * self.quantity) * (self.taxRate/100 + 1)
        return finalPrice
    
    
class Tea(CaffeineDrink):
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
    
    def __init__(self, description, size, quantity):
        super().__init__(description, size)
        self.__quantity = quantity
        
    def getPrice(self):
        basePrice = 5
        finalPrice = basePrice * self.quantity 
        return finalPrice
    
    
# Creating instances of Coffee and Tea classes
coffee = Coffee("Freshly brewed coffee", "Large", 2, 10)
tea = Tea("Chamomile tea", "Small", 1)

# Printing drink info and price
print(coffee.drinkInfo())  # Outputs: description: Freshly brewed coffee, size: Large
print("Coffee price: ", coffee.getPrice())  # Should output the price for 2 large coffees with a 10% tax

print(tea.drinkInfo())  # Outputs: description: Chamomile tea, size: Small
print("Tea price: ", tea.getPrice())  # Should output the price for 1 small tea
