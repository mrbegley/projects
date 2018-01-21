import math

print "\nWelcome to my expense thing\n"
print "-"*50

monthly_income = raw_input("What is your Monthly income? [+] $")
rent = raw_input("Monthly price for rent? [+] $")
gas = raw_input("Monthly price for gas? [+] $")
food = raw_input("Monthly price for food [+] $")
electricity = raw_input("Monthly price for electricity? [+] $")
Wi_Fi = raw_input("Monthly price for Wi_Fi? [+] $")
Credit_Cards = raw_input("Current monthly amount due for Credit Card(s)? [+] $") 
misc = raw_input("Price for misc? [+] $")

total_expenses = int(gas) + int(electricity) + int(Wi_Fi) + int(Credit_Cards) + int(misc) + int(food)
left_over = int(monthly_income) - int(total_expenses)

print "-"*50
print "\nYour total expenses are : [+] $%s" % total_expenses
if left_over > 0:
	print "You save about : [+] $%s" % left_over
	print "Save that money!"
if left_over < 0:
	print "You lose about : [+] $%s" % left_over
	print "Do better!"

print "-"*50
print "\nMain Menu"
print "select by the number"
print "[1] view "
print "[2] "

def whattodo():
	print "-"*50
	print "\n"

