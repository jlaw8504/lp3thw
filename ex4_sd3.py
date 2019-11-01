# create variable cars to contain integer 100
cars = 100
# create variable space_in_a_car to contain float 4.0
space_in_a_car = 4.0
# create variable drivers to contain int 30
drivers = 30
# create variable passengers to contain int 90
passengers = 90
# subtract drivers from cars to set int variable cars_not_driven
cars_not_driven = cars - drivers
# set cars_driven variable to int value contained in drivers
cars_driven = drivers
# set carpool_capacity float variable to cars_driven
# multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# set average_passengers_per_car to int value of passengers
# divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
