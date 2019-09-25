name = input("What is your name?")
print("What's up", name, "my name is Herbert, but you can call me Herb. Where are you from?")
place = input()
print("Woah,", place, "sounds like a great place to live.")
number = int(input("What is your favorite number?"))
my_number = 3 * number
print("That's so cool, my favorite number", my_number, "is three times bigger than your favorite number", number)
car = input("What is your dream car?")
print("Dang", name, "I see you. A", car, "is a great car.")
price = float(input("How much does it cost?"))
print("Golly", price, "is a lot of dinero. If you took out a loan, how many years would you make it?")
years = float(input())
print("What would the annual interest rate (percent) be?")
monthly_interest_rate = float(input())
number_of_monthly_payments = years * 12
monthly_interest_rate = monthly_interest_rate / 100 / 12
monthly__cost = float(monthly_interest_rate * price) / (1 - (1 + monthly_interest_rate)**-number_of_monthly_payments)
print("If you bought a", car, "your monthly cost would be,", monthly__cost, "per month.")
total_cost = monthly__cost * 12 * years
print("And the total cost would be,", total_cost)


