def cm_to_inch(cm):
    data = cm / 2.54
    return data


def get_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)
    return
def can_bank_issue_loan(total_mortgage_payments, monthly_income):
    monthly_payment = total_mortgage_payments / 300
    return monthly_payment <= monthly_income * 0.35
