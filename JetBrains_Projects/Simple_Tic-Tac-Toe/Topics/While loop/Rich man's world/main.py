limit = 700_000
interest_rate = 7.1
deposit = float(input())
amount_of_years = 0

while deposit < limit:
    deposit += deposit * interest_rate / 100
    amount_of_years += 1
print(amount_of_years)
