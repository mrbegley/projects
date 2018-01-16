import math
import sys

print "\nWelcome to my expense thing\n"
print "-"*50

monthly_income = raw_input("What is your Monthly Income? [+] $")
rent = raw_input("Monthly price for Rent? [+] $")
gas = raw_input("Monthly price for Gas? [+] $")
food = raw_input("Monthly price for Food [+] $")
electricity = raw_input("Monthly price for Electricity? [+] $")
Wi_Fi = raw_input("Monthly price for Wi_Fi? [+] $")
Credit_Cards = raw_input("Current monthly amount due for Credit Card(s)? [+] $") 
insurance = raw_input("Current monthly price for Insurance [+] $")
misc = raw_input("Price for Miscellaneous? [+] $")

total_expenses = int(gas) + int(electricity) + int(Wi_Fi) + int(Credit_Cards) + int(misc) + int(food) + int(insurance)
left_over = int(monthly_income) - int(total_expenses)

print "-"*50
print "\nYour total expenses are : [+] $%s" % total_expenses
if left_over > 0:
    print "You save : [+] $%s" % left_over
    print "Save that money!"
if left_over < 0:
    print "You lose : [+] $%s" % left_over
    print "Do better!"

print "-"*50
print "\n[+] Main Menu\n"
print "-"*50
print "\nSelect by the number"
print "\n[1] Save expenses to a file"
print "[2] View expenses once more"
print "[3] View how to better your savings\n"

option = raw_input("[+] ")

def number_1():
    print "-"*50
    file = open('expenses.txt', 'w')
    file.write('Rent: $%s\n' % int(rent))
    file.write('Gas: $%s\n' % int(gas))
    file.write('Food: $%s\n' % int(food))
    file.write('Electricity: $%s\n' % int(electricity))
    file.write('Wi-Fi: $%s\n' % int(Wi_Fi))
    file.write('Credit Cards: $%s\n' % int(Credit_Cards))
    file.write('Insurance: $%s\n' % int(insurance))
    file.write('Miscellaneous: $%s\n' % int(misc))
    file.write('Total: $%s') % int(total_expenses)
    file.close()

def number_2():
    print "Rent: $%s\n" % int(rent)
    print "Gas: $%s" % int(gas)
    print "Food: $%s" % int(food)
    print "Electricity: $%s" % int(electricity)
    print "Wi-Fi: $%s" % int(Wi_Fi)
    print "Credit Cards: $%s" % int(Credit_Cards)
    print "Insurance: $%s" % int(insurance)
    print "Miscellaneous: $%s" % int(misc)
    print "\nTotal Expenses: $%s" % int(total_expenses)

def number_3():
   print "Invest in tron..." 

if option == '1':
    number_1()
if option == '2':
    number_2()
if option == '3':
    number_3()
