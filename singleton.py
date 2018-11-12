#!/usr/bin/env python

class Borg:
	"""Borg class making class attributes global"""
	_shared_state = {} # Attribute dictionary

	def __init__(self):
		self.__dict__ = self._shared_state # Make it an attribute dictionary

class Singleton(Borg): #Inherits from the Borg class
	"""This class now shared all its attributes among its various instances"""

	def __init__(self, **kwargs):
		Borg.__init__(self)
		# Update the attribute dictionary by inserting a new key-value pari
		self._shared_state.update(kwargs)

	def __str__(self):
		# Returns the attribute dictionary for printing
		return str(self._shared_state)

#Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hypertext transfer protocol")
#Print the object
print(x)

#Let's create another
y = Singleton(SNMP="Simple Network Management Protocol")
#Print the object
print(y)