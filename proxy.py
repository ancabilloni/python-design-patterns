#!/usr/bin/env python
import time

class Producer:
	"""Define the `resource-intensive` object to instatiate!"""
	def produce(self):
		print("Producer is working hard!")

	def meet(self):
		print("Producer has time to meet you now!")

class Proxy:
	"""Define the `relatively less resource-intensive` proxy to instatiate as a middleman"""
	def __init__(self):
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		"""Check if Producer is available"""
		print("Artist checking if Producer is available...")

		if self.occupied == 'No':
			#If the producer is available, create a producer object!
			self.producer=Producer()
			time.sleep(2)

			#Make the producer meet the guest!
			self.producer.meet()
		else:
			#Otherwise, don't instaiate a producer
			time.sleep(2)
			print("Producer is busy!")

#Instatiate a Proxy
p = Proxy()

#Make the proxy: Artist produce until Producer is available
p.produce()

#Change the sate to 'occupied'
p.occupied="Yes"

#Make the Producer produce
p.produce()