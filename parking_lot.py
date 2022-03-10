import datetime


class ParkingLot():
	def __init__(self):
		self.parkinglotCapacity = {'small':0,'large':0,'xl':0,'bike':0}
		self.occupiedCapacity = {'small':0,'large':0,'xl':0,'bike':0}
		self.availableSpots = {'small':[],'large':[],'xl':[],'bike':[]}
		self.occupiedSpots = {'small':[],'large':[],'xl':[],'bike':[]}
		self.tickets = {}
		self.payment = {'small': 80,'large':100, 'xl':150, 'bike':50}

	def createParkinglot(self, name, address):
		self.name = name
		self.address = address
		return self.name, self.address

	def createCapacity(self, slotType, slotCapacity):
		self.parkinglotCapacity[slotType] = slotCapacity
		self.availableSpots[slotType] = list(range(1,slotCapacity+1))
		return self.parkinglotCapacity, self.availableSpots

	def checkAvailability(self, vehicle):
		if self.occupiedCapacity[vehicle.carType] >= self.parkinglotCapacity[vehicle.carType]:
			return False
		else:
			return True

	def AssignSpot(self, vehicle):
		spot = self.availableSpots[vehicle.carType][-1]
		self.occupiedSpots[vehicle.carType].append(self.availableSpots[vehicle.carType][-1])
		print(spot)
		ticket = self.generateTicket(vehicle, spot)
		self.availableSpots[vehicle.carType].pop()
		self.occupiedCapacity[vehicle.carType] += 1
		return self.tickets
		
	def generateTicket(self, vehicle, spot):
		self.tickets[vehicle.registrationNo] = [spot,datetime.datetime.now(),'Active']

	def Bill(self, vehicle, tickets ):
		hours = 2
		amount = self.payment[vehicle.carType]*2
		return amount

	def ProcessPayment(self, vehicle, payment):
		if payment == 'completed' or payment == 'Completed':
			self.tickets[vehicle.registrationNo][-1] = 'Completed'
			return True
		else:
			return False

	def RemoveCar(self, vehicle, tickets):
		self.availableSpots[vehicle.carType].insert(0, tickets[vehicle.registrationNo][0])
		print(self.occupiedSpots)
		self.occupiedSpots[vehicle.carType].remove(tickets[vehicle.registrationNo][0])
		self.occupiedCapacity[vehicle.carType] -= 1
		
	def getCurrentStatus(self):
		return self.parkinglotCapacity, self.occupiedSpots





















