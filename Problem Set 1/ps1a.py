portion_down_payment = .25
current_savings = 0
r = .04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Calculate the number of months it will take to save for the down payment
months = 0
while current_savings < total_cost * portion_down_payment:
    current_savings += annual_salary / 12 * portion_saved + current_savings * r / 12
    months += 1

print("Number of months:", months)
