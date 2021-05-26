import math
# Coding excersize for loans


def calculate_loan():
    loan_amt = int(input("Please input the loan amount: "))
    interest_rate = int(input("Please input the interest rate for the loan: "))
    time_in_months = int(input(
        "Please input the desired number of months to pay off the loan: "))

    # Example formulae successful
    test_formulae = ((6.5 / 100 / 12) * 200000) / \
        (1 - ((1 + (6.5 / 100 / 12)) ** (-30 * 12)))
    # print(test_formulae)

    # should be doable with mathmetical formulae
    month_payment = ((interest_rate / 100 / 12) * loan_amt) / \
        (1 - ((1 + (interest_rate / 100 / 12)) ** (time_in_months * -1))
         )  # multiply by negative one to match formulae
    print(str(math.ceil(month_payment)) + ' is your monthly bill')


calculate_loan()
