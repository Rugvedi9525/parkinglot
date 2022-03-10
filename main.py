from vehicle import *
from  parking_lot import *
import argparse

#Create Parking Lot
parkinglot = ParkingLot()
parkinglot.createParkinglot('Rugvedi Parking Lot', 'Mumbai, India')
parkinglot.createCapacity('small', 20)
parkinglot.createCapacity('large', 10)
parkinglot.createCapacity('xl', 5)
parkinglot.createCapacity('bike', 5)

#Create vehicle
rugvedi_audi = Vehicle(1234, 'large')
print(rugvedi_audi.getCardetails())

#Check spot availability
spot_available = parkinglot.checkAvailability(rugvedi_audi)
print(spot_available)

#generate ticket is spot available
if spot_available == True:
	tickets = parkinglot.AssignSpot(rugvedi_audi)

print(tickets[rugvedi_audi.registrationNo])

#generate bill
amount = parkinglot.Bill(rugvedi_audi,tickets)
print(amount)

#Process Paymemt
payment_status = parkinglot.ProcessPayment( rugvedi_audi, 'completed')
print(parkinglot.getCurrentStatus())

#Remove Car
if payment_status == True:
	parkinglot.RemoveCar(rugvedi_audi, tickets)
print(parkinglot.getCurrentStatus())