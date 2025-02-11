def calculate_lowest_payment(balance, annualInterestRate):
    monthlyPayment = balance // 12 // 10 * 10
    
    while True:
        last_balance = balance
        for i in range(12):
            unpaid_balance = last_balance - monthlyPayment
            interest = unpaid_balance * (annualInterestRate / 12.0)
            last_balance = unpaid_balance + interest
        if last_balance <= 0:
            return monthlyPayment
        monthlyPayment += 10

print("Lowest Payment: ",calculate_lowest_payment(balance, annualInterestRate))
# calculate_lowest_payment(3329, 0.2)
# calculate_lowest_payment(4773, 0.2)
calculate_lowest_payment(3926, 0.2)