portion_down_payment = .25
current_savings = 0
r = .04
annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = .07

# bisection search to find the best savings rate
low = 0
high = 10000
steps = 0
while abs(current_savings - total_cost * portion_down_payment) > 100:
    current_savings = 0
    steps += 1
    portion_saved = (low + high) / 2
    monthly_salary = annual_salary / 12
    for month in range(1, 37):
        current_savings += current_savings * r / 12
        current_savings += monthly_salary * portion_saved / 10000
        if month % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    if current_savings < total_cost * portion_down_payment:
        low = portion_saved
    else:
        high = portion_saved

if steps > 13:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search:", steps)
