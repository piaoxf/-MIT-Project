def calculate_lowest_payment(balance, annualInterestRate):
    monthly_interest_rate = annualInterestRate / 12.0
    monthlyPayment_lower_bound = balance // 12.0
    monthlyPayment_upper_bound = (balance * (1+monthly_interest_rate)**12) / 12.0
    epsilon = 0.01
    
    while True:
        last_balance = balance
        monthlyPayment = (monthlyPayment_lower_bound + monthlyPayment_upper_bound) / 2
        for i in range(12):
            unpaid_balance = last_balance - monthlyPayment
            interest = unpaid_balance * monthly_interest_rate
            last_balance = unpaid_balance + interest
        if abs(last_balance) < epsilon:
            return round(monthlyPayment,2)
        elif last_balance > 0:
            monthlyPayment_lower_bound = monthlyPayment
        elif last_balance < 0:
            monthlyPayment_upper_bound = monthlyPayment


print("Lowest Payment: ",calculate_lowest_payment(balance, annualInterestRate))

# print("Lowest Payment: ",calculate_lowest_payment(320000, 0.2))
# print("Lowest Payment: ",calculate_lowest_payment(999999, 0.18))