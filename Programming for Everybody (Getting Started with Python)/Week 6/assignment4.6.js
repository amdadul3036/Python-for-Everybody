def computepay(hours,rate):

	if hours > 40:

		pay = rate * 40.0

		pay = pay + (1.5*rate*(hours - 40))

	else:

		pay = rate * 40

	return pay

#return 42.37

hours = float(input("Enter Hours:"))

rate = float(input("Enter rate per hour: "))

p = computepay(hours,rate)

print('Pay',p)