#!/usr/bin/env python

class Dog:
	"""A Simple dog class"""
	
	# def __init__(self, name):
	# 	self._name = name

	def __str__(self):
		return "Dog"

	def speak(self):
		return "Woof!"

class Cat:
	"""A Simple cat class"""
	
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"

def get_pet(pet="dog"):

	"""The factory method"""

	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

	return pets[pet]

# d=get_pet("dog")
# print(d.speak())

# c = get_pet("cat")
# print (c.speak())

# ABSTRACT FACTORY
# Problem: The user expectation yields multiple, related objects
# Scenario: Pet factory - dog factory, cat factory
# Solution: Abstract factory: pet factory, Concreate factory: dog factory and cat factory, abstract product
# concreate product: dog and dog food; cat and cat food.

class DogFactory:
	"""Concreate factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object"""
		return "Dog Food!"

class PetStore:
	"""PetStore houses our Abstract Factory"""
	def __init__(self, pet_factory=None):
		"""pet_factory is our Abstract factory"""
		self._pet_factory = pet_factory

	def show_pet(self):
		"""Utility method to display the details of the objects returned by the DogFactory"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'".format(pet_food))

# Create a concreate factory
factory = DogFactory()

# Create a pet store housing our Abstract factory
shop = PetStore(factory)

# Invoke the utility method to show the details of our pet
shop.show_pet()

