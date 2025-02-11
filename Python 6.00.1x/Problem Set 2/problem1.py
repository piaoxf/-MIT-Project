# input
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
  monthlyPayment = balance * monthlyPaymentRate
  unpaid_balance = balance - monthlyPayment
  interest = unpaid_balance * annualInterestRate / 12.0
  balance = unpaid_balance + interest
  print('Month ', i + 1)
  print('Remaining balance: ', round(balance, 2))

print('Remaining balance: ', round(balance, 2))